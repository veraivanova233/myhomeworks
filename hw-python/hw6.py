def file():
    f = open('austen.txt', 'r', encoding = 'utf-8')
    s = f.read()
    s = s.split(' ')
    print(count_frequency(s))
    print(count_nouns(s))
    f.close()
def count_nouns(s):
    a = []
    b = []
    for i in s:
        if i[len(i)-1] == 's' and i[len(i)-2] == 's' and i[len(i)-3] == 'e' and i[len(i)-4] == 'n':
            a.append(i)
    b.append(a[0])
    for i in a:
        if i not in b:
            b.append(i)
    return len(b)
def count_frequency(s):
    a = []
    b = []
    flist = []
    number = 0
    for i in s:
        if i[len(i)-1] == 's' and i[len(i)-2] == 's' and i[len(i)-3] == 'e' and i[len(i)-4] == 'n':
            a.append(i)
    for elem in a:
        freq = 0
        if elem not in b:
            for i in a[number+1:]:
                if elem == i:
                    freq += 1
            b.append(elem)
            flist.append(freq)
            number += 1
        else:
            number += 1
    return max(flist)+1
print(file())
        
    
            
        
        
    
        
        
