# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

dictionary = {
    'Belarus': ('Minsk', 'Grodno', 'Molodechno'),
    'Russia': ('Moscow', 'Saint Petersburg', 'Omsk'),
    'Ukraine': ('Kyiv', 'Odessa', 'Lviv'),
    'Georgia': ('Tbilisi', 'Batumi', 'Kutaisi')
}

name_city = input('Enter city: ')

for i, j in dictionary.items():
    for k in dictionary.get(i):
        if k == name_city:
            print(f'This city is in {i}')
