""" 腾讯笔试第二题(第一轮)
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/7
"""

"""
解析
n = Cn1*C11 + Cn2*C21 + ... + Cnn*Cn1
  = n*x^(n-1)
"""

Max = int(1e9 + 7)
Base = 2
while True:
    n = eval(input())
    if n == 0:
        break
    tmp = n - 1
    base = Base
    ans = 1
    while tmp != 0:
        if tmp & 1 > 0:
            ans = ans * base % Max
        base = base * base % Max
        tmp = tmp >> 1
    print((n * ans) % Max)

"""
测试用例：
2
结果：
4
"""
