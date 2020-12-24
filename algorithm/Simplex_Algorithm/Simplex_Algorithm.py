""" 单纯形法
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/10/6
"""
import numpy as np


class SimplexAlgorithm():
    def __init__(self):
        """ 初始化
        """
        pass

    def solve(self, A, b, Z, X0):
        """ 求解m个方程n个变量的线性规划问题 AX = b
        :param A: numpy(m, n + 1): 增广矩阵[Ab]
        :param X0: numpy(m, 1): 初始基可行解
        :param Z: numpy(1, n): 最小化目标函数的参数z = ZX
        """
        self.n = A.shape[1] - 1
        self.m = A.shape[0]
        self.A = A
        self.Z = Z
        self.X = np.zeros(self.m, 3)  # (m, 3)
        self.X[:, 1] = X0
        self.X[:, 2] = self.A[:, -1]
        self.X[:, 0] = self.Z[X0]
        # 获取主元
        n_index, m_index = self.getPivot()
        # 利用行列式变换，将主元变成1
        self.makePivotOne(n_index, m_index)
        # 更换基变量
        self.X[m_index, 1] = n_index
        self.X[m_index, 0] = self.Z[n_index]
        self.X[m_index, 2] = self.A[n_index, -1]

    def getPivot(self):
        """ 获取主元
        """
        x = self.X[:, 2].transpose()  # (1, m)
        n_values = self.Z - np.dot(x, self.A[:, :-1])
        n_values[self.X[:, 1]] = 0
        n_index = np.argmin(n_values)
        m_values = x / self.A[:, n_index]
        m_index = np.argmax(m_values)
        return (n_index, m_index)

    def makePivotOne(self, n_index, m_index):
        """ 使主元变成系数为1
        """
        self.A[m_index, :] = self.A[m_index, :] / self.A[m_index, n_index]
        for i in range(self.m):
            if i == m_index:
                continue
            else:
                self.A[i, :] = self.A[i, :] - self.A[m_index, :] * self.A[i, n_index]
        return self.A
