""" 腾讯笔试第一题(第一轮)
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/7
"""

T = eval(input())
for i in range(T):
    input_ = input().split()
    A, B, C, D = int(input_[0]), int(input_[1]), int(input_[2]), int(input_[3])
    print(abs(A*D**3/3 + (D**2)/2 + B*D - A*C**3/3 - (C**2)/2 - B*C))


"""
测试用例：
1
2 3 1 2
结果:
9.166667
"""
