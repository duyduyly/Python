## File Handling 
- [**Read**](#read)
- [**Create And Write**](#create-and-write)
- [**Delete**](#delete)

| shortly key | Use to                                                                             |
|-------------|------------------------------------------------------------------------------------|
| `"r"`       | `Read` - Default value. Opens a file for reading, error if the file does not exist |
| `"a"`       | `Append` - Opens a file for appending, creates the file if it does not exist       |
| `"w"`       | `Write` - Opens a file for writing, creates the file if it does not exist          |
| `"x"`       | `Create` - Creates the specified file, returns an error if the file exists         |

In addition, you can specify if the file should be handled as binary or text mode:

| shortly key | Use to                             |
|-------------|------------------------------------|
| `"t"`       | Text - Default value. Text mode    |
| `"b"`       | Binary - Binary mode (e.g. images) |

```python
f = open("text-file.txt")

# f = open("text-file.txt", "rt") #the code above is same this code
```

## Read

```python
print("(1)")
t = open("../resource/text-file.txt")
print("Type: ", type(t.read()))
print(t.read())
t.close()  # should close after handling

print("(2)")
print("ReadLine: ")
t1 = open("../resource/text-file.txt")
print(t1.readline())
print(t1.readline())
print(t1.readline())
t1.close()

print()
print("(3)")
with open("../resource/text-file.txt") as f:  # don't worry about closing your file
    print(f.read())

print()
print("(4)")
with open("../resource/text-file.txt", "r") as f:  # don't worry about closing your file
    print()
    print("read(15)")
    print(f.read(15))
```
```text
(1)
Type:  <class 'str'>

(2)
ReadLine: 
Or Open window and search: `Edit environment variables `

- and then: open `environment variables...`

![ConfigEnvironment-1.png](resource/ConfigEnvironment-1.png)


(3)
Or Open window and search: `Edit environment variables `
- and then: open `environment variables...`
![ConfigEnvironment-1.png](resource/ConfigEnvironment-1.png)
- Choose path: ![ConfigEnvironment-2.png](resource/ConfigEnvironment-2.png)
- Get python folder path: `C:\Python310`
- paste here: ![ConfigEnvironment-3.png](resource/ConfigEnvironment-3.png)
- OK OK and Apply

(4)

read(15)
Or Open window 
```

## Create And Write
- `os.mkdir("../resource/12")  # create folder`

| shortly key | Use to                                                                             |
|-------------|------------------------------------------------------------------------------------|
| `"a"`       | `Append` - Opens a file for appending, creates the file if it does not exist       |
| `"w"`       | `Write` - Opens a file for writing, creates the file if it does not exist          |
| `"x"`       | `Create` - Creates the specified file, returns an error if the file exists         |

```python
print()
print("Write file")
with open("../resource/text-file2.txt", "w") as f:
    f.write("new File....")

with open("../resource/text-file2.txt", "r") as f:
    print(f.read(), "(1)")

with open("../resource/text-file2.txt", "w") as f:
    f.write("Just Update new file just create")

with open("../resource/text-file2.txt", "r") as f:
    print(f.read(), "(2)")
```
```text
Write file
new File.... (1)
Just Update new file just create (2)
```

### Delete

```python
import os

print()
print("Delete File")
os.mkdir("../resource/12")  # create folder
filePath = "../resource/text-file2.txt"
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("The file does not exist")
```