
class Bike:
    def __init__(self, name, color):            #magic mathod
        self.name = name
        self.color = color

    def __eq__(self, other):                  #magic method
        return self.name == other.name and self.color == other.color

    def __str__(self):                         #magic mathod
        return print(f"(str)>Name: {self.name}\t Color: {self.color}")

    def dis(self):
        print(f"(dis)>Name: {self.name}\t Color: {self.color}")

b1 = Bike("Ya", "Blue")
b1.dis()
b1.__str__()

b2 = Bike("Ya", "Blue")
print(b1 == b2)

#some magic methods
"""
    def __eq__(self, other):  ==
    def __ne__(self, other):  !=
    def __lt__(self, other):  <
    def __gt__(self, other):  >
    def __le__(self, other):  <=
    def __ge__(self, other):  >=
"""


#Regular expression >>>>>>>>>>>>>>>>>>>>
print("\n#Regular expression >>>>>>>>>>>>>\n")

import re
patrn = r"co"
#match()
if re.match(patrn, "this is red color, company"):   #only start string is process for match
    print("Matched 1")
if re.match(patrn, "color is red, company"):        #match()
    print("Matched 2")
else:
    print("Not Matched")


#findall()
print(re.findall(patrn, "color company co"))  #it return a list if found the target




#search()
if re.search(patrn, "this is red color, company"):   #search()
    print("Found 1")
if re.search(patrn, "color is red, company"):          #anywhere latter sequence is allow
    print("Found 2")
if re.search(patrn, "this is red calor, cmpany"):   #changed
    print("Found 3")
else:
    print("Not Found")


newPtr = "color"
text = "red is a color, what is your fav color"
mat = re.search(newPtr, text)

if mat:
    print(mat.start())    #where 1st found from starting index
    print(mat.end())      # ending index
    print(mat.span())     #start and end index of target


#replacing
txt1 = r"colour"
text2 = "What is your fav colour . This is red colour"
final = re.sub(txt1, "color",text2)
print("[final changed]:", final)

final2 = re.sub(txt1, "color",text2, count=1)
print("[final with count 1]:", final2)

#meta characters
print("\n\nmeta char>>>>>>>>")
tx = r"col..r"                        #anywhere start with col then 2 char then r will match
if re.match(tx, "coloura"):
    print("Matched1")
if re.match(tx, "color"):
    print("Matched2")
tx2 = "^col..r$"                   #anywhere start with col then 2 char then must end with r
if re.match(tx2, "colour"):
    print("Matched3")
