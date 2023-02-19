# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
import random

n = int(input('Enter N: '))
list_random = [random.randint(0, 100) for i in range(0, 10)]
print(f'Without shift:{list_random}')


def shift(any_list):
    list_shift = list_random[n:] + list_random[:n]
    return list_shift


print(f'   With shift:{shift(list_random)}')
