class Person:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    #Альтернативный вариант создания геттеров и сеттеров с помощью свойств (property)

    #Аннотации начинаются с @
    #Мы объявляем свойство с помощью аннтации "@property"
    #указывая что мы "как-бы" создаем открытое поле name,
    #но получение и изменение которого будет работать через указанные нами геттеры и сеттеры
    @property
    def name(self):
        print("Был вызван геттер")
        return self.__name

    #Сеттер
    @name.setter
    def name(self,name):
        print("Был вызван сеттер")
        self.__name=name
        
    def print_person(self):
        print(self.__name, self.age)

tom = Person("Tom", 16)
#Теперь мы снова можем просто обращаться к name через точку
#Но при этом будет работать геттер
print(tom.name)
#или сеттер, если мы изменяем значение поле
tom.name="Thomas"
tom.print_person()
