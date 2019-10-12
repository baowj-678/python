n = eval(input())
a = [0]*3
b = [0]*3
for i in range(n):
    s = input().split()
    if s[0] == 'C':
        if s[1] == 'J':
            a[0] += 1
            b[2] += 1
        elif s[1] == 'B':
            a[2] += 1
            b[0] += 1
        elif s[1] == 'C':
            a[1] += 1
            b[1] += 1
    elif s[0] == 'J':
        if s[1] == 'B':
            a[0] += 1
            b[2] += 1
        elif s[1] == 'C':
            a[2] += 1
            b[0] += 1
        elif s[1] == 'J':
            a[1] += 1
            b[1] += 1
    elif s[0] == 'B':
        if s[1] == 'C':
            a[0] += 1
            b[2] += 1
        elif s[1] == 'J':
            a[2] += 1
            b[0] += 1
        elif s[1] == 'B':
            a[1] += 1
            b[1] += 1
print(a,b)


