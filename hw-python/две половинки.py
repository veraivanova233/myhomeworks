a = input()
b = a[:len(a)//2+(len(a)%2)]
c = a[len(a)//2+(len(a)%2):]
print(c+b)
