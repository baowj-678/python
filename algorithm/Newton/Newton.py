""" 牛顿迭代法
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/10/19
"""
import numpy as np


def Newton(X0, delta, func, func_g, func_G):
    """ 牛顿迭代法
    :X0 :迭代初值
    :delta :精度
    :func :函数
    :func_g : 一阶导函数
    :func_G :二阶导函数
    """
    k = 0
    g_k = func_g(X0)
    if np.linalg.norm(g_k) > delta:
        G_k = func_G(X0)
        G_k_ = np.linalg.inv(G_k)
        p_k = -np.dot(G_k_, g_k)
        X0 = X0 + p_k
        ###
        print('k=', k)
        print('g_k\n', g_k)
        print('G_k\n', G_k)
        print('G_k_\n', G_k_)
        print('p_k\n', p_k)
        print('X0\n', X0)
        print()
        ###
        k += 1
    return X0


def func(X0):
    return 0


def func_g(X0):
    g = np.copy(X0)
    g[0] = 2*g[0]
    g[1] = 8*g[1]
    return g


def func_G(X0):
    g = np.zeros([2, 2])
    g[0, 0] = 2
    g[1, 1] = 8
    return g


if __name__ == "__main__":
    X0 = np.ones([2, 1])
    delta = 0.01
    print(Newton(X0, delta, func, func_g, func_G))
