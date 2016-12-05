arr = []
f = open('text.txt', 'r', encoding = 'utf-8')
line = f.readlines
for line in f:
    length = len(line)
    arr.append(length)
a = max(arr)
b = min(arr)
print(float(a)/float(b))
f.close()
                
        
        
