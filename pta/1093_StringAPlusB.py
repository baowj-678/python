def big(s):
    while(len(s) < 4):
        s += '0'
    s = sorted(s, reverse=True)
    number = ''
    for i in range(len(s)):
        number += s[i]
    return eval(number)

def small(s):
    s = sorted(s)
    number = ''
    for i in range(len(s)):
        if s[i] == '0':
            continue
        number += s[i]
    if number == '':
        return 0
    return eval(number)

s = input()
a = big(s)
b = small(s)
while a != b:
    print(a, end=' - ')
    s = str(a)
    s = sorted(s)
    for i in range(len(s)):
        print(s[i], end='')
    print(' = ', end='')
    c = a - b
    s = str(c)
    for i in range(4 - len(s)):
        print('0', end='')
    a = big(str(c))
    b = small(str(c))
    print(s)
    if c == 6174:
        break
if a == b:
    out = ''
    s = str(a)
    for i in range(4 - len(s)):
        out += '0'
    out += s
    print(out, '-', out, '= 0000', end='')