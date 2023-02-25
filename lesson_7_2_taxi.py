# 2. Написать класс Taxi Конструктор класса принимает атрибуты: cars: list[Car] (список экземпляров класса Car)
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

    def __str__(self):
        return f'Car {self.color}, passenger seat {self.count_passenger_seats}, ' \
               f'baby seat {self.is_baby_seat}, busy {self.is_busy}'


bmw = Car('red', 2, True, False)
audi = Car('black', 4, False, False)
volvo = Car('white', 4, True, False)
mazda = Car('blue', 4, True, False)

cars = [bmw, audi, volvo, mazda]


class Taxi:

    def __init__(self):
        # print('init')
        self.cars = cars

    # 2.1 Реализовать метод find_car На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
    # наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)На основании данных,
    # вернуть объект Car из атрибута cars подходящий по параметрам исвободный (is_busy = False),
    # у автомобиля сменить атрибут is_busy на значение True, если подходящего автомобиля нет, метод должен возвращать None
    def find_car(self, count_passengers, is_baby):
        # print('find_car')
        for i in self.cars:
            if count_passengers + is_baby <= i.count_passenger_seats and i.is_baby_seat:
                if not i.is_busy:
                    i.is_busy = True
                    # return i.color, i.count_passenger_seats, i.is_baby_seat, i.is_busy
                    return i


taxi = Taxi()
print(taxi.find_car(2, True))
