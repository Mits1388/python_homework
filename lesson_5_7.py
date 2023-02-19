# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
import random

list_random = [random.randint(0, 5) for i in range(0, 5)]

print(f'Random list: {list_random}')


def sum_of_neighbors(any_list):
    a = []
    for i in range(len(any_list)):
        if i != len(any_list) - 1:
            a.append(any_list[i + 1] + any_list[i - 1])
        else:
            a.append(any_list[i - 1] + any_list[0])
    return a


print(f'Sum of neighboring elements: {sum_of_neighbors(list_random)}')
