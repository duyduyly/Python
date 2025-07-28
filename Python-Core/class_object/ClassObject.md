# Class and Object

- [**Access Modifier**](#access-modifier)
- [**Init Function**](#init-function)
- [**Str Function**](#str-function)
- [**Object Methods**](#object-methods)
  - [**Self parameter**](#self-parameter)
- [**Delete Variable value and Object**](#delete--object-properties)
- [**Empty Method or Class (pass)**](#empty-method-or-class-pass)
- [**Inheritance**](#inheritance)

## Access Modifier
| Access Level  | Syntax                       | Meaning                                        |
|---------------|------------------------------|------------------------------------------------|
| **Public**    | `variable`                   | Accessible from anywhere                       |
| **Protected** | `_variable` (1 underscore)   | Meant for internal use (subclasses can access) |
| **Private**   | `__variable` (2 underscores) | Name mangled to prevent direct access          |

__Example:__
```python
class Test:
    name = "" #public
    _old = 12 #protected
    __ID = 123141412412 #private
```

## __init__() Function
- The `__init__()` function is called automatically every time the class is being used to create a new object.
- All classes have a function called `__init__()`, which is always executed when the class is being initiated.

```python
class Student:
    def __init__(self, id, name, age): #intitialize Constructor
        self.id = id
        self.name = name
        self.age = age


s1 = Student(1, "Alan", 12)
print(f"{s1.id}, {s1.name}, {s1.age}")
```

## __str__() Function
- The __str__() function controls what should be returned when the class object is represented as a string.

```python
class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


s1 = Student(1, "Alan", 12)
print(s1) #str
print(f"{s1.id}, {s1.name}, {s1.age}")
```

## Object Methods

### Self Parameter
- special keyword
- the `self` keyword in method parameters has a special meaning — `it refers to the current object (instance) of the class`.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self): # method #self special keyword to refer current object
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() #call method
```

## Delete  Object Properties
- `del` keyword to delete
```python
del s1.age #delete variable
del s1.name

del s1 #delete object
```

## Empty Method or Class (`pass`)
- use keyword `pass`
- use to mark skip and will write after
```python
class Student:
    pass #I will write later
```

# Inheritance
```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

from class_object.inheritance.Person import Person


class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # add params for parents class
        self.graduation_year = year

    def studentInfo(self):
        print(
            f"Student {self.get_fullname()} graduated at {self.graduation_year}"
        )  # call fullname function from parent class


student = Student("Alan", "Ly", 2021)
student.studentInfo()
```
Class Here: [Student.py](inheritance/Student.py)