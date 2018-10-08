# Даны два списка произвольной длины каждый. Списки могут содержать как числа, так и строки.
# Необходимо вывести только те элементы, которые входят как первый список, так и во второй.

lst1 = input('Input first space-separated list of numbers: ')
lst1 = lst1.split(' ')

lst2 = input('Input second space-separated list of numbers: ')
lst2 = lst2.split(' ')

lst_result = []

for l in lst1:
    if lst2.count(l):
        lst_result.append(l)

print('Both lists contain ', *lst_result)
