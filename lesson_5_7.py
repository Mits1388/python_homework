# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
import random

list_random = [random.randint(0, 5) for i in range(0, 5)]

print(f'Random list: {list_random}')
a = []
for i in range(len(list_random)):
    if i != len(list_random)-1:
        a.append(list_random[i+1]+list_random[i-1])
    else:
        a.append(list_random[i-1]+list_random[0])

print(f'Sum of neighboring elements: {a}')
