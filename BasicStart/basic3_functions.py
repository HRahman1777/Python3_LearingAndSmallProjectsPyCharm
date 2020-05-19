from math import *

print("max ", max(10, 30, 20))
print("min ", min(10, 30, 20))
print("abs ", abs(-5))
print("power ", pow(2,3))
print("sqrt ", sqrt(25))
print("round ", round(3.2))
print(round(3.5))
print(round(3.7))

print("floor ", floor(3.7))
print("ceil ", ceil(3.7))

val = "Haisbur Rahman 181"                                        #count()
print(val.count("a"))

#math import  c > https://www.programiz.com/python-programming/modules/math
'''
ceil(x)	Returns the smallest integer greater than or equal to x.
copysign(x, y)	Returns x with the sign of y
fabs(x)	Returns the absolute value of x
factorial(x)	Returns the factorial of x
floor(x)	Returns the largest integer less than or equal to x
fmod(x, y)	Returns the remainder when x is divided by y
frexp(x)	Returns the mantissa and exponent of x as the pair (m, e)
fsum(iterable)	Returns an accurate floating point sum of values in the iterable
isfinite(x)	Returns True if x is neither an infinity nor a NaN (Not a Number)
isinf(x)	Returns True if x is a positive or negative infinity
isnan(x)	Returns True if x is a NaN
ldexp(x, i)	Returns x * (2**i)
modf(x)	Returns the fractional and integer parts of x
trunc(x)	Returns the truncated integer value of x
exp(x)	Returns e**x
expm1(x)	Returns e**x - 1
log(x[, base])	Returns the logarithm of x to the base (defaults to e)
log1p(x)	Returns the natural logarithm of 1+x
log2(x)	Returns the base-2 logarithm of x
log10(x)	Returns the base-10 logarithm of x
pow(x, y)	Returns x raised to the power y
sqrt(x)	Returns the square root of x
acos(x)	Returns the arc cosine of x
asin(x)	Returns the arc sine of x
atan(x)	Returns the arc tangent of x
atan2(y, x)	Returns atan(y / x)
cos(x)	Returns the cosine of x
hypot(x, y)	Returns the Euclidean norm, sqrt(x*x + y*y)
sin(x)	Returns the sine of x
tan(x)	Returns the tangent of x
degrees(x)	Converts angle x from radians to degrees
radians(x)	Converts angle x from degrees to radians
acosh(x)	Returns the inverse hyperbolic cosine of x
asinh(x)	Returns the inverse hyperbolic sine of x
atanh(x)	Returns the inverse hyperbolic tangent of x
cosh(x)	Returns the hyperbolic cosine of x
sinh(x)	Returns the hyperbolic cosine of x
tanh(x)	Returns the hyperbolic tangent of x
erf(x)	Returns the error function at x
erfc(x)	Returns the complementary error function at x
gamma(x)	Returns the Gamma function at x
lgamma(x)	Returns the natural logarithm of the absolute value of the Gamma function at x
pi	Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)
e	mathematical constant e (2.71828...)
'''

#user define functions >>>>>>>>>>>>>>>
print("User define functions start>>>>\n")
def add(a, b):
    sum = a+b
    print(sum)

def substraction(a, b):
    sub = a-b
    return sub

add(3, 5)

res = substraction(10, 3)
print(res)


def multi(a, b):
    into = a*b
    return into
print(multi(2,3))
newMulti = multi                           #duplicating function to another variable
print(newMulti(2, 3))

def fact(n):
    if n==1:
        return 1
    else:
        return n* fact(n-1)

print(fact(3))

#xargs >>>>>>>>>>>
print("xargs>>>>\n")
def student(*all):
    print(all[0])
    print(all[1])
    print(all)
                                                  #tuples
student("Hasibur", 3.5, "CSE")


def addi(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum)

addi(1, 2, 3, 4)
addi(10, 50)


#xxargs >>>>>>>>>>>
print("xxargs>>>>\n")
def students(**details):
    print(details["id"])
    print(details)
                                                           #dict
students(id = "181-15-1777", name = 'Hasibur', cg = 3.5)

#lambda function >>>>>>>>>>>>>>
print("lambda functions start>>>>\n")
result = (lambda a, b : a+b)(2, 3)
print(result)


#map >>>>>>>>>>>>>>>
print("map functions start>>>>\n")
numbers = [1, 2, 3, 4, 5, 6]

def square(a):
    return a*a

ans = list(map(square, numbers))       #function with itteatiable object like list

print(ans)

#filter function >>>>>>>>>>>>>>>>
print("filter functions start>>>>\n")
filterans = list(filter(lambda a: a==1, numbers))
filterans2 = list(filter(lambda a: a%2==0, numbers))
print(filterans)
print(filterans2)


#comprehensive function >>>>>>>>>>
print("comprehensive functions start>>>>\n")
num = [1, 2, 3, 4]
result = [a*a for a in num]
print(result)

result = [a for a in num if a%2==0]
print(result)

#zip functions >>>>>>>>>>>>>>>>>>>>
print("ZIP functions start>>>>\n")
roll = [1777, 1793, 1839, 1920, 1832]
name = ['Hasibur', 'Naim', 'Emtiyaz', 'Nabid']

resList = list(zip(roll, name))
print(resList)                                       #result showing list inside many tuples

resList = list(zip(roll, name, "12345"))
print(resList)
