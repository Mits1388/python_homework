# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

decimal_number = int(input('Enter decimal number: '))


def is_convert_bin(number):
    b = ''
    while number > 0:
        b = str(number % 2) + b
        number //= 2
    return b


print(f'Binary number = {is_convert_bin(decimal_number)}')

binary_number = input('Enter binary number: ')


def is_convert_dec(number):
    a = []
    n = 1
    for i in reversed(number):
        a.append(int(i) * n)
        n *= 2
    return sum(a)


print(f'Decimal number: {is_convert_dec(binary_number)}')
