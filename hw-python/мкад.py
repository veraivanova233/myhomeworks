u = int(input())
t = int(input())
if u > 0:
    s = u*t - 109*(u*t//109)
else:
    u = abs(u)
    s = 109 - (u*t - 109*(u*t//109))
print(s)
