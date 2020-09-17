""" 高盛笔试第二题
@Title: Counting Pairs
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/17
"""

n = eval(input())
numbers = input().split()
numbers = [int(number) for number in numbers]
k = eval(input())
ans = []
numbers = sorted(numbers)
i = 1
while i < len(numbers):
    if numbers[i] == numbers[i - 1]:
        del(numbers[i])
    else:
        i += 1
for i, a in enumerate(numbers):
    for j, b in enumerate(numbers[i + 1:]):
        if a + k == b:
            ans.append((a, b))
        elif a + k < b:
            break
print(ans)
