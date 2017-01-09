a = []
b = input()
while b != '':
    a.append(b)
    b = input()
n = 0
for i in a:
    for q in a:
        if i == q:
            n += 1
print(n)
n = int(n) - len(a)
print(int(n)/2)
print(a)
        
