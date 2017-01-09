N = int(input())
M = int(input())
x = int(input())
y = int(input())
if x>(N-x) and y>(M-y):
    if (N-x)>(M-y):
        print(M-y)
    else:
        print (N-x)
elif x<(N-x) and y<(M-y):
    if x>y:
        print(y)
    else:
        print(x)
elif x>(N-x) and y<(M-y):
    if (N-x)>y:
        print(y)
    else:
        print(N-x)
else:
    # x<(N-x) and y>(M-y)
    if x>(M-y):
        print(M-y)
    else:
        print(x)
