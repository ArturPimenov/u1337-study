class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Малышка'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'Без цвета. Покрась меня.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return 'Цвет ' + self.make + ' ' + self.model + ' теперь ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return self.make + ' ' + self.model + ' не может ехать!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' делает врум-врум!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Количество бензина в '+self.make + ' ' + self.model + ': ' + str(self.gas)


class MonsterTruck(Car):
    size = 'Монстр'

    def rev(self):
        print('ДРЫН-ДЫН-ДЫН! Этот монстр-трак просто огромный!')

    def drive(self):
        self.rev()
        return Car.drive(self)