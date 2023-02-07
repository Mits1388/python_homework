# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
from pprint import pprint

numbers = int(input('Enter number: '))

list_name = [input(f'name {i+1}: ') for i in range(numbers)]
print(list_name)
list_email = [input(f'email {j+1}: ') for j in range(numbers)]
print(list_email)
users = {k: {'name': list_name[k], 'email': list_email[k]} for k in range(numbers)}
pprint(users)

# user = {
#     0: {'name': 'Ben', 'email': 'ben@com'},
#     1: {'name': 'Tom', 'email': 'tom_12@com'},
#     2: {'name': 'Alex', 'email': 'alex2000@com'}
# }

