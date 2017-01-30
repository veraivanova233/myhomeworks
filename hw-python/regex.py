# 2 вариант
import re
f = open('examples.txt', 'r', encoding = 'utf-8')
f = f.readlines()
result = 0
for i in f:
    while result != None:
        result = re.search("на(ш(л(и|а)|ёл|едший(ся)?)|й(ти|дё(ться|тесь|тся|мся|шься|т|м|те)|д(енный|утся|усь|т|я))|х(ожу|ожусь|од(ит|им|имся|ишься|ится|ишь|ят|ите|ить)))", i)
        print(result.group(0))
        i = i[:result.start()] + i[result.end()+1:]
        
        
