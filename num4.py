# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год.
# Программа получает на вход целые числа P, X, Y и должна вывести два числа:
# величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
import math
print('Enter interest rate: ')
p = int(input())
print('Enter deposit amount: ')
x = int(input())
y = int(input())
print('Deposit amount in a year: ')
sum = x * 100 + y
sum = math.floor(sum * (1 + p*0.01))
#без math
#sum = int(sum * (1 + p*0.01))
print(*divmod(sum, 100))
