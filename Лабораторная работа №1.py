import csv
import re

symdolsPunct = '.,!?\"\':;-()'

symbols = 0 
words = 0
sentences = 0
spaces = 0
punctuation = 0

with open('steam_description_data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        string = ','.join(line)
        symbols += len(string)
        for symbol in symdolsPunct:
            punctuation += string.count(symbol)
        spaces += string.count(' ')
        words += len(string.split())
        sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", string))

print('Общее кол-во знаков:',symbols)
print('Кол-во символов без знаков препинания:', symbols - punctuation)
print('Кол-во символов без пробелов:',symbols-spaces)
print('Кол-во слов:',words)
print('Кол-во предложений:',sentences)
