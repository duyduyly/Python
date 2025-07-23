mySet = {"apple", "banana", "cherry"}

mySet.add("orange")
print(mySet, end="(1) \n")

myList = ["pineapple", "mangle"]
mySet.update(myList)
print(mySet, end="(2) \n")

print()
mySet2 = {"apple", "banana", "cherry"}

mySet2.remove("banana")
print(mySet2, end="(1) \n")
mySet2.add("banana")  # remove by value

mySet2.discard("banana")
print(mySet2, end="(2) \n")  # remove by value
mySet2.add("banana")

mySet2.pop()  # Remove random value
print(mySet2, end="(3) \n")

mySet2.clear()
print(mySet2, end="(4) \n")

mySet3 = {"apple", "banana", "cherry"}

# del mySet3  # delete set completely out memory

# print(mySet3, end="(5) \n")


print()
mySet1 = {"a", "b", "c"}
mySet2 = {1, 2, 3}
mySet4 = {"Fish Mang", "Snack Fish"}

mySet5 = mySet1.union(mySet2)  # join set1 with set 2 Using Union function
print(mySet5, end="(1) \n")

mySet6 = mySet1 | mySet2 | mySet3  # using |
print(mySet6, end="(2) \n")

mySet7 = mySet2.update(mySet1)
print(mySet7, end="(3) \n")

mySet8 = {1, 2, "A"}
mySet9 = {"A", "C"}

mySet10 = mySet8.intersection(mySet9)  # return new Set and take value duplicate of both set
print(mySet10, end="(4) \n")
mySet11 = mySet8 & mySet9  # can use & instead of intersection

mySet8.intersection_update(mySet9)  # update mySet8, (not return new Set)
print(mySet8)

mySet12 = mySet8 | mySet11
