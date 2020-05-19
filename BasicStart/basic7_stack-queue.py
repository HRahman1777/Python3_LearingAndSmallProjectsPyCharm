from collections import deque


#stack LIFO

names = []
names.append("name1")
names.append("name2")
names.append("name3")
names.append("name4")
print(names)

"""
- name4 -
- name3 -
- name2 -
- name1 -
_________
"""
names.pop()
print(names)
"""
- name3 -
- name2 -
- name1 -
_________
"""

if not names:                     #to check list is empty or not
    print("names list empty")



#queue FIFO
names = []
names.append("name1")
names.append("name2")
names.append("name3")
names.append("name4")
print(names)

"""
- name4 -
- name3 -
- name2 -
- name1 -
_________
"""
names.pop(0)
print(names)
"""
- name4 -
- name3 -
- name2 -
_________
"""
...
#queue using function
bank = deque(["Hasib", "Rahim", "Karim"])
print(bank)
"""
3 - Karim -
2 - Rahim -
1 - Hasib -
_________
"""
bank.popleft()
print(bank)

"""
2 - Karim -
1 - Rahim -
_________
"""