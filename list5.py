# Программа получает на вход невозрастающую(все элементы списка не упорядочены по возрастанию)
# последовательность натуральных чисел. После этого вводится число X.
# Все числа во входных данных натуральные и не превышают 200. Выведите индекс, где окажется число Х.
# Если в списке есть элемент с таким значением, то число Х помещается после него.

lst = input('Input space-separated list of numbers: ')
lst = lst.split(' ')

x = int(input('Input X: '))
result_index: int = -1

for l in lst:
    if int(l) == x:
        result_index = lst.index(l) + 1
        break
    elif int(l) < x:
        result_index = lst.index(l)
        break

if result_index == -1:
    result_index = len(lst)

print('INDEX in array of X is ', result_index)
