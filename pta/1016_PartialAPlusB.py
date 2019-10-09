s = input().split()
a = s[0]
b = s[2]
da = s[1]
db = s[3]
a_n = a.count(da)
b_n = b.count(db)
sum = 0
if a_n != 0:
    sum += eval(da*a_n)
if b_n != 0:
    sum += eval(db*b_n)
print(sum)