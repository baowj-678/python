s = input()
words = s.split(' ')
for i in range(len(words)-1, 0, -1):
    print(words[i], end=' ')
print(words[0],end='')
print("\\")