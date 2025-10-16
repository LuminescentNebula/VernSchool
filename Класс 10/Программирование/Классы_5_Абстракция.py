import math

# В Python для создания абстрактного класса необходимо импортировать библиотеку ABC
from abc import ABC,abstractmethod
# Примеры как абстрактный класс объявляется других языках, которые больше ориентированны на ООП:
#C#: abstract class GeometricFigure
#Java: abstract class GeometricFigure

#Python
class GeometricFigure(ABC):
    pass

class Flat(GeometricFigure, ABC):
    @abstractmethod
    def area(self): pass

class Rectangle(Flat):
    def __init__(self,width,height):
        self.__width=width
        self.__height=height
    def area(self):
        return self.__width * self.__height

class Circle(Flat):
    def __init__(self,radius):
        self.__radius=radius
    def area(self):
        return math.pi*self.__radius * self.__radius

class Volumetric(ABC):
    @abstractmethod
    def volume(self): pass

class Cylinder(Volumetric):
    def __init__(self,radius,height):
        self.__radius=radius
        self.__height=height
    def volume(self):
        return math.pi*self.__radius * self.__radius*self.__height

