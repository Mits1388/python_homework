# 4. Изменить класс Category из задачи 3, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей

# dict_categories = {
#     0: {'name': 'bus', 'is_published': True},
#     1: {'name': 'sports', 'is_published': True},
#     2: {'name': 'electric', 'is_published': False},
#     3: {'name': 'truck', 'is_published': False},
#     4: {'name': 'ambulance', 'is_published': True}
# }


class Category:
    dict_categories = {
        0: {'name': 'bus', 'is_published': True},
        1: {'name': 'sports', 'is_published': True},
        2: {'name': 'electric', 'is_published': False},
        3: {'name': 'truck', 'is_published': False},
        4: {'name': 'ambulance', 'is_published': True}
    }

    # def __init__(self):
    #     self.dict_categories = dict_categories

    def add(self, category_car, is_published):
        for i, j in self.dict_categories.items():
            if category_car == j['name']:
                raise ValueError('There is a category in the list')
            else:
                if i == len(self.dict_categories) - 1:
                    self.dict_categories[i + 1] = dict(name=category_car, is_published=is_published)
                    return f'index {len(self.dict_categories.keys()) - 1}'
                else:
                    continue

    def get(self, index):
        for i, j in self.dict_categories.items():
            if i == index:
                return j['name']
        else:
            raise IndexError('No such index in the list')

    def delete(self, index):
        for i, j in list(self.dict_categories.items()):
            if i == index:
                del self.dict_categories[i]

    def update(self, index, new_category):
        for i, j in self.dict_categories.items():
            if new_category == j['name']:
                raise ValueError('There is a category in the list')
            else:
                if new_category in self.dict_categories:
                    continue
                else:
                    self.dict_categories[index] = dict(name=new_category, is_published=False)
                    return self.dict_categories

    # 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
    # ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
    def make_published(self, index):
        for i, j in self.dict_categories.items():
            if index > len(self.dict_categories):
                raise IndexError('There is an index in the list')
            else:
                if i == index:
                    if not j['is_published']:
                        j['is_published'] = True

    # 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
    # значение ключа is_published на False, если такого индекса нет, вызвать исключение IndexError
    def make_unpublished(self, index):
        for i, j in self.dict_categories.items():
            if index > len(self.dict_categories):
                raise IndexError('There is an index in the list')
            else:
                if i == index:
                    if j['is_published']:
                        j['is_published'] = False


category = Category()
print(f'Method of adding - {category.add("car", True)}')
print(f'Method of getting - {category.get(5)}')
print(f'Before deleting the index - {category.dict_categories}')
category.delete(3)
print(f'After deleting the index - {category.dict_categories}')
print(f'After updating - {category.update(3, "taxi")}')
category.make_published(2)
print(f'After published - {category.dict_categories}')
category.make_unpublished(2)
print(f'After unpublished - {category.dict_categories}')
