wordlist = []
word = input('Введите слово: ')
while word != '':
    wordlist.append(word)
    word = input('Введите слово: ')
for i in wordlist:
    if len(i) > 5:
        print (i)
