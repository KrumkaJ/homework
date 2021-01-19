class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self._weigth = 25
        self._tickness = 5

    def result(self):
        result = self._length * self._width * self._weigth * self._tickness / 1000
        print(f'Для покрытия всего дорожного полотна нужно {result} т асфальта')


asphalt = Road(7000, 15)
asphalt.result()
