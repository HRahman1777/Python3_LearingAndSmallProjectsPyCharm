from  abc import ABC, abstractmethod


class Shape(ABC):                         #it became abstract class
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @abstractmethod
    def calculate(self):         #now this is abstract method
        pass

class Triangle(Shape):                      #this class should use abstract method becoz it inherite a abstract class
    def calculate(self):
        res = 0.5 * int(self.base) * int(self.height)
        print(res)

t1 = Triangle(10, 20)
t1.calculate()

t2 = Triangle(20, 30)
t2.calculate()