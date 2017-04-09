s = input("Введите слово (в кириллице): ")
a = (s[0::2])
q = len(str(a))
d = 0
b = 0
c = 0
for i in a:
    if i == "о":
        print (i)
    else: d += 1
    if i == "п":
        print (i)
    else: b +=1
    if i == "е":
        print (i)
    else: c+=1
if (d == q) and (b == q) and (c == q):
            print ("Нет таких букв.")
