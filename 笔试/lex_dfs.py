g_from = [0, 3, 1, 0, 1, 2]
g_to = [3, 4, 2, 1, 3, 4]
r = [0, 3, 2, 1]
v = [1, 4, 4, 2]
g_from_to = {}
m = 0
for x, y in zip(g_from, g_to):
    m = max(m, x, y)
    if x in g_from_to:
        g_from_to[x].append(y)
    else:
        g_from_to[x] = [y]
    if y in g_from_to:
        g_from_to[y].append(x)
    else:
        g_from_to[y] = [x]
for key in g_from_to.keys():
    g_from_to[key] = sorted(g_from_to[key])
for from_, to_ in zip(r, v):
    is_visited = [0]*(m+1)
    path = [from_]
    is_visited[from_] = 1
    while path[-1] != to_ and len(path) < (m + 1):
        next_ = g_from_to[path[-1]]
        for i in next_:
            if is_visited[i] == 0:
                is_visited[i] = 1
                path.append(i)
                break
    print(path)
"""
5 6
0 3
3 4
1 2
0 1
1 3
2 4
3 4
"""
