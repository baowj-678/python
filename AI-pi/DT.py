import pandas as pd
import numpy as np
import copy

def load_file(fileName):
    text = pd.read_csv(fileName, delimiter='\t')
    values = text.values
    data = np.zeros([values.shape[0], 14])
    for i in range(values.shape[0]):
        string = values[i][0]
        data_temp = string.split(' ')
        while '' in data_temp:
            data_temp.remove('')
        data[i] = data_temp
    return data

class DecisionTree():
    def __init__(self):
        pass
    
    def generateTree(self, data, features):
        self.Tree = self.train(data, features)
        return self.Tree

    def train(self, data, features):
        n = data.shape[0]
        m = data.shape[1] - 1
        k = features.shape[0]
        if(data.shape[0] == 0):
            return
        elif(data.shape[0] == 1):
            return data[0, k]
        if(features.shape[0] == 0):
            return
        elif(features.shape[0] == 1):
            # the data col will be calc
            data = data[data[:, 0].argsort(),:]
            # S initialization
            S = np.zeros(n)
            S[0] = data[0, 0] - 0.01
            for i in range(n - 1):
                S[i + 1] = (data[i, 0] + data[i + 1, 0])/2
            # C1 initialization
            C1 = np.zeros(n)
            C1[0] = 0
            for i in range(1, n, 1):
                C1[i] = C1[i - 1] + data[i - 1, 1]
            for i in range(1, n, 1):
                C1[i] = C1[i]/i
            # C2 initialization
            C2 = np.zeros(n)
            C2[n - 1] = data[n - 1, 1]
            for i in range(n - 2, -1, -1):
                C2[i] = (C2[i + 1] + data[i, 1])
            for i in range(n - 2, -1, -1):
                C2[i] = C2[i]/(n - i)
            # calc Loss
            Loss = np.zeros(n)
            for i in range(n):
                Loss[i] = np.sum((data[: i, 1] - C1[i])**2) + np.sum((data[i:, 1] - C2[i])**2)
            index = np.argmin(Loss)
            s = S[index]
            R = {}
            R[(features[0], 1, s)] = C2[index]
            R[(features[0], 0, s)] = C1[index]
            return R
        
        else:
            Loss_split = np.zeros(k)
            Loss_index = np.zeros(k, dtype=int)
            Loss_value = np.zeros(k)
            Loss_C = np.zeros([k, 2])
            for i in range(k):
                # the data be used
                data = data[data[:, i].argsort(), :]
                # S initialization, the number to split data
                S = np.zeros(n)
                S[0] = data[0, i]/2
                for j in range(n - 1):
                    S[j + 1] = (data[j, i] + data[j + 1, i])/2
                # C1 initialization, left average
                C1 = np.zeros(n)
                C1[0] = 0
                for j in range(1, n, 1):
                    C1[j] = C1[j - 1] + data[j - 1, k]
                for j in range(1, n, 1):
                    C1[j] = C1[j]/j
                # C2 initialization, right average
                C2 = np.zeros(n)
                C2[n - 1] = data[n - 1, k]
                for j in range(n - 2, -1, -1):
                    C2[j] = C2[j + 1] + data[j, k]
                for j in range(n - 2, -1, -1):
                    C2[j] = C2[j]/(n - j)
                Loss_ = np.zeros(n)
                for j in range(n):
                    Loss_[j] = np.sum((data[: j, k] - C1[j])**2) + np.sum((data[j :, k] - C2[j])**2)
                index = np.argmin(Loss_)
                Loss_split[i] = S[index]
                Loss_index[i] = index
                Loss_value[i] = Loss_[index]
                # Loss_C[i, 0] = C1[index]
                # Loss_C[i, 1] = C2[index]

            index = np.argmin(Loss_value)
            s = Loss_split[index]
            data = data[data[:, index].argsort(), :]
            data = np.delete(data, i, axis=1)
            data1 = data[:Loss_index[index], :]
            data2 = data[Loss_index[index]:, :]
            feature = features[index]
            features = np.delete(features, index, axis=0)
            R = {}
            if(data2.shape[0] == 0 or data1.shape[0] == 0):
                R[(feature, 1, 0)] = self.train(data, features)
            else:
                R[(feature, 1, s)] = self.train(data2, features)
                R[(feature, 0, s)] = self.train(data1, features)
            return R
    
    def self_predict(self, data):
        label = np.zeros(data.shape[0])
        for i in range(data.shape[0]):
            label[i] = self.predict_single(self.Tree, data[i])
        return label

    def tree_predict(self, Tree, data):
        label = np.zeros(data.shape[0])
        for i in range(data.shape[0]):
            label[i] = self.predict_single(Tree, data[i])
        return label

    def predict_single(self, tree, data):
        if(type(tree) is not dict):
            return tree
        is_ok = False
        for k,v in tree.items():
            if(k[1] == 0 and data[k[0]] < k[2]):
                is_ok = True
                return self.predict_single(v, data)
            elif(k[1] == 1 and data[k[0]] >= k[2]):
                is_ok = True
                return self.predict_single(v, data)
            
        if(is_ok == False):
            print(tree, data)

    def cutBranch(self, data, alpha):
        self.alpha = alpha
        self.data = data
        self.cutBranchSubTree(copy.deepcopy(self.Tree))
        return 

    def cutBranchSubTree(self, Tree):
        subtree = 0
        if(type(Tree) is not dict):
            return (1, Tree)

        for k,v in Tree.items():
            n, t = self.cutBranchSubTree(v)
            Tree[k] = t
            subtree += n
        
        labels = np.zeros(self.data.shape[0])
        for i in range(labels.shape[0]):
            labels[i] = self.predict_single(Tree, self.data[i])
        C_Tt = np.sum((labels - self.data[:, -1])**2)
        C_t = np.average(self.data[:, -1])
        C_t = np.sum((self.data[:, -1] - C_t)**2)
        g_t = (C_t - C_Tt)/max((subtree - 1), 1)
        if(max(g_t, self.alpha) == self.alpha):
            return (1, C_t)
        else:
            self.alpha = g_t
            return (subtree, Tree)



fileName = "D:\\我的课件\\AI-pi\\2019年AI π竞赛队暑期招新初选赛题\\2019年AI π竞赛队暑期招新初选赛题\\数据.data"
data = load_file(fileName)

np.random.shuffle(data)
print(data.shape)
dt = DecisionTree()
features = np.linspace(0, 12, 13, dtype=int)
# train
dt.generateTree(data[: 450, :], features)

# predict
# pre = dt.predict(data[450 :, :])
# print(pre-data[450 :, 13])
test = data[450 :, :]
print(dt.cutBranch(test, 9))


