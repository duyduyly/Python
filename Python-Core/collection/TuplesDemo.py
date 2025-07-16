myTuples = ("Apple",)
myTuples2 = ("Apple")

print(type(myTuples))
print(type(myTuples2))

myTuple3 = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(myTuple3)

fruits = ("apple", "banana", "cherry")

(green, *yellow) = fruits

print(green)
print(yellow)
