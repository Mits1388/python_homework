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


class Taxi(Car):
    cars = []

    def __init__(self, color, count_passenger_seats, is_baby_seat, is_busy):
        super().__init__(color, count_passenger_seats, is_baby_seat, is_busy)
        Taxi.cars.append(self)

    def __str__(self):
        return "{} {} {} {}".format(self.color, self.count_passenger_seats, self.is_baby_seat, self.is_busy)


bmw = Taxi('red', 2, True, True)
audi = Taxi('white', 4, False, True)
mazda = Taxi('black', 4, True, False)
volvo = Taxi('blue', 4, False, False)

for i in Taxi.cars:
    print(i)
