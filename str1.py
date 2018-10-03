# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов.

print("Input line: ")
s: str = input()
num: int = 0
prev = 1
for c in s:
    if prev == 1 and c != ' ':
        num = num + 1
        prev = 0
    elif c == ' ':
        prev = 1
print("Number of words in line: ")
print(num)
#OR
list = s.split(' ')
num1: int = 0
for l in list:
    if l != '':
        num1 += 1
print(num1)

