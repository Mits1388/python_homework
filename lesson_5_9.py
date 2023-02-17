# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

dictionary = {
    0: {'first name': 'David', 'last name': 'Novak', 'phone': '1 441 673 4321', 'email': ''},
    1: {'first name': 'Evelina', 'last name': 'Bogdanova', 'phone': '1 787 864 1156', 'email': 'elvina@gmail.com'},
    2: {'first name': 'Roy', 'last name': 'Jones', 'phone': '1 340 456 8546', 'email': ''},
    3: {'first name': 'Philip', 'last name': 'Lum', 'phone': '1 671 333 1451'},
    4: {'first name': 'Jessica', 'last name': 'Parker', 'phone': '1 721 777 7777', 'email': 'jessica@gmail.com'},
    5: {'first name': 'Marie', 'last name': 'Broadbet', 'phone': '53 343 45 342', 'email': 'marie@gmail.com'},
}

key = 'email'
for i, j in dictionary.items():

    for k, v in j.items():
        if k == 'email':
            if j[k] == '':
                print(j.get('first name'))
    if key not in j:
        print(j.get('first name'))
