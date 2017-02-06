import re
f = open('new.txt', 'r', encoding = 'utf-8')
f = f.readlines()
a = 0
for i in f:
    m = re.search("(Часовой пояс)", i)
    if m != None:
        a = m.group(0)
for i in range(len(f)):
    if f[i][0] == a[0] and f[i][1] == a[1]:
        print(f[i+1])
        
        
    
