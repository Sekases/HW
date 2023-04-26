class Car:
    def __init__(self, color: str, count_pass_seats: int, is_baby_seats: bool):
        self.color = color
        self.count_pass_seats = count_pass_seats
        self.is_baby_seats = is_baby_seats
        self.busy = False

    def __str__(self):
        if self.is_baby_seats:
            flag = 'есть'
        else:
            flag = 'нет'
        return f'Эта машина {self.color}, в ней {self.count_pass_seats} сидения и в ней {flag} детское сидение'



class Taxi:
    def __init__(self, cars):
        self.cars = cars

    def find_car(self, count_pass, is_baby):
        for car in self.cars:
            if (car.count_passenger_seats >= count_pass) and (car.is_baby_seat == is_baby) and (not car.is_busy):
                car.is_busy = True
                return car
        return None



