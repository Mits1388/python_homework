# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число
number_one = int(input('Enter number one: '))
action = input('Enter action: ')
number_two = int(input('Enter number two: '))
if action == '+':
    print(number_one + number_two)
elif action == '-':
    print(number_one - number_two)
elif action == '*':
    print(number_one * number_two)
elif action == '/':
    print(round(number_one / number_two, 1))
else:
    print('it is a simple calculator only +, -, *, /')
