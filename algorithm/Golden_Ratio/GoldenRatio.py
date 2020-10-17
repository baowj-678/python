""" 黄金分割法实现
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/10/17
"""


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


def func(x):
    return 2*x**2 - x - 1


if __name__ == "__main__":
    a = -1
    b = 1
    delta = 0.16
    print(golden_ratio(a, b, delta, func))
