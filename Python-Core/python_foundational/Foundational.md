## Foundational

## Keyword
- [Print method](#print-method)
- [Comment](#comment)
- [Data Types](#data-types)
- [Number Types](#number-types)
  - [Casting](#numeric-casting)
  - [Random Number](#random-number)
- [String](#string-type)
  - [Assign String](#assign-string)
  - [String Array](#string-array)
  - [Check String](#check-string)
  - [Slicing String](#slicing-string)
  - [String methods](#string-methods)
  - [String Format](#string-format)


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
print(f"The price is {price} dollars") #Add a placeholder for the price variable.
print(f"The price is {price:.2f} dollars") #Display the price with 2 decimals.
print(f"The price is {20 * 59} dollars") #Perform a math operation in the placeholder, and return the result.
```
```text
The price is 59 dollars
The price is 59.00 dollars
The price is 1180 dollars
```
