users = {
    1 : {
        'Name' : 'Kostya',
        'Lastname' : 'Golubovich',
        'Phone' : 375299942160,
        'Email' : 'tipo4ek1213@gmail.com'
    },
    2 : {
        'Name' : 'Max',
        'Lastname' : 'Dondukov',
        'Phone' : 375299933993,
        'Email' : 'kakaha@gmail.com'
    },
    3 : {
        'Name' : 'Sasha',
        'Lastname' : 'Rumyancev',
        'Phone' : 375449900880,
        'Email' : None
    },
    4 : {
        'Name': 'Nastya',
        'Lastname': 'Karlione',
        'Phone': 375449977440,
        'Email': None
    }
}

for val in users.values():
    if val['Email'] == None:
        print(val['Name'])