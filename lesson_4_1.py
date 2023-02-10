# Вывести первые N цисел кратные M и больше K

n = int(input('Enter N: '))
m = int(input('Enter M: '))
k = int(input('Enter K: '))
number_of_iterations = 0
while True:
    if k % m == 0:
        if number_of_iterations != n:
            print(k)
            number_of_iterations += 1
    k += 1
