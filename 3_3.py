name, age, city = input('Ваше имя? '), input('Сколько вам полных лет? '), input('В каком городе вы проживаете? ')

def first(name, age, city):
    text = 'Приветствую %s и добро пожаловать в мир прекрасного языка Python. В городе %s у нас как раз' %(name, city) + \
        'проходят достойные курсы, ведь %s прожитых года - это самый зрелый возраст для смены круга деятельности!' %(age)
    print(text)

def second(name, age, city):
    text = 'Приветствую {} и добро пожаловать в мир прекрасного языка Python. В городе {} у нас как раз'.format(name, city)  + \
        'проходят достойные курсы, ведь {} прожитых года - это самый зрелый возраст для смены круга деятельности!'.format(age)
    print(text)

def third(name, age, city):
    text = f'Приветствую {name} и добро пожаловать в мир прекрасного языка Python. В городе {city} у нас как раз' + \
        f'проходят достойные курсы, ведь {age} прожитых года - это самый зрелый возраст для смены круга деятельности!'
    print(text)

third(name,age, city)
