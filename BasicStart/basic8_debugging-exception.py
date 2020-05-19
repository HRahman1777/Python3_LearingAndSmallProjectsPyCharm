



def addi(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

res = addi(1, 2, 3, 4)
print(res)


#exception >>>>>>>>>

try:
    list = [0, 1, 2, 4]
    res = list[3]/list[0]
    print(res)
except ZeroDivisionError:
    print("Under zero divition error")
except IndexError:
    print("Under indixing error")
except (ValueError, FloatingPointError):    #use multiple error
    print("Find error")
finally:
    print("if find expection, under finally will must continue work")

#another
def per(x, y):
    if y<1:
        raise ValueError("Enter bigger than zero")
    return x/y

try:
    print(per(4, 2))
    print(per(4, 0))
except ValueError as e:
    print(e)






