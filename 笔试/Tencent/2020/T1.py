""" 腾讯笔试第一题
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/7
"""

T = int(input())
i = 0
for i in range(T):
    n = eval(input())
    data = [int(x) for x in input().split()]
    # 左 -> 右，递减序列
    length1 = [1]*n
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if data[i] < data[j]:
                length1[i] = max(length1[i], length1[j] + 1)
    # 右 -> 左，递增序列
    length2 = [1]*n
    for i in range(n-1, -1, -1):
        for j in range(i+1, n, 1):
            if data[i] < data[j]:
                length2[i] = max(length2[i], length2[j] + 1)
    max_ = 0
    for i in range(n):
        for j in range(i+1, n):
            if data[i] == data[j]:
                if min(length1[i], length2[j])*2 > max_:
                    max_ = min(length1[i], length2[j])*2
    print(max_)

"""
用例：
3
9
5 4 3 2 1 2 3 4 5
5
1 2 3 4 5
14
87 70 17 12 14 86 61 51 12 90 69 89 4 65
"""
