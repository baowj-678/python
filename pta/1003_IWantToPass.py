def check(temp):
    is_yes = True
    a = False
    p = False
    t = False
    for i in range(len(temp)):
        if(temp[i]=='P'):
            p = True
        elif(temp[i]=='T'):
            t = True
        elif(temp[i]=='A'):
            a = True
        else:
            is_yes = False
            break
    if(is_yes and a and p and t):
        print("YES")
    else:
        print("NO")

n = eval(input())
s = []
for i in range(n):
    temp = input()
    s.append(temp)
for i in range(n):
    check(s[i])