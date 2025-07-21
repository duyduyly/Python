## Foundational

## Keyword
- [**Print method**](#print-method)
- [**Comment**](#comment)
- [**Data Types**](#data-types)
- [**Number Types**](#number-types)
  - [*Casting*](#numeric-casting)
  - [*Random Number*](#random-number)
- [**String**](#string-type)
  - [*Assign String*](#assign-string)
  - [*String Array*](#string-array)
  - [*Check String*](#check-string)
  - [*Slicing String*](#slicing-string)
  - [*String methods*](#string-methods)
  - [*String Format*](#string-format)
- [**Boolean**](#boolean)
- [**Operator**](#operator)
- [**For Loop**](#for-loop)
- [**Condition**](#condition)
- [**Function**](#function)
- [**Import Class**](#import-class)
- [**Naming Conventions**](#naming-conventions)


------------------------------
<br/>

## Print Method
- Basic
```python
print("Hello")
print("Python", "And", "And", sep="--") #use sep
print("Python", "And", "And", end="--") #use end
print("")
print("Python", "And", "And", sep="\n")
print("")
print("Python", "And", "And", sep="\n", end="----------")
```
```text
Hello
Python--And--And
Python And And--
Python
And
And

Python
And
And----------
```
----------------
<br/>

## Comment
__Single line:__
```python
# this is single Comment
```
#
__Multiple Comment:__
```python
"""
This is 
Multiple 
Comment
"""
```

------------------------------
<br/>

## Data types
- Python's `dynamic typing mechanism` allows variables to change their data types during program execution.
- No need declare variable type (use `type(<variable>)` method to check)


#
### All About Types
- [Numeric Types](#-numeric-types)
- [Text Type](#-text-type)
- [Boolean Type](#-boolean-type)
- [Sequence Types](#-sequence-types)
- [Mapping Type](#-mapping-type)
- [Set Types](#-set-types)
- [None Type](#-none-type)
- [Binary Types](#binary-types)
- [Types Example](#types-example)

#
### 🔤 Numeric Types
| Type      | Description                   | Example        |
|-----------|-------------------------------|----------------|
| `int`     | Integer numbers               | `10`, `-3`     |
| `float`   | Floating point numbers        | `3.14`, `-2.0` |
| `complex` | Complex numbers (real + imag) | `3 + 5j`       |

#
### 🔤 Text Type
| Type  | Description        | Example   |
|-------|--------------------|-----------|
| `str` | String (text data) | `"hello"` |

#
### 🧠 Boolean Type
| Type   | Description    | Example         |
|--------|----------------|-----------------|
| `bool` | Logical values | `True`, `False` |

#
### 📦 Sequence Types
| Type    | Description                         | Example       |
|---------|-------------------------------------|---------------|
| `list`  | Ordered, mutable collection         | `[1, 2, 3]`   |
| `tuple` | Ordered, immutable collection       | `(1, 2, 3)`   |
| `range` | Sequence of numbers (used in loops) | `range(1, 5)` |

#
### 🗂️ Mapping Type
| Type   | Description     | Example                        |
|--------|-----------------|--------------------------------|
| `dict` | Key-value pairs | `{"name": "Alice", "age": 25}` |

#
### 🧮 Set Types
| Type        | Description                | Example                |
|-------------|----------------------------|------------------------|
| `set`       | Unordered, unique elements | `{1, 2, 3}`            |
| `frozenset` | Immutable version of `set` | `frozenset([1, 2, 3])` |

#
### Binary Types
| Type         | Description                               | Example                         |
|--------------|-------------------------------------------|---------------------------------|
| `bytes`      | Immutable sequence of bytes               | `b"hello"` or `bytes([65, 66])` |
| `bytearray`  | Mutable sequence of bytes                 | `bytearray([65, 66, 67])`       |
| `memoryview` | Memory-efficient object to access buffers | `memoryview(b"hello")`          |


#
### 🪑 None Type
| Type       | Description         | Example |
|------------|---------------------|---------|
| `NoneType` | Represents no value | `None`  |

#
### Types Example:
```python
x = 10            # int
y = 3.14          # float
name = "Alice"    # str
flag = True       # bool
items = [1, 2, 3] # list
point = (4, 5)    # tuple
info = {"id": 1}  # dict
unique = {1, 2, 3}# set
nothing = None    # NoneType
```

------------------------------
<br/>

## Number Types:

```python
a = 20
b = 30.25
c = 3j
print(a, b, c)
print(type(a))
print(type(b))
print(type(c))
```
```text
20 30.25 3j
<class 'int'>
<class 'float'>
<class 'complex'>
```

#
### Numeric Casting
```python
#int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#float
x2 = float(1)     # x will be 1.0
y2 = float(2.8)   # y will be 2.8
z2 = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2

#Str
x3 = str("s1") # x will be 's1'
y3 = str(2)    # y will be '2'
z3 = str(3.0)  # z will be '3.0'
```

### Random Number
```python
import random

print(random.randrange(1, 10))
```
------------------------------
<br/>

## String Type

#
### Assign String
#### Single:
```python
a = "Hello"
```

#### Multiple:
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)
```

#
#### String Array
```python
print("Hello, World!"[1])
for x in "banana":
    print(x)
```
```text
e
b
a
n
a
n
a
```

#
#### Check String

__Is Contain in text?:__
```python
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```
__Is Not Contain in text:__
```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```

#### Slicing String
```python
b = "Hello, World!"
print(b[2:5]) #b[startIndex:endIndex]

b2 = "Hello, World!"
print(b[:5])

b3 = "Hello, World!"
print(b[-3:-1]) # b[end:start] when use negative index which will start from -1 to -3
```
```text
llo
Hello
ld
```

#
### String Methods
- Full String methods (https://www.w3schools.com/python/python_strings_methods.asp)

| Method                                         | Description                                                                                    | Example                                                  | Result                       |
|------------------------------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------------------------|
| [len()](#len)                                  | To get the length of a string, use the `len()` function.                                       | `len("Hello, World!")`                                   | 13                           |
| [upperCase()/lowerCase()](#uppercaselowercase) | Upper Case and Lower Case                                                                      | `b = "Hello, World!";print(b.lower()); print(b.upper())` | `hello, world!HELLO, WORLD!` |
| [Remove Whitespace](#remove-whitespace)        | The `strip()` method removes any whitespace from the beginning or the end                      | `print("    Hello    ".strip())`                         | `Hello`                      |
| [Replace String](#replace-string)              | The `replace()` method replaces a string with another string.                                  | `print("Hello, World!".replace("H", "J"))`               | `Jello, World!`              |
| [Split String](#split-string)                  | The `split()` method splits the string into substrings if it finds instances of the separator. | `print("Hello, World!".split(","))`                      | `['Hello', ' World!']`       |



#
#### len()
```python
print(len("Hello, World!"))
```
```text
13
```

#
#### upperCase()/lowerCase()
```python
b = "Hello, World!"
print(b.lower())
print(b.upper())
```
```text
hello, world!
HELLO, WORLD!
```

#
#### Remove Whitespace
```python
print("    Hello    ".strip())
```
```text
Hello
```

#
#### Replace String
```python
print("Hello, World!".replace("H", "J"))
```

#
#### Split String
```python
print("Hello, World!".split(","))
```
```text
['Hello', ' World!']
```

#
### String Format
```python
price = 59
print(f"The price is {price} dollars")  #Add a placeholder for the price variable.
print(f"The price is {price:.2f} dollars")  #Display the price with 2 decimals.
print(f"The price is {20 * 59} dollars")  #Perform a math operation in the placeholder, and return the result.
```

```text
The price is 59 dollars
The price is 59.00 dollars
The price is 1180 dollars
```

------------------------
<br/>

## Boolean

### Return True When

- Almost any value is evaluated to True if it has some sort of content.
- Any string is True, except empty strings.
- Any number is True, except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.

```python
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
```

### Return False When

```python
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```

----------------------
<br/>

## Operator

- Read Here! (https://www.w3schools.com/python/python_operators.asp)

-------------------
<br/>

## For Loop

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)

for i in range(5):  # 0 to 4
  print(i)

for i in range(len(fruits)):
  print(i, fruits[i])

for index, fruit in enumerate(fruits):
  print(index, fruit)
```

-------------------
<br/>

## Condition

### If elif else 
```python
a = 200
b = 50

#if
if b > a:
    print("b greater than a")

# if elif else
if b > a:
    print("b greater than a")
elif b == a:
    print("b equal a")
else:
    print("a greater than b")
    
#shortly
print("b greater than a") if b > a else print("a greater than b")

```
#
### Match
#### Syntax
```text
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
```

```python
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
```

------------------
<br/>

## Function
```python
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#default parameter
def greet(name="Guest"):
    print(f"Hi {name}")

#multiple arguments
def total(*args):
    return sum(args)

print(total(1,2,3,4,5,6,7))

#keyword arguments
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_info(name="Alice", age=25, country="USA")


```

-------------------
<br/>

## Import Class

| Syntax                                        | What It Imports                  | How You Use It                      |
|-----------------------------------------------|----------------------------------|-------------------------------------|
| `import TodoListService`                      | Whole module (file)              | `TodoListService.TodoListService()` |
| `import TodoListService as tls`               | Whole module, but renamed        | `tls.TodoListService()`             |
| `from TodoListService import TodoListService` | Only the class `TodoListService` | `TodoListService()`                 |


### 🧠 Best Practice?
- ✅ Use `from ... import ...` when you just want a class or function (e.g., `from math import sqrt`)
- ✅ Use `import module as alias` when you use many items from that file or want to shorten long names

#
Option 1: `import TodoListService`
```python
import TodoListService

service = TodoListService.TodoListService()  # Need full name
```

#
Option 2: `from TodoListService import TodoListService`
```python
from TodoListService import TodoListService

service = TodoListService()  # Shorter and cleaner
```

#
Option 3: `import TodoListService as tls`
```python
import TodoListService as tls

service = tls.TodoListService()  # Uses alias
```

-------------
<br/>

## Naming Conventions
| Type                | Style                 | Example                  |
|---------------------|-----------------------|--------------------------|
| Variable / function | `snake_case`          | `user_age`, `get_info()` |
| Class               | `PascalCase`          | `CustomerOrder`          |
| Constant            | `ALL_CAPS`            | `MAX_SIZE`               |
| Protected           | `_underscore`         | `_helper_method()`       |
| Private             | `__double_underscore` | `__secret()`             |
| Magic method        | `__dunder__`          | `__init__`, `__str__`    |
| Module/file         | `snake_case.py`       | `math_utils.py`          |
| Package             | `lowercase`           | `mypackage`              |
