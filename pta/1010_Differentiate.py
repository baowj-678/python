s = input().split(" ")
n = []
for i in range(len(s)):
    n.append(eval(s[i]))
s = []
for i in range(0, len(n) - 1, 2):
    differetiate = n[i + 1]*n[i]
    if differetiate != 0:
        s.append(differetiate)
        s.append(n[i + 1] - 1)

for i in range(len(s)):
    if i != len(s) - 1:
        print(s[i], end=' ')
    else:
        print(s[i], end='')
if len(s) == 0:
    print("0 0")
print("\\")