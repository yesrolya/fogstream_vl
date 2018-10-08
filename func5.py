# Реализовать функцию-валидатор почтовых адресов. Принимает строку, которая содержит адрес электронной почты.
# Возвращает True, если адрес валидный, иначе возвращает False.

def check_email(str):
    if str.find(' ') != -1: return False
    # print('Не содержит пробелов')
    if not('A' <= str[0] <= 'Z' or 'a' <= str[0] <= 'z' or '0' <= str[0] <= '9'): return False
    # print('Начинается с корректного символа')
    if 0 >= str.find('@') >= 64: return False
    # print('localpart правильной длины')
    for s in str[0: str.find('@')]:
        if not (0 < ord(s) <= 127):
            return False
    # print('localpart содержит корректные символы')
    str = str.split('@')
    if len(str) > 2: return False
    str = str[1]
    if len(str) < 1 or len(str) > 253: return False
    str = str.split('.')
    if len(str) < 2: return False
    for s in str:
        if len(s) < 1 or len(s) > 63: return False
        for ch in s:
            if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9'):
                return False
    # print('No domain can start with a period, end with a period, or have two successive periods')
    return True


str = input('Input email: ')
if check_email(str):
    print('Valid')
else:
    print('Non-Valid')
