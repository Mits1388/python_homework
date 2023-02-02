#Пользователь вводит 3 числа, найти среднее арифмитическое с точностью 3
first_numder = input("Enter first numder: ")
second_number = input("Enter second numder: ")
third_number = input("Enter third numder: ")

sum_of_numbers = int(first_numder)+int(second_number)+int(third_number)
average = sum_of_numbers/3

print("Average: ", round(average, 3))