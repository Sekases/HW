user_text = input('Введите текст: ')
low_user_text_n = user_text.lower()
low_user_text = sorted(low_user_text_n)
us_dict = {low_user_text[0] : low_user_text.count(low_user_text[0])}

for i in low_user_text:
    if i in us_dict:
        continue
    else:
        us_dict[i] = low_user_text.count(i)

print(us_dict)