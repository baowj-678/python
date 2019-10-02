def out(n):
    if(n==0):
        print("ling",end='')
    elif(n==1):
        print("yi",end='')
    elif(n==2):
        print("er",end='')
    elif(n==3):
        print("shan",end='')
    elif(n==4):
        print("si",end='')
    elif(n==5):
        print("wu",end='')
    elif(n==6):
        print("liu",end='')
    elif(n==7):
        print("qi",end='')
    elif(n==8):
        print("ba",end='')
    elif(n==9):
        print("jiu",end='')


number = eval(input())
sum = 0
while(number!=0):
    sum += number%10
    number //= 10
n = []

while(sum!=0):
    n.append(sum%10)
    sum //= 10
if len(n)==0:
    out(0)
for i in range(len(n)):
    if(i!=len(n)-1):
        out(n[len(n)-i-1])
        print(" ",end='')
    else:
        out(n[len(n)-1-i])