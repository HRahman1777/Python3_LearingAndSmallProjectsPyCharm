

def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y
def rem(x, y):
    return x%y

while(True):

    try:
        num1 = float(input("New:\n"))
        sign = input("")
        num2 = float(input(""))

        if sign == "+":
            print(add(num1, num2))
        elif sign == "-":
            print(sub(num1, num2))
        elif sign == "*":
            print(mul(num1, num2))
        elif sign == "/":
            print(div(num1, num2))
        elif sign == "%":
            print(rem(num1, num2))
    except (ValueError,ZeroDivisionError, FloatingPointError, IndexError, EOFError) as e:
        print("\n", e, "\n")
    finally:
        b = input("Do you want to do calculate again? yes/no")
        if b == "No" or b == "no" or b == "N" or b == "n":
            print("\n>>>Closed<<<\n")
            break;

