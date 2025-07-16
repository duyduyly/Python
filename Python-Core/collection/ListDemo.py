import random

thislist = ["apple", "banana", "cherry"]  # 1
thislist2 = list(("apple", "banana", "cherry"))  # 2

print(thislist)
print(type(thislist))
print(thislist2)
print(type(thislist2))
print()

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist3[1], end=" (1) \n")  # Get Value with index
print(thislist3[-1], end=" (2) \n")  # Get value with negative Index

print(thislist3[2:5], end=" (3) \n")  # Get value with range of indexes
print(thislist3[:5], end=" (4) \n")  # Start is zero
print(thislist3[2:], end=" (5) \n")  # end is length-1
print(thislist3[-5:-1], end=" (6) \n")  # -1 is start and -5 is and

print()
thislist4 = ["apple", "banana", "cherry"]  # 1

thislist4[1] = "Banana"
print(thislist4, end=" (1) \n")

thislist4[1] = ["Banana1", "Banana2"]
print(thislist4, end=" (2)\n")

thislist4[0:3] = ["blackcurrant2", "watermelon2"]
print(thislist4, end=" (3)\n")

thislist4[1:2] = ["blackcurrant3", "watermelon3"]
print(thislist4, end=" (4)\n")

thislist4.insert(1, "watermelon4")
print(thislist4, end=" (5)\n")

print()
thislist5 = ["apple"]

thislist5.append("Banana")  # use append method to add
print(thislist5, end="(1) \n")

thislist5.insert(2, "Cherry")  # use insert to add
print(thislist5, end="(2) \n")

thislist5_1 = ["Mango", "Plum"]  # list
thislist5_2 = ("Mango2", "Plum2")  # Tuble

thislist5.extend(thislist5_1)
print(thislist5, end="(3) \n")
thislist5.extend(thislist5_1)
print(thislist5, end="(4) \n")

print()
thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

thislist6.remove("banana")
print(thislist6, end="(1) \n")  # remove banana first (if have two element is banana in list)

thislist6.pop(1)
print(thislist6, end="(2) \n")  # remove element at index == 1

thislist6.pop()
print(thislist6, end="(3) \n")  # remove last element

del thislist6[0]  # remove element at index == 0
print(thislist6, end="(4) \n")

thislist6.clear()  # clear all element in list
print(thislist6, end="(5) \n")

print()
thislist7 = ["apple", "banana"]
for e in thislist7:
    print(e, end="(1) ")

print()
for i in range(len(thislist7)):
    print(thislist7[i], end="(2) ")

print()
i = 0
while i < len(thislist7):
    print(thislist7[i], end="(3) ")
    i += 1

print()
[print(x, end="(4) ") for x in thislist7]

print()
print()

thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [x if x != "banana" else "orange" for x in thislist6]
print(newlist)

newlist2 = [x for x in thislist6 if "a" in x]
print(newlist2)

newlist3 = [x for x in range(10) if x < 5]
print(newlist3)

print()
myList = ["banana", "Orange", "Kiwi", "cherry"]
myList.sort(key=str.lower)
print(myList, end="(1) \n")

myList2 = ["banana", "Orange", "Kiwi", "cherry"]
myList.sort()
print(myList, end="(2) \n")

myList3 = [random.randrange(1, 10) for i in range(10)]
myList3.sort()
print(myList3, end="(3) \n")

myList3.sort(reverse=True)
print(myList3, end="(4) \n")

myList4 = [random.randrange(1, 100) for i in range(10)]


def myCustomSort(n):
    return abs(n - 50)


myList4.sort(key=myCustomSort)
print(myList4, end="(5) \n")

print()
# Copy list
list1 = [1, 2, 3, 4, 5]
list2 = list1  # wrong copy
list3 = list1.copy()  # right
list4 = list(list1)  # right
list5 = list1[:]  # right

print(list2, end=" (list 2) \n")
print(list1, end=" (list 1) \n")
list1[1] = 10

print("after change")
print(list2, end=" (list 2 changed when list 1 change, for List 2 reference to list 1) \n")
print(list3, end=" (2) \n")
print(list4, end=" (3) \n")
print(list5, end=" (4) \n")
