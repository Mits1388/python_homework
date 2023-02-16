# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


list_different_types = [77, 'hello', 45, 54, 'world', 4.4, None]

list_string = filter(lambda i: type(i) is str, list_different_types)
print(list(list_string))

