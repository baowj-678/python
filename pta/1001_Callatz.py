a = eval(input())
n = 0
while(a != 1):
    if(a%2 == 0):
        a = a / 2
    else:
        a = (a*3 + 1) / 2
    n = n + 1
 
print(n)