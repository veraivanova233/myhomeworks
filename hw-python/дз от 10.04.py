import os
numbs = '1234567890'
count = 0
a = {0}
for f in os.listdir('.'):
    if f.endswith('.txt') or f.endswith('.pdf'):
        i = 0
        for num in numbs:
            if num not in f:
                i += 1
                if i == 10:
                    count += 1
                    a.add(f)
print(count)
for i in a:
    if i != 0:
        print(i)
