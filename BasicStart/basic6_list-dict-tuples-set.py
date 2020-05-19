
#list >>>>>>>>>>>>>>>>
print("List >>> \n")
names = ['Hasibur', 'Rahman', 'Mohammad', 'Mahmud', 'Rahim']
names2 = ['Has', 'Rah', 'Abc', 'ioj']
num = [10, 2, 6, 8, 3, 3]

print(names)
print(len(names))                    #len()
print(names[0])
print(names[1:])
print(names[:-1])

names = names + ['Karim', 1777]
names.append("Number")               #append()
print(names)
names.insert(2, 'Abu')               #insert( position, value)
print(names)

names.remove("Abu")                      #remove()
print(names)

names.reverse()                        #reverse()
print(names)
names.pop()                             #pop()
print(names)

newName = names.copy()                    #copy()
print(newName)
res = newName.index("Rahman")            #index(value)
print(res)


print(names * 2)
print("Rahman" in names)
print("python" in names)
print("python" not in names)

names2.sort()                               #sort()   must need all str or int (same data type)
print(names2)
num.sort()
print(num)
print(num.count(3))                        #count()

newList = list(range(10))                  #range( , )
print(newList)
newList = list(range(3, 6))
print(newList)
newList = list(range(2, 21, 2))            #range( , , )
print(newList)


#dict >>>>>>>>>>>>>>>>>>>>>>
print("Dict>>>>\n")

student = {
    "1" : "Hasibur",
    "2" : "Rahman",
    "5" : "Rahim",
    3 : "Karim"
}

print(student["5"])           #also can be use student.get("5")

print(student.get(3, "Not available"))
print(student.get("3", "Not available"))


#tuples >>>>>>>>>>>>>>>>>>>>>>>>>>> same as list but value cant be changed

studentName = (
    "abc", "def", "ghi", (1, 2, 3, 4)
)
print(studentName)
print(studentName[3])  #tuples under tuples (also valid in list)


#set >>>>>>>>>>>>>>>>>>>>>>>>
print("Set >>>>>>>>\n")

num1 = {1, 2, 3, 4, 5, 5}                       #duplicate value cant work
num2 = set([4, 5, 6, 7])                         #list converted into set useing .set()
print(num1)
print(num2)

num1.add(9)
print(num1)

num1.remove(9)
print(num1)
print(3 in num1)

print(num1 | num2)              #union
print(num1 & num2)              #intersection
print(num1 - num2)              #minus num2 from num1