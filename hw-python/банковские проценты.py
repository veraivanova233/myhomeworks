# банковские проценты
x = int(input())
p = int(input())
y = int(input())
a = 0
while float(x) < float(y):
    a += 1
    x += float(p)*float(x)/100
    round (x, 2)
print (a)
