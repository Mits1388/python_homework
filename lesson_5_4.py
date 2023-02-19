# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


list_different_types = [77, 'hello', 45, 54, 'world', 4.4, None]


def is_type(list_any_types):
    a = []
    for i in list_any_types:
        if isinstance(i, str):
            a.append(i)
    return a


print(is_type(list_different_types))
