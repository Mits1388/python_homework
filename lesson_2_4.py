# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
number_first = int(input('Enter the number one: '))
number_second = int(input('Enter the number two: '))
number_third = int(input('Enter the number three: '))
print('User enter positive number', (number_first >= 0) + (number_second >= 0) + (number_third >= 0))
print('User enter negative number', (number_first < 0) + (number_second < 0) + (number_third < 0))

