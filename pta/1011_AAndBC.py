n = eval(input())
for i in range(n):
    s = input()
    s = s.split(" ")
    for j in range(len(s)):
        s[j] = eval(s[j])
    if s[0] + s[1] > s[2]:
        print("Case #" + str(i + 1) + ": true")
    else:
        print("Case #" + str(i + 1) + ": false")
    
