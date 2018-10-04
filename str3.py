# Дана строка. Если в этой строке буква f встречается только один раз,
# выведите её индекс. Если она встречается два и более раз,
# выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, вывести -1.

s: str = input('Input line: ')
num_first: int = s.find('f')
num_last: int = s.rfind('f')
if num_first == -1 or num_first == num_last:
    print(num_first)
else:
    print('First index: ', num_first, ', last index: ', num_last)

