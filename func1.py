# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
# Считайте четыре действительных числа и выведите результат работы этой функции.


def distance(x1, y1, x2, y2):
    return pow(pow((x1 - x2), 2) + pow((y1 - y2), 2), 0.5)


x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

print(distance(x1, y1, x2, y2))
