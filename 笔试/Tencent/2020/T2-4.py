""" 腾讯2020秋季笔试第四题
@Author: Bao Wenjie
@Eamil: bwj_678@qq.com
@Date: 2020/9/7
"""

T = eval(input())
i = 0
for i in range(T):
    n = eval(input())
    j = 0
    nums = []
    for j in range(n):
        num = [int(a) for a in input().split()]
        num = sorted(num)
        nums.append("".join(map(str, num)))
    sorted(nums)
    isYes = False
    for j in range(1, n):
        if nums[j] == nums[j - 1]:
            print('YES')
            isYes = True
            break
    if isYes is False:
        print('NO')


"""
测试用例：
2
2
1 2 3 4 5 6
2 3 4 5 6 1
3
1 2 3 4 5 6
8 5 4 1 2 3
2 3 4 5 6 7
"""
