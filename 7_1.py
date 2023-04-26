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

kos = Car('красная', 4, True)

print(kos)
