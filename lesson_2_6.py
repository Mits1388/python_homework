# Вводится строка с клавиатуры (input),
# состоящая минимум из 3х слов, с помощью методов поиска, срезов и конкатенации,
# необходимо поменять местами первое и последнее слово в строке
text = input('Enter three words: ')
end_position = text.find(' ')
# print(end_position)
start_position = text.rfind(' ') + 1
# print(start_position)
first_word = text[:end_position]
second_word = text[start_position:]
third_word = text[end_position:start_position]
print(f'{second_word}{third_word}{first_word}')
