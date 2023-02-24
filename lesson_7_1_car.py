# 1. Написать класс Car Конструктор класса принимает атрибуты: color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест) is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на вход)
class Car:
    color: str
    count_passenger_seats: int
    is_baby_seat: bool
    is_busy: bool

    def __init__(self, color, count_passenger_seats, is_baby_seat, is_busy):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = is_busy

# 1.1 Написать магический метод __str__ выводящий форматированную строку c информацией об автомобиле
    def __str__(self):
        return f'Car {self.color = }; {self.count_passenger_seats = }; ' \
               f'{self.is_baby_seat = }; {self.is_busy = }'


bmw = Car('white', 2, False, True)

print(bmw.__str__())
