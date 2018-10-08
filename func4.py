# Написать функцию avaranger, которая принимает 1 аргумент - любое число и возвращается среднее арифметическое значение,
# на основании текущего числа и предыдущих, которые были введены ранее.

a: float = 0
b: float = 0


def avaranger(c):
    global a
    global b
    print('Average of ', a, b, c, ' is ', (a + b + float(c)) / 3)
    a = b
    b = float(c)
    return

avaranger(input())
avaranger(input())
avaranger(input())
avaranger(input())
avaranger(input())
