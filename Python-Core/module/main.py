from package1 import python01, python02  # the statement to import or static function in module
from package1 import upperCaseName, lowerCaseName
from package2 import do_something

py1 = python01()
py2 = python02()

py1.init_func()
py2.init_func()

print("Uppercase: ", upperCaseName("alan"))
print("Lowercase: ", lowerCaseName("ALAN"))

do_something()
