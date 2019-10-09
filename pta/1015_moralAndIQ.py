def getLast(element):
    return element[-1]

s = input().split()
N = eval(s[0])
L = eval(s[1])
H = eval(s[2])
data =[]
for i in range(N):
    s = input().split()
    piece = []
    piece.append(s[0])
    piece.append(eval(s[1]))
    piece.append(eval(s[2]))
    if piece[2] < L and piece[1] < L:
        continue
    piece.append(piece[2]+piece[1])
    score = 0
    if piece[1] >= H:
        if piece[2] >= H:
            score = 4
        else:
            score = 3
    else:
        if piece[2] >= H:
            score = 2
        else:
            score = 1
    piece.append(score)
    data.append(piece)

data.sort(key=getLast,reverse=True)
print(data)