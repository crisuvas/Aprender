class RegularFigure:
    def __init__(self, base, high):
        self.base = base
        self.high = high


class Triangle(RegularFigure):
    def __init__(self, base, high):
        super().__init__(base, high)
        self.__area = 0

    def calculate_area(self):
        self.__area = self.base * self.high / 2

    def show_area(self):
        return self.__area


class Rectangle(RegularFigure):
    def __init__(self, base, high):
        super().__init__(base, high)
        self.__area = 0

    def calculate_area(self):
        self.__area = self.base * self.high
        
    def show_area(self):
        return self.__area


tiny_triangle = Triangle(9, 2)
tiny_rectangle = Rectangle(4, 4)
tiny_triangle.calculate_area()
tiny_rectangle.calculate_area()
print(tiny_triangle.show_area())
print(tiny_rectangle.show_area())
