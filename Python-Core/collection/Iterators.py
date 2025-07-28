my_tuple = ("apple", "banana", "cherry")
myit = iter(my_tuple)

print(next(myit))
print(next(myit))


# Custom Iterators
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))


# Custom 2
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass2 = MyNumbers2()
myiter2 = iter(myclass2)

for x in myiter2:
    print(x)
