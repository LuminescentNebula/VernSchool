import math
#Абстракция - принцип ООП, который заключается в выделении общих характеристик и свойств объектов, игнорируя при этом второстепенные детали реализации.

#Абстрактный класс - класс, который описывает общие свойства для классов наследников.
#Абстрактный класс только описывает, у него не может быть реализации, то есть нельзя создать объекты абстрактного класса
#Абстрактный метод - метод, который может быть описан в абстрактном классе. У абстрактного методы нет собственной реализации. Дочернии классы обязаны переопределить абстрактный метод и реализовать его логику.

# В Python для создания абстрактного класса необходимо импортировать библиотеку ABC
from abc import ABC,abstractmethod
# Примеры как абстрактный класс объявляется других языках, которые больше ориентированны на ООП:
#C#: abstract class GeometricFigure
#Java: abstract class GeometricFigure

#Python
#Абстрактный класс создается так
class GeometricFigure(ABC):
    #В абстрактном классе описываются свойства для наследников

    #Поля можно объявлять не только в конструкторе, но и так:
    name: str

#Так указывается двойное наследование.
#Этот класс является и абстрактным, и наследником GeometricFigure
class Flat(GeometricFigure, ABC):
    #В абстрактном методе могут быть уже реализованные методы (с логикой), которые унаследуются наследниками
    def get_type(self) -> str:
        return "Flat"
    #Так и абстрактные методы, у которых нет реализации. Наследники этот метод тоже унаследуют, но будут обязаны переопределить его
    #С помощью аннотации "@abstractmethod" указывается абстрактный метод
    @abstractmethod
    def area(self) -> float: 
        pass


# Класс Rectangle наследуется от абстрактного класса Flat
class Rectangle(Flat):
    def __init__(self,width:int,height:int):
        self.__width:int =width
        self.__height:int =height
    #Если бы мы не переопределили абстрактный метод, то была бы ошибка
    def area(self) -> float:
        return self.__width * self.__height

class Circle(Flat):
    def __init__(self,radius:int):
        self.__radius:int=radius
    def area(self) -> float:
        return math.pi*self.__radius * self.__radius

class Volumetric(ABC):
    @abstractmethod
    def volume(self) -> float: 
        pass

class Cylinder(Volumetric):
    def __init__(self,radius:int,height:int):
        self.__radius:int=radius
        self.__height:int=height
    def volume(self) -> float:
        return math.pi*self.__radius * self.__radius*self.__height

