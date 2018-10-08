# Дан файл с расписанием занятий на неделю.
# Помимо названия предмета в нем также указано лекция это, или практическое занятие, или лабораторная работа.
# В одной строке может быть указаны только один предмет с информацией о нем.
# Посчитать, сколько за неделю проходит практических занятий, лекций и лабораторных работ.

file = open('f1_in.txt', 'r')
schedule = file.readlines()
file.close()

lect_name = "(лекц.)"
lab_name = "(лаб.)"
pz_name = "(практ.)"
lect_count = 0
lab_count = 0
pz_count = 0


for line in schedule:
    if line.find(lect_name) != -1:
        lect_count += 1
    elif line.find(lab_name) != -1:
        lab_count += 1
    elif line.find(pz_name) != -1:
        pz_count += 1

print('Lectures: ', lect_count)
print('Lab: ', lab_count)
print('Practice: ', pz_count)