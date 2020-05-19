#while loop >>>>>>>>>>>>>>
i = 1
while i<=10:
    print(i)
    i = i+1
print("1st Loop Done")


print("2nd Loop Start")
n = 1
while n <= 10:
    if n == 5:
        break
    n = n+1
print(f"Break when n: {n}")
print("2nd Loop Done")


print("3rd Loop Start")
n = 0
while n < 10:
    n = n+1
    if n == 5:
        continue
    print(n)
print("3rd Loop Done\n\t")


print("4th Loop Start")
num = [2, 4 ,6, 0, 1]
print(num)
n = len(num)
i=0
while i < n:
    print(num[i])
    i = i+1
print("4th Loop Done\n\t")


#for loop >>>>>>>>>>>>>

newList = list(range(10))                  #range( , )
print(newList)
newList = list(range(3, 6))
print(newList)
newList = list(range(2, 21, 2))            #range( , , )
print(newList)

print("2nd For Loop Start")
num = [2, 4 ,6, 0, 1]
print(num)
n = len(num)

for i in num:
    print(i)

print("2nd For Loop Done\n\t")

print("3rd For Loop Start")
n = 5
for i in range(n):
    print(i)

print("3rd For Loop Done\n\t")

print("4th For Loop Start")
n = 20
for i in range(1, n+1, 2):
    print(i)

print("4th For Loop Done\n\t")