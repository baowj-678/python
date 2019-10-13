n = eval(input())
a = [0]*3
a0 = [0]*3
b = [0]*3
b0 = [0]*3
# b c j
for i in range(n):
    s = input().split()
    if s[0] == 'C':
        if s[1] == 'J':
            a0[1] += 1
            a[0] += 1
            b[2] += 1
        elif s[1] == 'B':
            b0[0] += 1
            a[2] += 1
            b[0] += 1
        elif s[1] == 'C':
            a[1] += 1
            b[1] += 1
    elif s[0] == 'J':
        if s[1] == 'B':
            a0[2] += 1
            a[0] += 1
            b[2] += 1
        elif s[1] == 'C':
            b0[1] += 1
            a[2] += 1
            b[0] += 1
        elif s[1] == 'J':
            a[1] += 1
            b[1] += 1
    elif s[0] == 'B':
        if s[1] == 'C':
            a0[0] += 1
            a[0] += 1
            b[2] += 1
        elif s[1] == 'J':
            b0[2] += 1
            a[2] += 1
            b[0] += 1
        elif s[1] == 'B':
            a[1] += 1
            b[1] += 1
print(a[0], a[1], a[2])
print(b[0], b[1], b[2])
a = a0.index(max(a0))
b = b0.index(max(b0))
if(a == 0):
    print('B', end=' ')
elif(a == 1):
    print('C', end=' ')
elif(a == 2):
    print('J', end=' ')

if(b == 0):
    print('B', end='')
elif(b == 1):
    print('C', end='')
elif(b == 2):
    print('J', end='')

