# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


list_types = [77, 'hello', 45, 54, 'world', 4.4, None]


def different_type(any_types):
    a = []
    for i in any_types:
        if isinstance(i, str):
            a.append(i)
    return a


print(different_type(list_types))
