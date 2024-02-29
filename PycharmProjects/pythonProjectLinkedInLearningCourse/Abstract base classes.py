from abc import ABC, abstractmethod
class GraphicShape:
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        return self.side * self.side

circle = Circle(10)
square = Square(4)
print(circle.calcArea())
print(square.calcArea())