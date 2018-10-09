# Создать класс Fraction, который должен иметь два поля: числитель a и знаменатель b.
# Оба поля должны быть типа int. Реализовать методы: сокращение дробей, сравнение, сложение и умножение.


class Fraction:
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # == = 0, x< = 1, x> = -1

    def reduct(self):
        # сокращение дроби
        a = self.a
        b = self.b
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        self.a = int(self.a / (a + b))
        self.b = int(self.b / (a + b))
        return self

    def compare(self, x):
        # сравнение дробей
        # при равенстве возвращает 0
        # если это число > => 1
        # если это число > = > 1
        b1 = self.b
        b2 = x.b
        while b1 != 0 and b2 != 0:
            if b1 > b2:
                b1 = b1 % b2
            else:
                b2 = b2 % b1
        nod = b1+b2
        a1 = self.a * (x.b / nod)
        a2 = x.a * (self.b / nod)
        if a1 == a2:
            return 0
        elif a1 > a2:
            return 1
        else:
            return -1

    def add(self, num):
        a = 0
        b = 0
        if type(num) is Fraction:
            a = num.a
            b = num.b
        elif type(num) is int:
            b = self.b
            a = self.b * num
        mn = 1
        if a * self.a < 0:
            # разные знаки
            mn = -1

        b1 = self.b
        b2 = b
        while b1 != 0 and b2 != 0:
            if b1 > b2:
                b1 = b1 % b2
            else:
                b2 = b2 % b1
        nod = b1 + b2

        ret = Fraction(int((self.a * (b/nod)) + (mn * a * (self.b/nod))), int(self.b / nod * b))
        return ret.reduct()

    def multiply(self, num):
        a = 0
        b = 0
        if type(num) is Fraction:
            a = num.a
            b = num.b
        elif type(num) is int:
            b = 1
            a = num
        ret = Fraction(int(self.a * a), int(self.b * b))
        return ret.reduct()

    def print(self):
        print(int(self.a), '/', int(self.b))
        return

new_num = Fraction(1, 2)
new_num1 = Fraction(6, 8)
new_num.print()
new_num1.reduct()
new_num1.print()
(new_num1.add(new_num)).print()
(new_num.multiply(new_num1)).print()

