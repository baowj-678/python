""" 高盛笔试第一题
@Title: Counting Pairs
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/17
"""


def first(item):
    return item[0]


weight = input().split()
weight = {value: str(i) for i, value in enumerate(weight)}
n = eval(input())
nums = []
for i in range(n):
    a = input()
    b = ''
    for i in range(len(a)):
        b += weight[a[i]]
    b = int(b)
    nums.append([b, a])
nums.sort(key=first)
print(nums)
nums = [num[1] for num in nums]
print(nums)
"""
测试用例：
3 5 4 6 2 7 9 8 0 1
3
990
332
32
"""
