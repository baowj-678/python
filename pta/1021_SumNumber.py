import numpy as np

s = np.array(list(input()))
num = [0]*10
for i in range(10):
    num[i] = sum(s == str(i))

for i in range(10):
    if num[i]!=0:
        print(str(i) + ':',end='')
        print(num[i])
