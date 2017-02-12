import re
f = open('text.txt', 'r', encoding = 'utf-8')
y = open('text1.txt', 'w', encoding = 'utf-8')
lines = f.readlines()
for i in lines:
    i = re.sub('(^Викинг)', 'Бурундук', i, flags = re.U)
    i = re.sub('(викинг)', 'бурундук', i, flags = re.U)
    i = re.sub('(Ви́кинги)', 'Бурундуки́', i, flags = re.U)
    i = str(i)
    y.write(i)
f.close()




    
