from random import *

user_size = int(input('Введите размер списка: '))

user_list = [*range(0, user_size)]

for i in range(0, len(user_list)):
    user_list[i] = randint(0, 18)
print(user_list)

for i in range(0, len(user_list)):
    if i == (len(user_list) - 1):
        user_list[i] = user_list[i-1] + user_list[0]
        break
    user_list[i] = user_list[i-1] + user_list[i+1]



print(user_list)