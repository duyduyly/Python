# Collection

## Keyword
- [**List**](#list)
  1. [*Create List*](#create-list)
  2. [*Access List*](#access-list)
  3. [*Change Element*](#change-element-by-index-and-range-of-index)
  4. [*Add*](#add)
  5. [*Remove*](#remove)
  6. [*Loop*](#loop)
  7. [*List Comprehension*](#list-comprehension)
  8. [*Sort*](#sort)
  9. [*Copy*](#copy)
  10. [*Methods*](#methods)
- [**Tuples**](#tuples)
  1. [*Why Use Tuples?*](#-why-use-tuples) 
  2. [*Create Tuple*](#create-tuples) 
  3. [*Unpack Tuples*](#unpack-tuples)  
  4. [*Use Case*](#-use-cases) 
  5. [*Tuple Methods*](#tuple-methods) 
- [**Set**](#set)
  1. [*Create*](#create-set)
  2. [*Add*](#add-element-in-set)
  3. [*Remove*](#remove-element-in-set)
  4. [*Join*](#join-multiple-sets)
  5. [*Method*](#methods-in-set)
- [**Dictionaries**](#dictionaries)
  1. [*Access*](#access-in-dict)
  2. [*Change And Add*](#change-and-add-element-in-dict)
  3. [*Remove*](#remove-in-dict)
  4. [*Loop*](#loop-in-dict)
  5. [*Copy*](#copy-in-dict)
  6. [*Nested*](#nested-in-dict)
  7. [*Methods*](#methods-in-dict)

------------------
<br/>

## List
- Allow duplicate values.
- The first item has index 0.

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


---------------
<br/>

## Set
- Set items are unordered, unchangeable, and do not allow duplicate values.
- Unordered:
  - Unordered means that the items in a set do not have a defined order.
  - Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
- Unchangeable
  - Set items are unchangeable, meaning that we cannot change the items after the set has been created.

#
### Create Set
```python
thisset = {"apple", "banana", "cherry", "apple"} #created by {} 

thisset2 = {"apple", "banana", "cherry", True, 1, 2} # 1 and True is same, so set just store True

# and, 0 and False is also same.
```

#
### Add Element in Set

```python
mySet = {"apple", "banana", "cherry"}

mySet.add("orange")
print(mySet, end="(1) \n") #add a element

myList = ["pineapple", "mangle"]
mySet.update(myList) #add a List to set
print(mySet, end="(2) \n")
```
```text
{'banana', 'cherry', 'apple', 'orange'}(1) 
{'banana', 'cherry', 'mangle', 'pineapple', 'orange', 'apple'}(2) 
```

#
### Remove Element in Set
```python
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

del mySet3  # delete set completely out memory

print(mySet3, end="(5) \n")
```

```text
Traceback (most recent call last):
  File "...\collection\SetDemo.py", line 30, in <module>
    print(mySet3, end="(5) \n")
NameError: name 'mySet3' is not defined. Did you mean: 'mySet'?

{'cherry', 'apple'}(1) 
{'cherry', 'apple'}(2) 
{'apple', 'banana'}(3) 
set()(4)
```

#
### Join multiple Sets
| **Method**                           | **Operator**                   | **Description**                                                             | **Example Code**                                          | **Result**              |
|--------------------------------------|--------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------|-------------------------|
| `union(other)`                       | `set4 = set1 \| set2  \| set3` | Returns `a new set` with all elements from both sets (no duplicates).       | `{1, 2}.union({2, 3})`                                    | `{1, 2, 3}`             |
| `update(other)`                      | `set1 \|= set2`                | Not return and Update Called Method                                         | `a = {1, 2}; a.update({2, 3})`                            | `a` becomes `{1, 2, 3}` |
| `intersection(other)`                | `set3 = set1 & set2`           | Returns a new set with `elements duplicate` of `both sets`.                 | `{1, 2, 3}.intersection({2, 3, 4})`                       | `{2, 3}`                |                         
| `intersection_update(other)`         | `set1 &= set2`                 | Update the called set and take `duplicate value` of `both sets`.            | `a = {1, 2, 3}; a.intersection_update({2, 3, 4})`         | `a` becomes `{2, 3}`    |                         
| `difference(other)`                  | `set3 = set1 - set2`           | Returns a new set with `keep all elements` from `set1 that are not in set2` | `{1, 2, 3}.difference({2, 3})`                            | `{1}`                   |                         
| `difference_update(other)`           | `set1 -= set2`                 | Update set and same with `difference`                                       | `a = {1, 2, 3}; a.difference_update({2, 3})`              | `a` becomes `{1}`       |                         
| `symmetric_difference(other)`        | `set3 = set1 ^ set2`           | Returns a new set with keep `all elements not duplicate` in both sets.      | `{1, 2, 3}.symmetric_difference({2, 3, 4})`               | `{1, 4}`                |                         
| `symmetric_difference_update(other)` | `set1 ^= set2`                 | Updates set and same with `symmetric_difference`.                           | `a = {1, 2, 3}; a.symmetric_difference_update({2, 3, 4})` | `a` becomes `{1, 4}`    |                         

#
### Methods in Set
- Can read Here! https://www.w3schools.com/python/python_sets_methods.asp


-------------------
<br/>

## Dictionaries
- Dictionaries are `changeable`, meaning that we `can change`, add or remove items after the dictionary has been created.
- Duplicate values will overwrite existing values.
- Can Store String, int, boolean, and list data types.

#
### Access in Dict
```python
dict_ = dict(name="Alan", age=25, country="Norway")
print(dict_["name"], end="(1) \n")
print(dict_.get("name"), end="(2) \n")
print(dict_.keys(), end="(3) \n")
print(dict_.values(), end="(4) \n")
print(dict_.items(), end="(5) \n")
```
```text
Alan(1) 
Alan(2) 
dict_keys(['name', 'age', 'country'])(3) 
dict_values(['Alan', 25, 'Norway'])(4) 
dict_items([('name', 'Alan'), ('age', 25), ('country', 'Norway')])(5)
```

#
### Change and Add Element in Dict
```python
dict_2 = dict(name="Alan", age=25, country="Norway")
dict_2["name"] = "Alan Change" #if existed is Update
dict_2["name2"] = "Alan Change2" #if new key is add
print(dict_2)

dict_2.update({"name": "Alan Update"}) #if existed is Update
dict_2.update({"name3": "Alan Update3"}) #if new key is add
print(dict_2)
```
```text
{'name': 'Alan Change', 'age': 25, 'country': 'Norway', 'name2': 'Alan Change2'}
{'name': 'Alan Update', 'age': 25, 'country': 'Norway', 'name2': 'Alan Change2', 'name3': 'Alan Update3'}
```

#
### Remove in Dict
```python
dict_3 = dict(name="Alan", age=25, country="Norway")

dict_3.pop("name")  # removes the item with the specified key name:
print(dict_3, end="(1) \n")
dict_3.update({"name": "Alan"})

dict_3.popitem()  # remove last Item
print(dict_3, end="(2) \n")
dict_3.update({"name": "Alan"})

del dict_3["age"]  # remove by Item
print(dict_3, end="(3) \n")
dict_3.update({"age": 25})

# del dict_3  remove completely dict_3, when if printing will error
dict_3.clear()
print(dict_3, end="(4) \n")
```
```text
{'age': 25, 'country': 'Norway'}(1) 
{'age': 25, 'country': 'Norway'}(2) 
{'country': 'Norway', 'name': 'Alan'}(3) 
{}(4) 
```

#
### Loop in Dict
```python
dict_4 = dict(name="Alan", age=25, country="Norway")

print()
for x in dict_4:
    print(dict_4[x])

print()
for x in dict_4.keys():
    print(x)

print()
for x in dict_4:
    print(x)

print()
for x, y in dict_4.items():
    print(x, y)
```
```text
Alan
25
Norway

name
age
country

name
age
country

name Alan
age 25
country Norway
```

#
### Copy in Dict
```python
dict_5 = dict(name="Alan", age=25, country="Norway")
dict_6 = dict_5.copy()  # Copy Dict
dict_7 = dict(dict_5)  # Copy Dict
```

#
### Nested in Dict
```python
dict_7 = dict(name="Alan", age=25, country="Norway")
dict_8 = dict(name="Alan", age=25, inner=dict_7)
dict_9 = dict(name="Alan", age=25, inner=dict_8)

print(dict_9)

print(dict_9["inner"]["name"])

print()
for x, obj in dict_9.items():
    print(x)
    if type(x) is dict:
        for y in obj:
            print(y + ':', obj[y])
```
```text
{'name': 'Alan', 'age': 25, 'inner': {'name': 'Alan', 'age': 25, 'inner': {'name': 'Alan', 'age': 25, 'country': 'Norway'}}}
Alan

name
age
inner
```

#
### Methods in Dict
Read Here! (https://www.w3schools.com/python/python_dictionaries_methods.asp)
