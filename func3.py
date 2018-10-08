# Дан список результатов попыток одного спортсмена для некоторого соревнования.
# Написать функцию, которая считает сколько за сессию был установлен новый рекорд,
# т.е. текущее значение превышает значение максимального.
#
# Например. Имеем список результатов.:
# scores = [10, 5, 20, 20, 4, 5, 2, 25, 1].
# В данном случае ответ: 2.


def top_score(scores):
    x: int = 0
    max: float = -1000
    for s in scores:
        if float(s) > max:
            if max != -1000:
                x += 1
            max = float(s)
    return x


scores = input('Input space-separated list: ')
scores = scores.split(' ')
print(top_score(scores))
