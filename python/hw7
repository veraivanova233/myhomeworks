import random
A = {}
f = open('файл.csv', 'r', encoding = 'utf-8')
f = f.read()
f = f.split(';')
p = open('файл1.csv', 'r', encoding = 'utf-8')
p = p.read()
p = p.split(';')
count = 0
for i in f:
    A[i] = p[count]
    count += 1
keys = []
for i in A.keys():
    keys.append(i)
x = random.choice(keys)
count = 0
print(x + ' ' + len(A.get(x))*'.')
n = input()
while A[x] != n:
    print('Not exactly, try it again')
    n = input()
print('You are right. Congratulations!')
