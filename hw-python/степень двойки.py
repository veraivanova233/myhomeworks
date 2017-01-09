N = int(input())
if N == 0:
    print('no numbers')
while int(N)%2 != 0:
    N = int(N)-1
print(N) # сама степень (2 в степени)
a = int(N)/2 # все степени до N
p = 1 # показатель степени
if a == 0:
    print('0')
if a == 1:
    print ('1')
while (a != 1) and (a != 0):
    a = int(a)/2
    p += 1
    print (p)
