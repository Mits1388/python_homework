# 3. Реализовать класс Category. Создать атрибут класса categories
categories = ['bus', 'sports', 'electric', 'truck']


class Category:

    def __init__(self):
        # print('init')
        self.categories = categories

# 3.1 Написать метод класса add принимающий на вход название категории, если такой категории в атрибуте класса categories
# нет, добавить данную категорию в список и вернуть индекс вхождения новой категории в списке.Если такая категория уже
# есть, вызвать исключение ValueError
    def add(self, category_car):
        # print('add_categories')
        for i in self.categories:
            if i == category_car:
                raise ValueError('There is a category in the list')
            else:
                if category_car in self.categories:
                    continue
                else:
                    self.categories.append(category_car)
                    return self.categories


category = Category()
print(category.add('buss'))

# print(category.categories)

# cat = Category()
# Category.add_categories('Bus')


# else:
#     try:
#     except ValueError as e:
#         print('ValueError exception')


# def get_categories(self):
#
#
# def delete_categories(self):
#
# def update(self):
