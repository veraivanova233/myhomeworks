s = input()
a = s.find('h')
b = s.rfind('h')
print (s[int(b)-1:a:-1])
