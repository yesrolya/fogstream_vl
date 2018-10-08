# Найти все уникальные элементы в списке.
# Список произвольной длины и может состоять как из чисел, так и строк.

lst = input('Input space-separated list: ')
lst = lst.split(' ')

unique_lst = []

for el in lst:
    if lst.count(el) == 1:
        unique_lst.append(el)

print("Unique elements: ", *unique_lst)
