# Вывести первые N цисел кратные M и больше K

# m = int(input('Enter M: '))
# k = int(input('Enter K: '))
# for i in range(1, k + 1):
#     if i % m == 0:
#         print(i)
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
