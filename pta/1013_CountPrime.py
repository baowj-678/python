s = input().split()
num = []
for i in range(len(s)):
    num.append(eval(s[i]) - 1)

prime = [0]*(num[1] + 1)
prime[0] = 2
if num[1] >= 1:
    i = 2
    j = 3
    prime[1] = 3
else:
    i = 1
    j = 1
while prime[num[1]] == 0:
    j += 2
    if j%3 == 0:
        continue
    is_prime = True
    for k in range(i):
        if prime[k] > j**0.5:
            break
        elif j%prime[k] == 0:
            is_prime = False
            break
    if is_prime:
        prime[i] = j
        i += 1

for i in range(num[0], num[1], 1):
    if (i - num[0] + 1)%10 == 0:
        print(prime[i])
    else:
        print(prime[i],end=' ')
print(prime[num[1]],end='')