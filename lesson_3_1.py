# Заполнить список степенями числа 2 (от 2^1 до 2^n)
degree = int(input('Enter number: '))
numbers_list = [2 ** (i + 1) for i in range(degree)]
print(numbers_list)

# numbers = [2, 4, 8, 16, 32]
