f = open('quotes.txt', 'r', encoding = 'utf-8')
r = f.read()
s = r.split('\n')
a = []
for i in range(len(s)):
    a.append(s[i])
#2
for q in a:
    if 'разум' in q:
        b = q.split('- ')
        print(b)
        
