# В одном файле в каждой строке записаны координаты пар точек.
# Каждая координата отделена от другой пробелом.
# Например, строка вида 3 6 -2 4 означает, что координаты первой точки (3;6), второй - (-2;4).
# Во второй файл требуется построчно записать наибольшее и наименьшее расстояние между точками.


def distance(*lst):
    x1 = float(lst[0])
    y1 = float(lst[1])
    x2 = float(lst[2])
    y2 = float(lst[3])
    return pow(pow((x1 - x2), 2) + pow((y1 - y2), 2), 0.5)


file = open('f2_in.txt', 'r')
coordinates = file.readlines()
file.close()

min_value = -1
max_value = -1

for c in coordinates:
    d = distance(*c.split(' '))
    #print(d)
    if min_value == -1:
        min_value = d
        max_value = d
    elif min_value > d:
        min_value = d
    elif max_value < d:
        max_value = d

file = open('f2_out.txt', 'w')
print('MAX: ', max_value, file=file)
print('MIN: ', min_value, file=file)
file.close()
