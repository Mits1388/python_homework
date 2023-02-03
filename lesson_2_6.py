# Вводится строка с клавиатуры (input),
# состоящая минимум из 3х слов, с помощью методов поиска, срезов и конкатенации,
# необходимо поменять местами первое и последнее слово в строке
text = input('Enter three words: ')
t = text.find(' ')
e = text.rfind(' ')+1
first_word = text[:t]
second_word = text[e:]
third_word = text[t:e]
print(f'{second_word}{third_word}{first_word}')



