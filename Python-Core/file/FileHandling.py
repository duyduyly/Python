import os

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

print()
print("Delete File")
os.mkdir("../resource/12")  # create folder
filePath = "../resource/text-file2.txt"
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("The file does not exist")
