s = input()
a = s.find('h')
b = s.rfind ('h')
first = s[:a]
second = s[int(b)+1:]
third = first + second
print (third)
