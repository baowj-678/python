import numpy as np

class NearestNeighbor:
    def __init__(self):
        pass

    def tarin(self, X, y):
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        num_test = X.shape[0]
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)
        
        for i in range(num_test):
            distances = np.sum(np.abs(self.Xtr - X[i, :]), axis=1)
            print(distances)
            min_index = np.argmin(distances)
            Ypred[i] = self.ytr[min_index]

        return Ypred


X = [
    [56, 32, 10, 18], 
    [90, 23, 128, 133],
    [24, 26, 178, 200],
    [2, 0, 255, 220]
    ]
y = [10, 20, 24, 17]
    # [8, 10, 89, 100],
    # [12, 16, 178, 170],
    # [4, 32, 233, 112]
X = np.array(X)
y = np.array(y)
net = NearestNeighbor()
net.tarin(X, y)
print(net.predict(X))