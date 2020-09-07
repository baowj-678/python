""" 腾讯2020秋季笔试第五题
@Key: Dijkstra算法
@Author: Bao Wenjie
@Eamil: bwj_678@qq.com
@Date: 2020/9/7
"""

# 输入
input_ = input().split()
n = int(input_[0])
m = int(input_[1])
T = int(input_[2])
i = 0
graph = [[] for i in range(n + 1)]
for i in range(m):
    input_ = input().split()
    x = int(input_[0])
    y = int(input_[1])
    d = int(input_[2])
    graph[x].append([y, d])
INF = 2000000
distance = 0
min_d = [INF]*(n + 1)
is_min = [0]*(n + 1)
min_d[1] = 0
u = 1
while True:
    # 更新u邻接结点
    for yd in graph[u]:
        if yd[1] + min_d[u] < min_d[yd[0]]:
            min_d[yd[0]] = yd[1] + min_d[u]
    # 更新u
    min_ = INF
    min_index = -1
    for i in range(1, n + 1):
        if is_min[i] == 0 and min_ > min_d[i]:
            min_ = min_d[i]
            min_index = i
    u = min_index
    is_min[min_index] = 1
    if is_min[n] == 1:
        distance += min_d[n]
        break
min_d = [INF]*(n + 1)
is_min = [0]*(n + 1)
min_d[n] = 0
u = n
while True:
    # 更新u邻接结点
    for yd in graph[u]:
        if yd[1] + min_d[u] < min_d[yd[0]]:
            min_d[yd[0]] = yd[1] + min_d[u]
    # 更新u
    min_ = INF
    min_index = -1
    for i in range(1, n + 1):
        if is_min[i] == 0 and min_ > min_d[i]:
            min_ = min_d[i]
            min_index = i
    u = min_index
    is_min[min_index] = 1
    if is_min[1] == 1:
        distance += min_d[1]
        break
print(T*distance)

"""
5 5 3
1 2 1
2 3 1
3 5 1
5 1 1
4 5 1
"""