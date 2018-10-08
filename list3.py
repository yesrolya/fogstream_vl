# Дан список чисел.
# Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

lst = input('Input space-separated list of numbers: ')
lst = lst.split(' ')

max_index: int = 0
try:
    for l in lst:
        if float(lst[max_index]) < float(l):
            max_index = lst.index(l)

    print('Value: ', lst[max_index], '\nIndex: ', max_index)

except ValueError:
    print('Could not convert string in list to float/ a lot of spaces')
except IndexError:
    print('List is empty')
except TypeError:
    print('List is empty')