# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.

lst = input('Input space-separated list of numbers: ')
lst = lst.split(' ')

i: int = 1
try:
    while i < len(lst):
        if (float(lst[i]) * float(lst[i-1])) >= 0:
            print(*lst[i-1: i + 1: 1])
            break;
        i += 1
except ValueError:
    print('Could not convert string in list to float')
