#My functions
def chek_int(dig):
    while not isinstance(dig, int):
        try:
            dig = int(dig)
        except ValueError:
            dig = input('Введите ЧИСЛО!: ')
        return dig


#Start programm
size_list = input('Установите размер списка: ')

size_list = chek_int(size_list)
user_list = [n for n in range(1, size_list + 1)]

user_slice = input('С какого элемента срезаем: ')
user_slice = chek_int(user_slice)

user_list_2 = user_list[:user_slice:]
del user_list[:user_slice:]
user_list.extend(user_list_2)

print(user_list)