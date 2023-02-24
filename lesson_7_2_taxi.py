# 2. Написать класс Taxi Конструктор класса принимает атрибуты: cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)На основании данных,
# вернуть объект Car из атрибута cars подходящий по параметрам исвободный (is_busy = False),
# у автомобиля сменить атрибут is_busy на значение True, если подходящего автомобиля нет, метод должен возвращать None

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
        return f'Car {self.color = }; {self.count_passenger_seats = }; ' \
               f'{self.is_baby_seat = }; {self.is_busy = }'


class Taxi:

    def __init__(self):
        self.cars = []

    def __str__(self):
        i = 0
        while i != len(taxi.cars):
            print(f'{self.cars[i]}')
            i += 1

    def add_car(self, car):
        self.cars.append(car)


bmw = Car('red', 2, True, True)
mazda = Car('white', 4, False, False)

taxi = Taxi()
taxi.add_car(bmw)
taxi.add_car(mazda)

taxi.__str__()
