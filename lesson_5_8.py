# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
import dictionary as dictionary

dictionary = {
    'Belarus': {'Minsk', 'Grodno', 'Molodechno'},
    'Russia': {'Moscow', 'Saint Petersburg', 'Omsk'},
    'Ukraine': {'Kyiv', 'Odessa', 'Lviv'},
    'Georgia': {'Tbilisi', 'Batumi', 'Kutaisi'}
}

name_city = input('Enter city: ')


def country(any_dictionary):
    for i, j in dictionary.items():
        if name_city in j:
            return i


print(f'This city is in {country(dictionary)}')

#
# for i, j in dictionary.items():
#     for k in dictionary.get(i):
#         if k == name_city:
#             print(f'This city is in {i}')
#
#             key = 'email'
#             for i, j in dictionary.items():
#                 if key not in j or j.get(key) == '':
#                     print(j.get('first name') + ' doesn`t have an email')
