""" 腾讯笔试第五题(第一轮)
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/16
@method: 单源最短路问题
"""
import queue


INF = 999999
input_ = input().split()
n = eval(input_[0])
m = eval(input_[1])
k = eval(input_[2])
graph = [list() for i in range(n + 1)]
for i in range(m):
    xy = input().split()
    u = int(xy[0])
    v = int(xy[1])
    value = int(xy[2])
    graph[u].append((v, value))
for i in range(k):
    xy = input().split()
    u = int(xy[0])
    v = int(xy[1])
    graph[u].append((v, 0))
# SPFA
distance = [INF] * (n + 1)
distance[1] = 0
Q = queue.Queue()
Q.put(1)
while Q.empty() is False:
    u = Q.get()
    for v, value in graph[u]:
        value_ = distance[u] + value
        if value_ < distance[v]:
            distance[v] = value_
            Q.put(v)
print(distance[n])

"""
测试用例：
5 3 2
1 2 1
2 3 1
3 4 1
4 5
1 2
结果：
2
"""
