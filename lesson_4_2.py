# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число
try:
    a = int(input('Enter number one: '))
    action = input('Enter action: ')
    b = int(input('Enter number two: '))
    if action == '+':
        print(f'{a} + {b} =', a + b)
    elif action == '-':
        print(f'{a} - {b} =', a - b)
    elif action == '*':
        print(f'{a} * {b} =', a * b)
    elif action == '/':
        try:
            print(f'{a} / {b} =', round(a / b, 2))
        except ZeroDivisionError as e:
            print('Can`t be divided by zero')
    else:
        print('Invalid action')
except ValueError as e:
    print('Invalid value')
