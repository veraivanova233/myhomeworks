a = int(input())
q = 0
while a != 0:
    if a > q:
        q = a
        a = int(input())
    else:
        a = int(input())
print(q)
        
