h = int(input())
a = int(input())
b = int(input())
p = 0
f = 0
while p < h:
    f = p
    p += a
    if p >= h:
        break
    p -= b
print(f+1)
    
