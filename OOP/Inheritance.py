

#Parent class/ Super class/ Base Class
class Phone:

    def call(self):
        print("Can Call")
    def message(self):
        print("Can Message")



#Child class/  Sub class/ Derived class
class SmartPhone(Phone):                              #this is inheritaning Phone to SmartPhone
    #call() + message()
    def camera(self):
        print("Can take photo")



S1 =SmartPhone()
S1.call()
S1.message()
S1.camera()


#exercise
print("\nexercise >>>\n")

class Shape:
    dim1 = ""
    dim2 = ""
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2


class Traingle(Shape):

    def Area(self):
        res = 0.5 * self.dim1 * self.dim2
        print("Area of traingle: ", res)

class Rectangle(Shape):                                         #HIERARCHICAL INHERITANCE

    def Area(self):
        res = self.dim1 * self.dim2
        print("Area of rectangle: ", res)

t1 = Traingle(20, 30)
t1.Area()

r1 = Rectangle(20, 30)
r1.Area()

#type of inheritance-- Hierarchical ,Multi-lvl,  Multiple
print("\nMulti-level inh>>>>>>>>>>>\n")

class A:
    def display1(self):
        print("it is class A")
class B(A):
    #here have display1()
    def display2(self):
        super().display1()
        print("it is class B")
class C(B):
    # here have display1() and display2()
    def display3(self):
        super().display1()
        super().display2()
        print("it is class C")

obj1 = C()
obj1.display1()
print("\n")
obj1.display2()
print("\n")
obj1.display3()

print("\nMultiple inh>>>>>>>>>>>\n")

class X:
    def dis1(self):
        print("it is class X")

class Y:
    def dis2(self):
        print("it is class Y")

class Z(X,Y):
    def dis3(self):
        print("it is class Z")

obj2 = Z()
obj2.dis1()