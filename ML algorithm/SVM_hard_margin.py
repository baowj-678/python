import numpy as np
from matplotlib import pyplot as plt

class data:
    def __init__(self, dataSets, C):
        #Xi中i的数目，为行向量
        self.n = dataSets.shape[0]
        #X的属性数目，为行向量
        self.m = dataSets.shape[1] - 1
        #X，行向量
        self.X = dataSets[:, :self.m]
        #Y，列向量
        self.Y = np.array(dataSets[:, self.m], dtype=np.int32)[:, np.newaxis]
        #b
        self.b = 0
        #alpha
        self.alpha = np.zeros([self.n, 1])
        #C
        self.C = C

#计算f(x)
def calcFx(alpha, Y, X, x, b):
    fx = alpha * Y * (np.multiply(X, np.transpose(x)))
    fx = np.sum(fx) + b
    return fx

def calck(x1, x2):
    x2 = x2[:, np.newaxis]
    return np.dot(x1, x2)

#返回alpha_new未修改dataInfo
def clipAlpha(data, alphai_new, i, j):
    L = None
    H = None
    alpha_new = None
    if data.Y[i, 0] == data.Y[j, 0]:
        L = max(0, data.alpha[i, 0] + data.alpha[j, 0] - data.C)
        H = min(data.C, data.alpha[i, 0] + data.alpha[j, 0])
    else:
        L = max(0, data.alpha[i, 0] - data.alpha[j, 0])
        H = min(data.C, data.C + data.alpha[i, 0] - data.alpha[j, 0])

    if alphai_new > H:
        alpha_new = H
    elif L <= alphai_new <= H:
        alpha_new = alphai_new
    else:
        alpha_new = L
    return alpha_new

def hard_margin_SVM(dataSets, C):
    dataInfo = data(dataSets, C)
    #
    for time in range(100):
        for i in range(dataInfo.n):
            #计算f(xi)
            fxi = calcFx(dataInfo.alpha, dataInfo.Y, dataInfo.X, np.transpose(dataInfo.X[i,:]), dataInfo.b)
            print("fxi:",fxi)
            if(dataInfo.alpha[i] == 0 and dataInfo.Y[i] * fxi >= 1):
                continue
            if(dataInfo.alpha[i, 0] == dataInfo.C and dataInfo.Y[i, 0] * fxi <= 1):
                continue
            if(0 < dataInfo.alpha[i, 0] < dataInfo.C and dataInfo.Y[i, 0] * fxi == 1):
                continue
            Ei = fxi - dataInfo.Y[i]
            dalt = 0
            Ej = 0
            j = 0
            for k in range(dataInfo.n):
                fxk = calcFx(dataInfo.alpha, dataInfo.Y, dataInfo.X, np.transpose(dataInfo.X[k, :]), dataInfo.b)
                Ek = fxk - dataInfo.Y[k]
                if abs(Ei -Ek) > dalt:
                    j = k
                    Ej = Ek
                    dalt = abs(Ei - Ej)
            yeta = calck(dataInfo.X[i, :], dataInfo.X[i, :]) + calck(dataInfo.X[j, :], dataInfo.X[j, :]) - 2 * calck(dataInfo.X[i, :], dataInfo.X[j, :])
            alphai_new = dataInfo.alpha[i] + (dataInfo.Y[i] * (Ej - Ei)) / yeta
            alphai_new = clipAlpha(dataInfo, alphai_new, i, j)
            alphaj_new = dataInfo.alpha[j, 0] + dataInfo.Y[i, 0] * dataInfo.Y[j, 0] * (dataInfo.alpha[i, 0] - alphai_new)

            bi = - Ei - dataInfo.Y[i, 0] * (alphai_new - dataInfo.alpha[i, 0]) * calck(dataInfo.X[i, :], dataInfo.X[i, :])\
                - dataInfo.Y[j, 0] * (alphaj_new - dataInfo.alpha[j, 0]) * calck(dataInfo.X[i, :], dataInfo.X[j, :]) + dataInfo.b
            bj = - Ej - dataInfo.Y[i, 0] * (alphai_new - dataInfo.alpha[i, 0]) * calck(dataInfo.X[j, :], dataInfo.X[i, :])\
                - dataInfo.Y[j, 0] * (alphaj_new - dataInfo.alpha[j, 0]) * calck(dataInfo.X[j, :], dataInfo.X[j, :]) + dataInfo.b
            if 0 < alphai_new < dataInfo.C:
                dataInfo.b = bi
            elif 0 < alphaj_new < dataInfo.C:
                dataInfo.b = bj
            else:
                dataInfo.b = (bi + bj) / 2
            print(dataInfo.b)
            # if time<90:
            #     dataInfo.b = 5
            dataInfo.alpha[i, 0] = alphai_new
            dataInfo.alpha[j, 0] = alphaj_new
    print(dataInfo.alpha)
    w = np.sum((dataInfo.alpha * dataInfo.Y * dataInfo.X), axis=0)
    w = w[:, np.newaxis]
    return w,dataInfo.b

def main():
    data = np.array([
         [1.2, 2.3, -1]
        ,[0.9, 1.3, -1]
        ,[2.6, 1.5, -1]
        ,[5, 3, 1]
        ,[4.5, 4.5, 1]
        ,[5.7, 4, 1]
        ,[3.4, 3.9, 1]
    ])
    plt.scatter(data[:3, 0],data[:3,1])
    plt.scatter(data[3:, 0],data[3:,1])
    w,b = hard_margin_SVM(data, 1)
    print(w,b)
    x = np.linspace(0,6,50)
    y = (-b - w[0]*x)/w[1]
    plt.plot(x,y)
    plt.show()
main()  
