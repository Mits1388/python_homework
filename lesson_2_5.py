# Вводится строка с клавиатуры (input), необходимо подсчитать количество слов в данной строке
text = input('Enter string: ')
list_split = text.split(' ')
words_count = len(list_split)
print(words_count)
