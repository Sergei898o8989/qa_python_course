from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self._perimeter = a + b + c
        p = self._perimeter / 2
        self._area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
