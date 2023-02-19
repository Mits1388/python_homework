# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

decimal_number = int(input('Enter decimal number: '))


def convert_bin(number):
    b = ''
    while number > 0:
        b = str(number % 2) + b
        number //= 2
    return b


print(f'Binary number = {convert_bin(decimal_number)}')

binary_number = input('Enter binary number: ')


def convert_dec(number):
    a = []
    n = 1
    for i in reversed(number):
        a.append(int(i) * n)
        n *= 2
    return sum(a)


print(f'Decimal number: {convert_dec(binary_number)}')
