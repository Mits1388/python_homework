# Вводится слово, вывести True если слово является палиндромом (читается справа налево как слева направо), False в противном случае
word = input('Enter word: ')
if word[:] == word[::-1]:
    print('True')
else:
    print('False')

