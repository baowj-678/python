s1 = input()
s2 = input()
s3 = input()
s4 = input()
day = [None]*2
time = None
for i in range(len(s1)):
    if(s1[i] == s2[i] and ('A' <= s1[i] <='Z')):
        day[0] = s1[i]
        break
for i in range(i + 1, len(s1)):
    if(s1[i] == s2[i] and ('A' <= s1[i] <='N' or '0' <= s1[i] <= '9')):
        day[1] = s1[i]
        break

for i in range(len(s3)):
    if s3[i] == s4[i] and ('A' <= s3[i] <='Z' or 'a' <= s3[i] <= 'z'):
        time = i
        break

if '0' <= day[1] <= '9':
    day[1] = ord(day[1]) - ord('0')
elif 'A' <= day[1] <= 'Z':
    day[1] = ord(day[1]) - ord('A') + 10

if day[0] == 'A':
    print("MON", end=' ')
elif day[0] == 'B':
    print("TUE", end=' ')
elif day[0] == 'C':
    print("WED", end=' ')
elif day[0] == 'D':
    print("THU", end =' ')
elif day[0] == 'E':
    print("FRI", end=' ')
elif day[0] == 'F':
    print("SAT", end=' ')
elif day[0] == 'G':
    print("SUN", end=' ')

if day[1] < 10:
    print(0,end='')
    print(day[1], end=':')
else:
    print(day[1], end=':')

if time < 10:
    print(0,end='')
    print(time, end='')
else:
    print(time, end='')
