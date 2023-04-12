num_11 = input('Введите первый операнд(): ')
oper = input('Введите оператор: ')
num_22 = input('Введите второй операнд: ')

while 1:
    try:
        num_1, num_2 = int(num_11), int(num_22)
        if oper == '+':
          print(num_1 + num_2)
        elif oper == '-':
            print(num_1 - num_2)
        elif oper == '*':
         print(num_1 * num_2)
        elif oper == '/':
            try:
                print(num_1 / num_2)
            except ZeroDivisionError:
                print('НА НОЛЬ НЕ ДЕЛЮ!')

    except:
        print('Введён неверный оператор или операнд!')

    num_1 = input('Введите первый операнд(! - для выхода): ')

    if num_1 == '!':
        break

    oper = input('Введите оператор: ')
    num_2 = input('Введите второй операнд: ')

print('Программа завершена без ошибок.')