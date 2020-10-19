""" 正定二次函数最速下降法
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/10/19
"""
import numpy as np


def gradientDescent(X0: np.ndarray, delta: int, G: np.ndarray, b: np.ndarray, c):
    """ 正定二次函数最速下降法 1/2xGx + xb + c
    :X0 :初始值,列向量
    :delta :终止限
    :G :
    :b :
    """
    def g_(X):
        return np.dot(G, X) + b

    def f(X):
        return 0.5*np.dot(X.transpose(), np.dot(G, X)) + np.dot(b.transpose(), X) + c

    X_new = X0
    X_old = np.zeros_like(X0)
    while abs(f(X_new) - f(X_old)) > delta:
        print('x:', X_new)
        g = g_(X_new)
        X_old = np.copy(X_new)
        X_new -= np.dot(X_old.transpose(), X_old)/np.dot(X_old.transpose(), np.dot(G, X_old))*g
    return X_new


if __name__ == "__main__":
    X0 = np.array([[1], [1]], dtype=float)
    delta = 1e-9
    G = np.array([[4, 0], [0, 2]])
    b = np.array([[0], [0]])
    c = 0
    print(gradientDescent(X0, delta, G, b, c))
