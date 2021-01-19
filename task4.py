class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'The car went'

    def stop(self):
        return 'The car has stopped'

    def turn(self, direction):
        return 'The car turned to ' + direction

    def show_speed(self):
        print(f'Current speed of car {self.name} is {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    pass


hyundai = TownCar(50, 'gray', 'hyundai', False)
bmw = SportCar(250, 'red', 'bmw', False)
volkswagen = WorkCar(70, 'black', 'volkswagen', False)
ford = PoliceCar(100, 'blue', 'ford', True)

print(bmw.turn('left'), ',', bmw.go(), ',', bmw.turn('right'), ',', bmw.stop())
print(hyundai.show_speed())
print(volkswagen.show_speed())
print(f'{hyundai.name} is {hyundai.color}')
print(f'Is {ford.name} a police car? {ford.is_police}')
print(f'Is {hyundai.name} a police car? {hyundai.is_police}')
print(bmw.speed)
