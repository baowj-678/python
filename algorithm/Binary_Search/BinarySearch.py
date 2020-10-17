""" 二分法
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/10/17
"""


def binarySearch(left, right, delta, func, funcc):
    """ 二分法，要求(funcc(left) < 0, funcc(right) > 0)
    :left :左端点
    :right :右端点
    :delta :精度
    :func :原方程
    :funcc :原方程的导数
    """
    ###
    k = 1
    ###
    while abs(right - left) > delta:
        mid = (left + right)/2
        mid_val = funcc(mid)
        ###
        print("k:%d\tleft:%.2f\tright:%.2f\tmid:%.2f\tmid_val:%.2f" % (k, left, right, mid, mid_val))
        k += 1
        ###
        if mid_val < 0:
            left = mid
        elif mid_val == 0:
            return mid
        else:
            right = mid
    return (left + right) / 2


def func(x):
    return 2*x**3 - x - 1


def funcc(x):
    return 4*x**4 - 1


if __name__ == "__main__":
    left = -1
    right = 1
    delta = 0.001
    print(binarySearch(left, right, delta, func, funcc))
