# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
import random

list_random = [random.randint(0, 100) for i in range(0, 10)]
print(f' No:{list_random}')


def is_turn(any_list):
    for i in range(len(list_random)):
        for j in range(len(list_random) - i):
            buff = list_random[i]
            list_random[i] = list_random[i + j]
            list_random[i + j] = buff
    return any_list


print(f'Yes:{is_turn(list_random)}')
