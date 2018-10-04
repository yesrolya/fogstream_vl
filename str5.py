# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

s: str = input('Input line: ')
i: int = len(s) - (len(s)%3)
while i > 0:
    s = s[0:i] + s[(i+1):len(s)]
    i -= 3
s = s[1:len(s)]

print(s)
