# Сделайте так, чтобы число секунд отображалось в виде дни: часы: минуты: секунды:
try:
    number = int(input('Enter number: '))
    remainder_of_second = number % 60
    minute = (number - remainder_of_second) / 60
    remainder_of_minute = minute % 60
    hour = (minute - remainder_of_minute) / 60
    remainder_of_hour = hour % 24
    day = (hour - remainder_of_hour) / 24
    remainder_of_day = day % 12
    print(f'{int(remainder_of_day)} day: '
          f'{int(remainder_of_hour)} hour: '
          f'{int(remainder_of_minute)} minute: '
          f'{int(remainder_of_second)} second')
except ValueError as e:
    print('Invalid value')
