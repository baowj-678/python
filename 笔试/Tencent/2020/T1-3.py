""" 腾讯笔试第三题(第一轮)
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/9
"""
import numpy as np

g = np.zeros((205, 205), dtype=int)
while True:
    s = input()
    if s == '':
        break
    for i in range(len(s)):
        g[i, i] = 1
    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 1, len(s)):
            g[i, j] = min(g[i + 1, j], g[i, j - 1]) + 1
            for k in range(i, j + 1):
                if ord(s[i]) - ord(s[k]) == -1  or ord(s[i]) - ord(s[k]) == -2:
                    g[i, j] = min(g[i, j], g[i + 1, k - 1] + g[k + 1, j])
                elif ord(s[i]) - ord(s[j]) == -1  or ord(s[i]) - ord(s[j]) == -2:
                    g[i, j] = min(g[i, j], g[i, k - 1] + g[k + 1, j - 1])
    print(g[0, len(s) - 1])
    print(g)
    g[g > 0] = 0