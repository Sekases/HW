user_number = int(input('Введите число: '))

list_of_numbers = range(1, user_number + 1)
q = 1

for i in list_of_numbers:
    i = 2 ** i
    print('2 to the power of', q, '=', i)
    q += 1




