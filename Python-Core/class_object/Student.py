class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def myFunc(self):
        print(self.name)

s1 = Student(1, "Alan", 12)
print(f"{s1.id}, {s1.name}, {s1.age}")
s1.myFunc()
