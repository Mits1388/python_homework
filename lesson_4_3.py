# Вывести четные числа от 2 до N по 5 в строку
n = int(input('Enter number: '))
numbers = []
for i in range(1, n + 1):
    if i % 2 == 0:
        numbers.append(str(i))
# print(numbers)
for i in range(0, len(numbers), 5):
    print(' '.join(numbers[i:i + 5]))
