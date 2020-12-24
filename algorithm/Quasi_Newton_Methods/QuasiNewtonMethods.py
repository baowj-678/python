""" 拟牛顿法
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/10/20
"""
import numpy as np

def DFP(X_0, func, func_g, epsilon):
    """ DFP算法
    """
    n = X_0.shape[0]
    H_t = np.eye(X_0.shape[0])
    g_t = func_g(X_0)
    X_t = X_0
    while np.linalg.norm(g_t) > epsilon:
        k = 0
        p_t = -np.dot(H_t, g_t)

        def func_(t):
            X_ = X_t + t*p_t
            return func(X_)
        # 一维搜索
        t_k = golden_ratio(0, 1, 1e-9, func_)
        X_t_ += t_k * p_t
        g_t_ = func_g(X_t_)
        if np.linalg.norm(g_t_) < epsilon:
            break
        k += 1
        if k != n:
            

def golden_ratio(left, right, delta, func):
    """ 黄金分割法实现
    :left: 搜索区间左端点
    :right: 搜索区间右端点
    :delta: 精度
    :func: 函数
    """
    ###
    k = 1
    ###
    right_ = left + 0.618*(right - left)
    left_ = left + 0.382*(right - left)
    right_val = func(right_)
    left_val = func(left_)
    while (right - left) > delta:
        ###
        print('k:%.3f\tak:%.3f\tbk:%.3f\tx1:%.3f\tx2:%.3f\tfx1:%.3f\tfx2:%.3f' % (k, left, right, left_, right_, left_val, right_val))
        k += 1
        ###
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
