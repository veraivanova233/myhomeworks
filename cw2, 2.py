import re
f = open('corpus.txt', 'r', encoding = 'utf-8')
w = open('output1.txt', 'w', encoding = 'utf-8')
words = dict()
lines = f.readlines()
for line in lines:
    if "<w lemma=" in line:
# 1 способ найти атрибут type:
        m = re.search('.*type="(.*)">.*', line)
# 2 способ, но он очень долго грузится:
#        a = 0
#        b = ''
#        for i in range(len(line)):            
#            if line[i] == '"':
#                a += 1
#            if a == 3:
#                for u in line[i+1:]:
#                    while u != '"':
#                        b += u
#                    print(b)
        if m != None:
            if m.group(1) in words.keys():
                    words[m.group(1)] += 1
            else:
                    words[m.group(1)] = 1
for i in words.keys():
    w.write(i + ' ' + str(words[i]) + '\n')
f.close()
w.close()

                
