arrDict = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
]

brand = "tesla"
model = "Tesla 01"
year = 2025
testaDic = dict(brand=brand, model=model, year=year)
arrDict.append(testaDic)

valueText = "brand,model,year"
myDict = arrDict[0]
print(myDict)
print(myDict["brand"])

for dic in arrDict:
    print()
    for key in valueText.split(","):
        print(dic[key])

print(eval("myDict[\"brand\"]"))

print()
dict_ = dict(name="Alan", age=25, country="Norway")
print(dict_["name"], end="(1) \n")
print(dict_.get("name"), end="(2) \n")
print(dict_.keys(), end="(3) \n")
print(dict_.values(), end="(4) \n")
print(dict_.items(), end="(5) \n")

print()
dict_2 = dict(name="Alan", age=25, country="Norway")
dict_2["name"] = "Alan Change"
dict_2["name2"] = "Alan Change2"
print(dict_2)

dict_2.update({"name": "Alan Update"})
dict_2.update({"name3": "Alan Update3"})
print(dict_2)

print()
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

print()
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

print()
dict_5 = dict(name="Alan", age=25, country="Norway")
dict_6 = dict_5.copy()
dict_7 = dict(dict_5)

print()
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
