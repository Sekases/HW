user_size = int(input('Задайте велечену списка: '))

user_list = [*range(1, user_size+1)]

user_list_chet = []
user_list_nechet = []
for i in user_list:
    if i % 2:
        user_list_nechet.append(i)
    else:
        user_list_chet.append(i)

user_list_chet.extend(user_list_nechet)
print(user_list_chet)