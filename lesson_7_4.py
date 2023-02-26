# 4. Изменить класс Category из задачи 3, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
categories = {
    0: {'name': 'bus', 'is_published': False},
    1: {'name': 'sports', 'is_published': False},
    2: {'name': 'electric', 'is_published': True},
    3: {'name': 'truck', 'is_published': False},
    4: {'name': 'ambulance', 'is_published': True}
}


class Category:
    def __init__(self):
        # print('init')
        self.categories = categories

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
                    return f'index {self.categories.index(category_car)}'





#
#     def get(self, index):
#         for i in self.categories:
#             if self.categories.index(i) == index:
#                 return i
#         else:
#             raise IndexError('No such index in the list')
#
#     def delete(self, index):
#         for i in self.categories:
#             if self.categories.index(i) == index:
#                 self.categories.remove(i)
#
#     def update(self, index, new_category):
#         for i in self.categories:
#             if i == new_category:
#                 raise ValueError('There is a category in the list')
#             else:
#                 if new_category in self.categories:
#                     continue
#                 else:
#                     self.categories.insert(index, new_category)
#                     return self.categories
#
#     # 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение ключа is_published на
#     # True, если такого индекса нет, вызвать исключение IndexError
#     def make_published(self, index):
#         return self.categories
#
#     # 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий значение ключа is_published
#     # на False, если такого индекса нет, вызвать исключение IndexError
#     def make_unpublished(self, index):
#         return self.categories
#
#
# category = Category()
# print(f'Method of adding - {category.add("car")}')
# print(f'Method of getting - {category.get(5)}')
# print(f'Before deleting the index - {category.categories}')
# category.delete(4)
# print(f'After deleting the index - {category.categories}')
# print(f'After updating - {category.update(2, "taxi")}')
