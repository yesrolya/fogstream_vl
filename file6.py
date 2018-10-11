# В файле содержится текстовая строка.
# Определить частоту повторяемости каждой буквы в тексте и вывести ее.

with open('f6_in.txt', 'r') as file:
    line: str = file.readline()

print("Only english:")
for ch in range(ord('a'), ord('z') + 1, 1):
    x = line.count(chr(ch))
    x += line.count(chr(ch + (ord('A') - ord('a'))))
    if x > 0:
        print(chr(ch), ':', x)


