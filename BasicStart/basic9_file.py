
file = open("student.txt", "r")      #r means read// w means write// r+ read-write both//  a means append..
print(file.readable())
print(file.writable())

#only one (1/2/3) will work to show result at a time

text2 = file.readlines()              #1 show as list
print(text2)

text = file.read()                     #2 full read
print(text)

size = len(text)                       #size of file contails ,,
print(size)

size = len(text2)                       #size of list ,, text2 is a list now
print(size)


for line in file:                        #3 another way to read files
    print(line)

file.close()

""" 
#only one will work in one .py

file2 = open("student.txt", 'a')        #'w' will erase all from file and write newly, but 'a' will write with old fils latters
file.write("Bangladesh")                 #write on file
file.close()
"""