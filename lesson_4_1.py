# Вывести первые N цисел кратные M и больше K

m = int(input('Enter M: '))
k = int(input('Enter K: '))
for i in range(1, k + 1):
    if i % m == 0:
        print(i)
