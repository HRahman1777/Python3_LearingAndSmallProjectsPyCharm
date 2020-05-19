
class Student:                                                 #class
    roll = ""
    gpa = ""
    def display(self):                                         #method
        print(f"Student ID: {self.roll}\nCGPA: {self.gpa}\n")

Hasibur = Student()                                            #object
print(isinstance(Hasibur, Student))

Hasibur.roll = 181151777
Hasibur.gpa = 3.5

Hasibur.display()

Rahman = Student()                                             #object
Rahman.roll = 1777
Rahman.gpa = 3.5
Rahman.display()

#excer 2
print("excer>>> 2")
class Info:                                                      #class
    name = ""
    id = ""
    def setValue(self, name, id):                                #method
        self.name = name
        self.id = id

    def display(self):                                           #method
        print(f"Student ID: {self.name}\nCGPA: {self.id}\n")

Data1 = Info()                                                    #object
Data1.setValue("HasiburRahman", 181151777)
Data1.display()


#Method OverWriting (in inheritance)
print("\nMethod OverWriting>>>>>>\n")

class Phone:
    def __init__(self):
        print("This is phone class")

class SmartPhone(Phone):
    def __init__(self):                               #already have init method by inheritace, and over-written
        super().__init__()
        print("This is smartphone class")

obj1 = SmartPhone()