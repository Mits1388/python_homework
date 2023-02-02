#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

positive_number = 0
negative_number = 0

if first_number >= 0:
    positive_number += 1
else:
    negative_number += 1
if second_number >= 0:
    positive_number += 1
else:
    negative_number += 1
if third_number >= 0:
    positive_number += 1
else:
    negative_number += 1

if positive_number == 1:
    print(f'Пользователь ввел {positive_number} положительное число')
else:
    print(f'Пользователь ввел {positive_number} положительных числа')
if negative_number == 1:
    print(f'Пользователь ввел {negative_number} отрицательное число')
else:
    print(f'Пользователь ввел {negative_number} отрицательных числа')