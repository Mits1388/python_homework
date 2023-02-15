# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

decimal_number = int(input('Enter decimal number: '))
b = ''
while decimal_number > 0:
    b = str(decimal_number % 2)+b
    decimal_number //= 2
print(f'Binary number = {b}')

binary_number = input('Enter binary number: ')
a = []
n = 1
for i in reversed(binary_number):
    a.append(int(i)*n)
    n *= 2
print(f'Decimal number: {sum(a)}')
