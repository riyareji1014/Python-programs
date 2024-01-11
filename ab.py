from abc import ABC,abstractmethod

class Shape(ABC):
    def area(self):
        print("calculating the areas")
class Circles(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("the area of the circe is",3.14*self.r*self.r)
class Square(Shape):
    def __init__(self,s):
        self.s=s 
    def area(self): 
        print("the area of the square:",self.s**2) 
c=Circles(6)
s=Square(4)
c.area()
s.area()                             
