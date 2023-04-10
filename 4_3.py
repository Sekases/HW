mans = int(input('Введите количество персон: '))
my_dict = dict.fromkeys(range(1, mans + 1))

for i in my_dict:
   my_dict[i] = {'name' : None, 'email' : None}

print('Ваш словарь:', my_dict)

while 1:
   key_num = int(input('Введите номер ключа(Нажмите 0 для выхода): '))

   if key_num == 0:
      break

   key_deep = input('Введите название ключа(name или email): ')
   user_text = input('Введите ваше значение: ')

   if user_text == 0:
      break

   my_dict[key_num][key_deep] = user_text

   print(my_dict)

print('END')