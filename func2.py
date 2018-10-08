# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.


def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(pow(x, 0.5)) + 1):
            if x%i == 0:
                return False
    return True


x = int(input())
print(is_prime(x))
