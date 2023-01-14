class Figure:
    def __init__(self, name):
        self.name = name
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Input is not a geometric figure")
        return self.area + figure.area
