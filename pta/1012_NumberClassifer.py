s = input().split(" ")
A1 = 0
A2 = 0
A3 = 0
A4 = 0
A5 = 0
A2_sign = 1
is_A2 = True
A4_num = 0
for i in range(1, len(s), 1):
    s[i] = eval(s[i])
    if(s[i]%5 == 0 and s[i]%2 == 0):
        A1 += s[i]
    elif(s[i]%5 == 1):
        A2 += s[i]*A2_sign
        A2_sign *= -1
        is_A2 = False
    elif(s[i]%5 == 2):
        A3 += 1
    elif(s[i]%5 == 3):
        A4 += s[i]
        A4_num += 1
    elif(s[i]%5 == 4 and s[i] > A5):
        A5 = s[i]
if A4_num == 0:
    A4 = 0
else:
    A4 /= (A4_num)
if(A1 == 0):
    print("N",end=" ")
else:
    print(A1,end=" ")
if(is_A2):
    print("N",end=" ")
else:
    print(A2,end=" ")
if(A3 == 0):
    print("N",end=" ")
else:
    print(A3,end=" ")

if(A4 == 0):
    print("N",end=" ")
else:
    print('%.1f'%A4,end=" ")
if(A5 == 0):
    print("N",end="")
else:
    print(A5,end="")

