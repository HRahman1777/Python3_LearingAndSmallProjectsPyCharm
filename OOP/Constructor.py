class Info:                                                      #class
    name = ""
    id = ""
    def __init__(self, name, id):                                #constructor
        self.name = name
        self.id = id

    def display(self):                                           #method
        print(f"Student ID: {self.name}\nCGPA: {self.id}\n")

Data1 = Info("HasiburRahman", 181151777)                                                    #object
Data1.display()

#exercise
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate(self):
        res = 0.5*int(self.base)*int(self.height)
        print(res)

t1 = Triangle(10, 20)
t1.calculate()

t2 = Triangle(20, 30)
t2.calculate()