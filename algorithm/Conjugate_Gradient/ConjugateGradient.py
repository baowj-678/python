""" 共轭梯度法
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/10/19
"""
import numpy as np


def FR(X_0, p_0, delta, func, func_g):
    """ 共轭梯度法
    :X0 : 初始值
    :p0 :初始下降方向
    :func :原函数
    :func_g :导数
    """
    g_k = func_g(X_0)
    p_k = -g_k
    X_k = X_0
    while np.linalg.norm(g_k) > delta:
        def func_(t):
            X_ = X_k + t*p_k
            return func(X_)
        # 一维线性搜索
        t_k = golden_ratio(0, 1, 1e-9, func_)
        X_k += t_k*p_k
        g_k_ = func_g(X_k)
        if np.linalg.norm(g_k_) < delta:
            break
        beta_k = np.linalg.norm(g_k_)**2 / np.linalg.norm(g_k)**2
        g_k = g_k_
        print('X_k', X_k)
        print('t_k', t_k)
        print('p_k', p_k)
        print('g_k', g_k)
        p_k = -g_k + beta_k*p_k
    return X_k


def golden_ratio(left, right, delta, func):
    """ 黄金分割法实现
    :left: 搜索区间左端点
    :right: 搜索区间右端点
    :delta: 精度
    :func: 函数
    """
    right_ = left + 0.618*(right - left)
    left_ = left + 0.382*(right - left)
    right_val = func(right_)
    left_val = func(left_)
    while (right - left) > delta:
        if right_val < left_val:
            left = left_
            left_ = right_
            right_ = left + 0.618*(right - left)
            left_val = right_val
            right_val = func(right_)
        elif right_val == left_val:
            left = left_
            right = right_
            right_ = left + 0.618*(right - left)
            left_ = left + 0.382*(right - left)
            left_val = func(left_)
            right_val = func(right_)
        else:
            right = right_
            right_ = left_
            left_ = left + 0.382*(right - left)
            right_val = left_val
            left_val = func(left_)
    return (right + left)/2


def func_g(X):
    g = np.zeros_like(X, dtype=np.float)
    g[0] = 3*X[0] - X[1] - 2
    g[1] = X[1] - X[0]
    return g


def func(X):
    return 3/2*X[0]**2 + 1/2*X[1]**2 - 2*X[0] - X[0]*X[1]


if __name__ == "__main__":
    X0 = np.array([0, 0], dtype=np.float)[:, np.newaxis]
    delta = 1e-6
    print(FR(X0, func_g(X0), delta, func, func_g))
