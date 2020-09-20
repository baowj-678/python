""" 腾讯笔试第二题
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/7
"""
import math

input_ = input().split()
L = int(input_[0])
d = int(input_[1])
print(math.log(L/d) + 1)

"""
测试用例
2 1

结果
1.6931471805599454
"""
