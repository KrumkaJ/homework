class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat(self):
        return self.v / 6.5 + 0.5

    def costume(self):
        return self.h * 2 + 0.3

    @property
    def cloth(self):
        return str(f'Расход ткани: {round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3))}')


class Coat(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.cloth_coat = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани для пальто: {self.cloth_coat}'


class Costume(Clothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.cloth_costume = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани для костюма: {self.cloth_costume}'


coat = Coat(38, 1.76)
costume = Costume(38, 1.76)
print(coat)
print(costume)
print(coat.cloth)
