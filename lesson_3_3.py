# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
from pprint import pprint

number = int(input('Enter number: '))
users = {k: {'name': input(f'name {k+1}: '), 'email': input(f'email {k+1}: ')} for k in range(number)}
pprint(users)

# user = {
#     0: {'name': 'Ben', 'email': 'ben@com'},
#     1: {'name': 'Tom', 'email': 'tom_12@com'},
#     2: {'name': 'Alex', 'email': 'alex2000@com'}
# }

