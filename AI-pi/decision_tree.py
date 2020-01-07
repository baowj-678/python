import numpy as np
import pandas as pd
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

    def loadData(self, data, features):
        self.data = data
        self.features = features

    def loadTree(self, Tree):
        self.Tree = Tree

    def train(self, data, features):
        self.data = data
        self.features = features
        self.Tree = self.generateTree(data, features)

    def calcSplitPoint(self, data, n):
        # sort data
        data = data[data[:, 0].argsort(), :]
        # initialization
        loss = np.zeros(n, dtype=float)
        aver = np.zeros([n, 2], dtype=float)
        # split point values
        point = np.zeros(n, dtype=float)

        point[0] = data[0, 0]
        # calc left average
        aver[0, 0] = 0
        for i in range(1, n, 1):
            point[i] = (data[i - 1, 0] + data[i, 0])/2
            aver[i, 0] = aver[i - 1, 0] + data[i - 1, 1]
        for i in range(1, n, 1):
            aver[i, 0] = aver[i, 0]/i
        
        # calc right average
        aver[n - 1, 1] = data[n - 1, 1]
        for i in range(n - 2, -1, -1):
            aver[i, 1] = aver[i + 1, 1] + data[i, 1]
        
        for i in range(n - 1, -1, -1):
            aver[i, 1] = aver[i, 1]/(n - i)
        
        # calc loss
        for i in range(n):
            loss[i] = np.sum((data[ :i, 1] - aver[i, 0])**2) + np.sum((data[i :, 1] - aver[i, 1])**2)
        
        # got index
        index = np.argmin(loss)
        # return
        return (loss[index], point[index])

    def getTree(self):
        return self.Tree
        
    def generateTree(self, data, features):
        # no feature return the average of data
        if(features.shape[0] == 0):
            return np.average(data[:, -1])
        else:
            k = features.shape[0]
            n = data.shape[0]
            Loss = np.zeros(k, dtype=float)
            Point = np.zeros(k, dtype=float)
            Aver = np.zeros([k, 2], dtype=float)
            # calc loss\point\aver for every feature
            for i in range(k):
                Loss[i], Point[i] = self.calcSplitPoint(data[:, [i, k]], n)
            # get the minimum loss's index
            index = np.argmin(Loss)
            feature_chosen = features[index]
            point_chosen = Point[index]
            # generate sub data
            data_left = data[data[:, index] < point_chosen, :]
            data_left = np.delete(data_left, index, axis=1)
            data_right = data[data[:, index] >= point_chosen, :]
            data_right = np.delete(data_right, index, axis=1)
            features = np.delete(features, index, axis=0)
            # generate sub Tree
            Tree = {}
            if(data_left.shape[0] == 0 or data_right.shape[0] == 0):
                Tree[(feature_chosen, 1, 0)] = np.average(data[:, -1])
            else:
                Tree[(feature_chosen, 0, point_chosen)] = self.generateTree(data_left, features)
                Tree[(feature_chosen, 1, point_chosen)] = self.generateTree(data_right, features)
            return Tree

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
        for k,v in tree.items():
            if(k[1] == 0 and data[k[0]] < k[2]):
                return self.predict_single(v, data)
            elif(k[1] == 1 and data[k[0]] >= k[2]):
                return self.predict_single(v, data)


    def cutBranch(self, data, alpha=1):
        self.alpha = alpha
        self.cutBranchSubTree(self.Tree, data)
        return self.Tree

    def cutBranchSubTree(self, Tree, data):
        subtree = 0
        if(type(Tree) is not dict):
            return (1, Tree)

        # cut subTree first
        for k,v in Tree.items():
            if(k[1] == 0):
                n, t = self.cutBranchSubTree(v, data[data[:,k[0]] < k[2], :])
            else:
                n, t = self.cutBranchSubTree(v, data[data[:,k[0]] >= k[2], :])
            Tree[k] = t
            subtree += n
        
        # if data is empty
        if(data.shape[0] == 0):
            return (subtree, Tree)
        # cut this Tree
        labels = np.zeros(data.shape[0])
        for i in range(labels.shape[0]):
            labels[i] = self.predict_single(Tree, data[i])
        Loss_Tt = np.sum((labels - data[:, -1])**2)
        average = np.average(data[:, -1])
        Loss_t = np.sum((data[:, -1] - average)**2)
        Loss = (Loss_t - Loss_Tt)/subtree
        if(Loss < self.alpha):
            return (1, average)
        else:
            return (subtree, Tree)

def main():
    DT = DecisionTree()
    fileName = "D:\\我的课件\\AI-pi\\2019年AI π竞赛队暑期招新初选赛题\\2019年AI π竞赛队暑期招新初选赛题\\数据.data"
    data = load_file(fileName)
    features = np.arange(0, 13, 1)
    np.random.shuffle(data)
    data_train = data[:450, :]
    data_test = data[450:, :]
    DT.train(data, features)
    
    # print(DT.getTree())
    print(np.sum((DT.self_predict(data_test) - data_test[:, -1])**2))
    print(DT.cutBranch(data_test), 0.1)
    print(np.sum((DT.self_predict(data_test) - data_test[:, -1])**2))

main()

