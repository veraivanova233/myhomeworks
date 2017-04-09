# Вариант 2
file = open('frida.txt', 'r', encoding = 'utf-8')
file = file.read().split('.')
lines = []
for sent in file:
    for symb in sent:
        if symb == ',' or symb == '-' or symb == ':' or symb == ';':
            sent = sent.replace(symb, '')
    lines.append(sent)
sents = [i for i in lines if len(i.split()) > 10]
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'
words = []
for sent in sents:
    for word in sent.split():
        if word[0] in letters:
            words.append(word)
# for sent in sents:
#     words = [word for word in sent.split() if word[0] in letters]
# В генераторе списка сверху написано вроде то же самое, что и в 5 строках выше, но при этом включаются не все результаты. Я не понимаю, почему.
template = 'Word: {:>5}'
for word in words:
    print(template.format(word))
