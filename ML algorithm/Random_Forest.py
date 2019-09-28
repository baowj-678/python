from sklearn.datasets import load_iris
import numpy as np
data = load_iris()



def calcEntropy(data_x, data_y):
    set_y = set(data_y)
    entropy = 0
    for i in set_y:
        proportion = np.sum(data_y == i) / data_y.shape[0]
        entropy -= proportion * np.log2(proportion)
    return entropy

def getBestPoint(data_x, data_y):#data_x in some dimesion,x y is a row vector
    point = None
    min_entropy = 10000
    set_x = np.sort(np.array(list(set(data_x))))
    # print(set_x)
    for i in range(set_x.shape[0] - 1):
        # print(i,'\n\n\n\n\n')
        now_point = (set_x[i] + set_x[i + 1])/2
        p_left = np.sum(data_x < now_point) / data_x.shape[0]
        left_entropy = calcEntropy(data_x[data_x < now_point], data_y[data_x < now_point])
        # print(p_left, left_entropy)
        p_right = np.sum(data_x > now_point) / data_x.shape[0]
        right_entropy = calcEntropy(data_x[data_x > now_point], data_y[data_x > now_point])
        # print(p_right, right_entropy)
        now_entropy = p_left*left_entropy + p_right*right_entropy
        if min_entropy > now_entropy:
            min_entropy = now_entropy
            point = now_point
    return (point, now_entropy)

def decisionTree(data_x, data_y):

    return 1

def main():
    data_x = np.transpose(np.array(data.data))
    data_y = np.array(data.target)
    print(data_x.shape, data_y.shape)
    print(calcEntropy(data_x, data_y))
    print(getBestPoint(data_x[0,:], data_y))

main()