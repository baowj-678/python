import  torchvision,torch
import  torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
import numpy as np

#加载数据
train = torchvision.datasets.MNIST(root='./mnist/',train=True, transform=transforms.ToTensor())
#将数据变成numpy
data = train.data.numpy()
target = train.targets.numpy()
print(target)

class Knn_For_Minist():
    def __init__(self):
        pass
    def train(self, X, Y):
        self.X = X
        self.Y = Y
    def predict(self, test_X):
        #预测数据的个数
        num_test = test_X.shape[0]
        #预测结果保存位置
        test_Y = np.zeros(num_test, dtype=self.Y.dtype)
        for i in range(num_test):
            distances = np.sum(np.sum(np.abs(self.X - test_X[i, :]), axis=2),axis=1)
            min_index = np.argmin(distances)
            # print(min_index)
            test_Y[i] = self.Y[min_index]
        return test_Y

    def accuracy(self, target, test_Y):
        # print(target, test_Y)
        sum = test_Y.shape[0]
        correct = np.sum(target == test_Y)
        return correct/sum

    def train_meam(self, X, Y):
        self.data = {}
        for i in range(10):
            self.data[i] = X[Y==i, :]
        self.target = Y
        
    def predict_mean(self, test_X):
        #预测数据的个数
        num_test = test_X.shape[0]
        #预测结果保存位置
        test_Y = np.zeros(num_test, dtype=self.data[0].dtype)
        for i in range(num_test):
            distances = np.zeros(10)
            for j in range(10):
                distances[j] = np.mean(np.sum(np.sum(np.abs(self.data[j] - test_X[i, :]), axis=2),axis=1))
            min_index = np.argmin(distances)
            # print(min_index)
            test_Y[i] = self.target[min_index]
        return test_Y
        
        
knn = Knn_For_Minist()
# knn.train(data[0:100, :], target[0:100])
# ans = knn.predict(data[100:200, :])
# print(knn.accuracy(target[100:200], ans))
# print(data[target == 1, :])
knn.train_meam(data[0:100, :], target[0:100])
knn.predict_mean(data[100:200])


