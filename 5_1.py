num_1 = int(input('Введите первое число(число, c которого будет вывод): '))
num_2 = int(input('Введите второе число(которому будут кратны числа): '))
num_3 = int(input('Введите третье число(сколько чисел вывести): '))
itera = 0
sch = num_1

while not(itera == num_3):

    if not(sch % num_2):
        print(sch, end= ' ')
        itera += 1

    sch += 1

print('\nEnd!')