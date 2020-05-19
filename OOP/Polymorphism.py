
#bohorup/polymorphism of len()  {built in function}
print(len("Hasibur Rahman"))
print(len([1, 3, 5, 2]))

#user function
def add(x, y, z=0):
    return x+y+z

print(add(2, 4))
print(add(2, 4, 4))


#another excercise

class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate(self):                      #now this is used 2 times with diff purpose so polymorphism is
        pass

class Triangle(Shape):
    def calculate(self):
        res = 0.5 * int(self.base) * int(self.height)
        print(res)

class GenArea(Shape):
    def calculate(self):
        ans = self.base * self.height
        print(ans)

t1 = Triangle(10, 20)
t1.calculate()

G2 = GenArea(20, 30)
G2.calculate()