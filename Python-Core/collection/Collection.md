# Collection

# Keyword

- [List](#list)
- [Tuples](#tuples)

## List

- Allow duplicate values.
- The first item has index 0.

Key:

- [Create List](#create-list)
- [Access List](#access-list)
- [Change Element](#change-element-by-index-and-range-of-index)
- [Add](#add)
- [Remove](#remove)
- [Loop](#loop)
- [List Comprehension](#list-comprehension)
- [Sort](#sort)
- [Copy](#copy)
- [Methods](#methods)

#

### Methods

| **Method**     | **Description**                                      | **Example**                 | **Value / Result**                |
|----------------|------------------------------------------------------|-----------------------------|-----------------------------------|
| `append(x)`    | Adds item `x` to the end of the list                 | `lst.append(10)`            | `lst = [1, 2, 3, 10]`             |
| `clear()`      | Removes all elements from the list                   | `lst.clear()`               | `lst = []`                        |
| `copy()`       | Returns a shallow copy of the list                   | `new_lst = lst.copy()`      | `new_lst = [1, 2, 3]`             |
| `count(x)`     | Counts how many times `x` appears in the list        | `lst.count(2)`              | `1` (if 2 appears once)           |
| `extend(lst2)` | Adds all items from `lst2` to end of original list   | `lst.extend([4, 5])`        | `lst = [1, 2, 3, 4, 5]`           |
| `index(x)`     | Returns index of first occurrence of `x`             | `lst.index(3)`              | `2` (if 3 is at index 2)          |
| `insert(i, x)` | Inserts `x` at index `i`, shifting others right      | `lst.insert(1, 99)`         | `lst = [1, 99, 2, 3]`             |
| `pop(i)`       | Removes and returns item at index `i` (default last) | `lst.pop()` or `lst.pop(1)` | Removes item; e.g. `lst = [1, 3]` |
| `remove(x)`    | Removes first occurrence of value `x`                | `lst.remove(2)`             | `lst = [1, 3]`                    |
| `reverse()`    | Reverses the list in place                           | `lst.reverse()`             | `lst = [3, 2, 1]`                 |
| `sort()`       | Sorts the list in ascending order                    | `lst.sort()`                | `lst = [1, 2, 3]`                 |

#

### Create List

- 1: Simple Create
- 2: This uses the list() constructor function, and you're passing a tuple ((...)) as an argument.

```python
thislist = ["apple", "banana", "cherry"]  # 1
thislist2 = list(("apple", "banana", "cherry"))  # 2

print(thislist)
print(type(thislist))
print(thislist2)
print(type(thislist2))
```

```text
['apple', 'banana', 'cherry']
<class 'list'>
['apple', 'banana', 'cherry']
<class 'list'>
```

#

### Access List

```python
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist3[1], end=" (1) \n")  # Get Value with index
print(thislist3[-1], end=" (2) \n")  # Get value with negative Index

print(thislist3[2:5], end=" (3) \n")  # Get value with range of indexes
print(thislist3[:5], end=" (4) \n")  # Start is zero
print(thislist3[2:], end=" (5) \n")  # end is length-1
print(thislist3[-5:-1], end=" (6) \n")  # -1 is start and -5 is and
```

```text
banana (1) 
mango (2) 
['cherry', 'orange', 'kiwi'] (3) 
['apple', 'banana', 'cherry', 'orange', 'kiwi'] (4) 
['cherry', 'orange', 'kiwi', 'melon', 'mango'] (5) 
['cherry', 'orange', 'kiwi', 'melon'] (6) 
```

#

### Change Element by Index and Range of Index

```python
thislist4 = ["apple", "banana", "cherry"]  # 1

thislist4[1] = "Banana"
print(thislist4, end=" (1) \n")

thislist4[1] = ["Banana1", "Banana2"]  # Change index 1 = list ["Banana1", "Banana2"]
print(thislist4, end=" (2)\n")

thislist4[0:3] = ["blackcurrant2", "watermelon2"]  # change from 0 -> 3 to "blackcurrant2" and "watermelon2"
print(thislist4, end=" (3)\n")

thislist4[1:2] = ["blackcurrant3", "watermelon3"]
print(thislist4, end=" (4)\n")

thislist4.insert(1, "watermelon4")  # use insert function
print(thislist4, end=" (5)\n")
```

```text
['apple', 'Banana', 'cherry'] (1) 
['apple', ['Banana1', 'Banana2'], 'cherry'] (2)
['blackcurrant2', 'watermelon2'] (3)
['blackcurrant2', 'blackcurrant3', 'watermelon3'] (4)
['blackcurrant2', 'watermelon4', 'blackcurrant3', 'watermelon3'] (5)
```

#

### Add

```python
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
```

```text
['apple', 'Banana'](1) 
['apple', 'Banana', 'Cherry'](2) 
['apple', 'Banana', 'Cherry', 'Mango', 'Plum'](3) 
['apple', 'Banana', 'Cherry', 'Mango', 'Plum', 'Mango', 'Plum'](4) 
```

#

### Remove

```python
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
```

```text
['apple', 'cherry', 'orange', 'kiwi', 'melon', 'mango'](1) 
['apple', 'orange', 'kiwi', 'melon', 'mango'](2) 
['apple', 'orange', 'kiwi', 'melon'](3) 
['orange', 'kiwi', 'melon'](4) 
[](5) 
```

#

### Loop

```python
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
[print(x, end="(4) ") for x in thislist7]  # short
```

```text
apple(1) banana(1) 
apple(2) banana(2) 
apple(3) banana(3) 
apple(4) banana(4)
```

#

### List Comprehension

#### Syntax

```text
newlist = [expression for item in iterable if condition == True]
```

```python
thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
newlist = [x if x != "banana" else "orange" for x in thislist6]
print(newlist)

newlist2 = [x for x in thislist6 if "a" in x]
print(newlist2)

newlist3 = [x for x in range(10) if x < 5]
print(newlist3)
```

```text
['apple', 'orange', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
['apple', 'banana', 'orange', 'mango']
[0, 1, 2, 3, 4]
```

#

### Sort

```python
import random

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
```

```text
['banana', 'cherry', 'Kiwi', 'Orange'](1) 
['Kiwi', 'Orange', 'banana', 'cherry'](2) 
[2, 4, 4, 5, 7, 8, 9, 9, 9, 9](3) 
[9, 9, 9, 9, 8, 7, 5, 4, 4, 2](4) 
[36, 75, 18, 16, 9, 95, 3, 97, 3, 99](5) 
```

#

### Copy

```python
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
```

```text
[1, 2, 3, 4, 5] (list 2) 
[1, 2, 3, 4, 5] (list 1) 
after change
[1, 10, 3, 4, 5] (list 2 changed when list 1 change, for List 2 reference to list 1) 
[1, 2, 3, 4, 5] (2) 
[1, 2, 3, 4, 5] (3) 
[1, 2, 3, 4, 5] (4) 
```

----------------------
<br/>

## Tuples

__Key:__ <br/>
| [Why Use Tuples?](#-why-use-tuples) | [Create Tuple](#create-tuples) | [Unpack Tuples](#unpack-tuples) | <br/>
| [Use Case](#-use-cases) | [Tuple Methods](#tuple-methods) | <br/>

### About Tuples
- Tuples are `unchangeable`, meaning that we `cannot change`, `add` or `remove` items after the tuple has been created.
- Allow duplicates
- Same list, but it's not support method to change value because it's immutable (unchangeable)

### 🔹 Why Use Tuples?

| Feature        | Benefit                                                                    |
|----------------|----------------------------------------------------------------------------|
| 🔒 Immutable   | Safe from accidental changes (good for constants or config)                |
| ⚡ Faster       | More memory-efficient and faster than lists for fixed data                 |
| 🧠 Hashable    | Can be used as dictionary keys or set elements (if contents are immutable) |
| ✅ Ordered      | Supports indexing and slicing                                              |
| 📦 Lightweight | Useful for fixed-size records (name, age, etc.)                            |

### Create Tuples
```python
thistuple = ("apple",)
print(type(thistuple))  # Tuple

thistuple = ("apple")
print(type(thistuple))  # str

myTuple3 = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(myTuple3)
```

```text
<class 'tuple'>
<class 'str'>
('apple', 'banana', 'cherry')
```

#
### Access

- same with list

#

### Update

- convert `from tuple to list` and `update` or `delete`

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```

#

### Unpack Tuples

- Unpacking a `tuple means assigning` each element of a tuple (or any iterable) to its own variable in a `single line`.

#### ✅ it's Ok

```python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

#### 🔴 It's not Ok

```python
fruits = ("apple", "banana", "cherry")

(green, yellow) = fruits
```

#### Extended Unpacking with *

```python
fruits = ("apple", "banana", "cherry")

(green, *yellow) = fruits

print(green)
print(yellow)
```

```text
apple
['banana', 'cherry']
```

#### ✅ Use Cases

| Use Case                    | Example               |
|-----------------------------|-----------------------|
| Assign multiple values      | `x, y = (1, 2)`       |
| Swap variables              | `a, b = b, a`         |
| Loop through list of tuples | `for x, y in points:` |
| Ignore values with `_`      | `x, _, z = (1, 2, 3)` |

#### You can also unpack in for loops

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, char in pairs:
    print(num, char)
```

#

### Tuple Methods

| **Method** | **Description**                                               | **Example**             | **Output / Result** |
|------------|---------------------------------------------------------------|-------------------------|---------------------|
| `count(x)` | Returns the number of times `x` appears in the tuple          | `(1, 2, 2, 3).count(2)` | `2`                 |
| `index(x)` | Returns the **first index** of value `x` (error if not found) | `(1, 2, 3).index(3)`    | `2`                 |


