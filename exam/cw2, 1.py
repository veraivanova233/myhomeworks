f = open('corpus.txt', 'r', encoding = 'utf-8')
y = open('output.txt', 'w', encoding = 'utf-8')
lines = f.readlines()
summ = 0
for line in lines:
    summ += 1
summ = str(summ)
y.write(summ)
f.close()
y.close()


    
