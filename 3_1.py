text = input('Введите текст: ')

def first(text):
    new_text = text.replace(' ', '-')
    print(new_text)

def second(text):
    new_text = text.split()
    print('-'.join(new_text))

