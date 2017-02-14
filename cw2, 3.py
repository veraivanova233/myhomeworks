import re
f = open('output1.txt', 'r', encoding = 'utf-8')
e = open('output2.txt', 'w', encoding = 'utf-8')
words = dict()
lines = f.readlines()
for line in lines:
    line = line.split()
    if line[0][0] == 'f' and line[0][2] == 'h':
        e.write(line[0] + ',' + ' ')
f.close()
e.close()
