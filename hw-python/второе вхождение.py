s = input()
t = s.count('f')
if t == 0:
    print ('-2')
if t!= 0:
    if t == 1:
        print ('-1')
    else:
        a = s.find('f')
        b = s[int(a)+1:].find('f')
        print (int(b) + 1 + int(a))
