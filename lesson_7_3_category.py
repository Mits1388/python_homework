# 3. Реализовать класс Category. Создать атрибут класса categories
categories = ['bus', 'sports', 'electric', 'truck', 'ambulance']


class Category:

    def __init__(self):
        # print('init')
        self.categories = categories

    # 3.1 Написать метод класса add принимающий на вход название категории, если такой категории в атрибуте класса
    # categories нет, добавить данную категорию в список и вернуть индекс вхождения новой категории в списке.
    # Если такая категория уже есть, вызвать исключение ValueError
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

    # 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка категорий на этом индексе,
    # если нет элемента на таком индексе, вызвать исключение IndexError
    def get(self, index):
        for i in self.categories:
            if self.categories.index(i) == index:
                return i
        else:
            raise IndexError('No such index in the list')

    # 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и удаляющий элемент из
    # списка категорий на этом индексе, если нет элемента на таком индексе, ничего не делать,
    # метод ничего возвращать не должен
    def delete(self, index):
        for i in self.categories:
            if self.categories.index(i) == index:
                self.categories.remove(i)

    # 3.4 Написать метод класса update принимающий индекс категорий и новое название категории, если нет элемента
    # на таком индексе, то новая категория должна добавляться с учетом того, что имена категорий уникальны,
    # если новое имя категории нарушает уникальность в списке категорий, вызвать исключение ValueError
    def update(self, index, new_category):
        for i in self.categories:
            if i == new_category:
                raise ValueError('There is a category in the list')
            else:
                if new_category in self.categories:
                    continue
                else:
                    self.categories.insert(index, new_category)
                    return self.categories


category = Category()
print(f'Method of adding - {category.add("car")}')
print(f'Method of getting - {category.get(5)}')
print(f'Before deleting the index - {category.categories}')
category.delete(4)
print(f'After deleting the index - {category.categories}')
print(f'After updating - {category.update(2, "taxi")}')

