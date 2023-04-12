num = input('Введите число: ')

while not isinstance(num, int):

    try:
        num = int(num)
    except:
        print('Я принимаю лишь числа!')
        num = input('Введите ЧИСЛО!: ')

for i in range(2, num + 1):
    if not (i % 2):
        print(i, end = ' ')
    if not (i % 10):
        print('\n')
