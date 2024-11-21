
import math


class GeometricFigure:
    
    def CalculationArea(self):
        raise NotImplementedError("Error")
    
class Rectangle(GeometricFigure):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def CalculationArea(self):
        return self.width * self.height
    
class Circle(GeometricFigure):
    
    def __init__(self, radius):
        self.radius = radius
        
    def CalculationArea(self):
        return math.pi * (self.radius ** 2)

class Rhombus(GeometricFigure):
    
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        
    def CalculationArea(self):
        return (self.diagonal1 * self.diagonal2) / 2

    
rectangle = Rectangle(7, 5)
print("Area rectangle:", rectangle.CalculationArea())
    
circle = Circle(8)
print("Area circle:", circle.CalculationArea())
    
rhombus = Rhombus(5, 8)
print("Area rhombus:", rhombus.CalculationArea())
    
