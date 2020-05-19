
val = input("Write proper sentence here for count: ")

digit = 0
alp = 0
ex = 0
word = val.count(" ")                                        #count()

for i in val:
    if (i>="A" and i<="Z") or (i>="a" and i<="z"):
        alp=alp+1
#    elif i == " ":
#        word = word+1
    elif (i>="1" and i<="9") or i == "0":
        digit=digit+1
    else:
        ex = ex+1

ex = ex - word

print("Word: ", word+1)
print("Number Digit: ", digit)
print("Total Alphabet : ", alp)
print("Extra: ", ex)