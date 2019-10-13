s = input().split(' ')
total = s[0].split('.')
for i in range(len(total)):
    total[i] = eval(total[i])
pay = s[1].split('.')
for i in range(len(pay)):
    pay[i] = eval(pay[i])

is_minus = False
if total[0]*29*17 + total[1]*29 + total[2] > pay[0]*17*29 + pay[1]*29 + pay[2]:
    temp = total
    total = pay
    pay = temp
    is_minus = True

change = [0]*3
change[2] = pay[2] - total[2]
if change[2] < 0:
    change[2] += 29
    pay[1] -= 1
change[1] = pay[1] - total[1]
if change[1] < 0:
    change[1] += 17
    pay[0] -= 1
change[0] = pay[0] - total[0]
if is_minus:
    print('-', end='')
print(change[0], end='.')
print(change[1], end='.')
print(change[2], end='')