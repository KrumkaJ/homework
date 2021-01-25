class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return '\n'.join([' '.join([str(el) for el in line]) for line in self.numbers])

    def __add__(self, other):
        result = []
        for sublist in zip(self.numbers, other.numbers):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return '\n'.join([' '.join([str(el) for el in line]) for line in result])


matrix_1 = Matrix([[4, 10, 32, 45], [5, 16, 22, 9], [36, 17, 4, 8], [87, 46, 13, 73]])
matrix_2 = Matrix([[5, 7, 8, 45], [35, 74, 8, 21], [57, 50, 43, 10], [7, 34, 6, 9]])
print(matrix_1)
print(Matrix.__add__(matrix_1, matrix_2))
