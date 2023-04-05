f_n, s_n, t_n = float(input('Введите первое число: ')), float(input('Введите второе число: ')), float(input('Введите третье число: '))

sum_a = (f_n / abs(f_n)) + (s_n / abs(s_n)) + (t_n / abs(t_n))

pos_n = int((sum_a + 1) / 2)
neg_n = int((sum_a - 1) / 2)

print('Положительные числа:', pos_n)
print('Отрицательные числа:', neg_n)