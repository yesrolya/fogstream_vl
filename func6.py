# Реализовать функцию map, принимающей два аргумента: список и произвольную арифметическую функцию.
# Функция map должна возвращать новый список, элементы которого являются результатом функции func.


def map(function, lst):
    new_lst = []
    for l in lst:
        new_lst.append(function(l))
    return new_lst


def new_func(x):
    return (float(x))**2

lst = input()
lst = lst.split(' ')
print(*map(new_func, lst))