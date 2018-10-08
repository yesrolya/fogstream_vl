# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# Выведите три найденных числа в формате, приведенном в примере.

file = open('f3_in.txt', 'r')
lines = file.readlines()
file.close()

line = 0
word = 0
letter = 0

for l in lines:
    if not l.isspace():
        line += 1
    l = l.split(' ')
    for w in l:
        if not w.isspace():
            word += 1
        for ch in w:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                letter += 1

print("Input file contains:")
print(letter, " letters")
print(word, " words")
print(line, " lines")