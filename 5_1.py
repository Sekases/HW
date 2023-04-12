num_1 = int(input('Введите первое число(число, больше которого будет вывод): '))
num_2 = int(input('Введите второе число(которому будут кратны числа): '))
num_3 = int(input('Введите третье число(сколько чисел вывести): '))
itera = -1

while not(itera == num_3):
    itera += 1
    if itera <= num_1:
        continue
    if not(itera % num_2):
        print(itera, end= ' ')

print('\nEnd!')