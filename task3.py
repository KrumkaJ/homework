class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return f'Результат {self.number * "*"}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if (self.number - other.number) > 0:
            return Cell(self.number - other.number)
        else:
            print('Отрицательное количество')

    def __mul__(self, other):
        return Cell(int(self.number * other.number))

    def __truediv__(self, other):
        return Cell(round(self.number // other.number))

    def make_order(self, cells):
        row = ''
        for i in range(int(self.number / cells)):
            row += f'{"*" * cells}\\n'
        row += f'{"*" * (self.number % cells)}'
        return row


cell_1 = Cell(28)
cell_2 = Cell(15)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2.make_order(6))
print(cell_1.make_order(10))
