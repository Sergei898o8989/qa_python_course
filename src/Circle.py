from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self._perimeter = 2 * 3.14 * r
        self._area = 3.14 * r ** 2
