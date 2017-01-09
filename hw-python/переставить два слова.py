s = input()
q = s[0]
s = s.replace(s[0],s[1])
s = s.replace(s[1],q)
print(s)
