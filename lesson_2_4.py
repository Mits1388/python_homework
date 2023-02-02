#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
cycle_numbers = 0
positive_number = 0
negative_number = 0

while cycle_numbers < 3:
    number = int(input(f'Enter {cycle_numbers + 1} number: '))
    if number >= 0:
        positive_number += 1
    else:
        negative_number += 1
    cycle_numbers += 1

print(f'User enter {positive_number} positive number')
print(f'User enter {negative_number} negative number')
