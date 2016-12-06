f = open('quotes.txt', 'r', encoding = 'utf-8')
data = f.read().split('\n')
a = []
for line in data:
    linewords = line.split(' ')
    for q in range(len(linewords)):
            a.append(linewords[q])
for p in a:
    if len(p)<10:
        print(p)

