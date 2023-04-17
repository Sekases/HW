num = input('Введите число: ')

while not isinstance(num, int):
    try:
        num = int(num)
    except ValueError:
        num = input('Введите ЧИСЛО!: ')

def int_to_bin_and_r(num):
    text = ''
    while num > 0:
        text += str(num % 2)
        num = num // 2
    text = text[::-1]
    print(text)
    text = text[::-1]
    text = list(text)
    for i in range(0, len(text)):
        text[i] = int(text[i])
        text[i] = text[i] * (2 ** i)
    sum = 0
    for i in text:
        sum += i
    return sum

a = int_to_bin_and_r(num)
print(a)