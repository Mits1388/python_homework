# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input('Enter string: ')
number_of_letters = {i: text.count(i) for i in text}
print(number_of_letters)
