# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
import random

list_random = [random.randint(0, 100) for i in range(0, 10)]
print(list_random)


def is_sorted(any_list):
    a = []
    b = []
    for i in range(len(any_list)):
        if any_list[i] % 2 == 0:
            a.append(any_list[i])
        else:
            b.append(any_list[i])
    return sorted(a) + sorted(b)


print(is_sorted(list_random))
