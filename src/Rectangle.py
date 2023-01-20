from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._perimeter = 2 * (a + b)
        self._area = a * b
