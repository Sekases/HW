user_size = int(input('Введите размер своего списка: '))

user_list = [*range(1, user_size+1)]

my_dict = {}

for i in user_list:
    my_dict[f'key{i}'] = i

print(my_dict)

#Можно и так

#m_list = [1, 2, 3, 4, 5]
#li = [*m_list]