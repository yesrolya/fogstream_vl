# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

lst = input('Input space-separated list of numbers: ')
lst = lst.split(' ')

try:
    prev = lst[0]
    result = []

    for l in lst:
        if prev < l:
            result.append(l)
        prev = l

    prev = result[0]
    print('List of values: ', *result)

except IndexError:
    print('List is empty')
