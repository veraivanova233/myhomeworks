# метрический размер - хорей (ударение на нечётный слог)
import random
def noun(number):
    if number == 1:
       f = open('monosyllabic nouns.txt', 'r', encoding = 'utf-8')
       s = f.read()
       a = s.split(' ')
       c = []
       for i in a:
           c.append(i)
       x = random.choice(c)
       return x 
    f = open('polysyllabic nouns.txt', 'r', encoding = 'utf-8')
    s = f.read()
    a = s.split(' ')
    c = []
    for i in a:
        c.append(i)
    x = random.choice(a)
    return x
def additional():
    f = open('adds.txt', 'r', encoding = 'utf-8')
    s = f.read()
    a = s.split(' ')
    c = []
    for i in a:
        c.append(i)
    x = random.choice(c)
    return x
def adverb():
    f = open('adverbs.txt', 'r', encoding = 'utf-8')
    s = f.read()
    a = s.split(' ')
    c = []
    for i in a:
        c.append(i)
    x = random.choice(c)
    return x
def verb():
    f = open('verbs.txt', 'r', encoding = 'utf-8')
    s = f.read()
    a = s.split(' ')
    c = []
    for i in a:
        c.append(i)
    x = random.choice(c)
    return x
def clitic():
    f = open('clitics.txt', 'r', encoding = 'utf-8')
    s = f.read()
    a = s.split(' ')
    c = []
    for i in a:
        c.append(i)
    x = random.choice(c)
    return x
def adjective():
    f = open('adjectives.txt', 'r', encoding = 'utf-8')
    s = f.read()
    a = s.split(' ')
    c = []
    for i in a:
        c.append(i)
    x = random.choice(c)
    return x
def short_adj():
    f = open('short_adjs.txt', 'r', encoding = 'utf-8')
    s = f.read()
    a = s.split(' ')
    c = []
    for i in a:
        c.append(i)
    x = random.choice(c)
    return x     
def mark():
     f = open('marks.txt', 'r', encoding = 'utf-8')
     s = f.read()
     a = s.split(' ')
     c = []
     for i in a:
         c.append(i)
     x = random.choice(c)
     return x
def verse1():
    return noun(1) + ' ' + additional() + ' ' + verb() + mark()
def verse2():
    return clitic() + ' - ' + noun(2) + ', ' + clitic() + ' - ' + noun(2) + mark()
def verse3():
    return adjective() + ', ' + adjective() + ' ' + noun(1) + ' - ' + noun(2) + mark()
def verse4():
    return short_adj() + ' ' + adjective() + ' ' + noun(1) + mark()
def verse5():
    return noun(1) + ' ' + adverb() + ' ' + verb() + mark()
def make_verse():
    verse = random.choice([1,2,3,4,5])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    elif verse == 3:
        return verse3()
    elif verse == 4:
        return verse4()
    else:
        return verse5()
for n in range(4):
    print(make_verse())
    
