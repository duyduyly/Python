# About Module

## __init__.py
- [Support Import](#support-imports-package-initialization)
- [Run Initialization code Automatically](#run-initialization-code-automatically)
- [Import Function](#import-static-function)
#
### Support Imports (Package Initialization)
  - It lets Python know that a folder is a package.
  - This allows you to import modules using dot notation:

- in package1: 
  - [Python1.py](package1/Python1.py)
  - [Python2.py](package1/Python2.py)

````python
class python01:
    def init_func(self):
        print("Init Python01")

class python02:
    def init_func(self):
        print("Init Python02")
````

- in [__init__.py](package1/__init__.py)
```python
from .Python1 import python01
from .Python2 import python02
```

- [main.py](main.py)
```python
from package1 import python01, python02

py1 = python01()
py2 = python02()

py1.init_func()
py2.init_func()
```

#
### Run Initialization Code Automatically
- You can preload functions, variables, or modules, or run any setup logic (like logging, loading configs, etc.).


- in Package2:
- [Config.py](package2/Config.py)
```python
ENV = "production"
API_KEY = "your-api-key"
```


- [Tools.py](package2/Tools.py)
```python
from . import ENV, API_KEY


def do_something():
    print(f"Running in {ENV} with API key: {API_KEY}")
```

- [__init__.py](package2/__init__.py)
```python
from .Config import ENV, API_KEY # add first to use in do_something in tool class
from .Tools import do_something

# Optional: run some setup
print(f"[my_package] Loaded in {ENV} mode") # add first to use in do_something in tool class

# Now expose variables at package level
__all__ = ["ENV", "API_KEY"] # add first to use in do_something in tool class
```
- [main.py](main.py)
```python
from package2 import do_something

do_something()
```
```text
[my_package] Loaded in production mode
Running in production with API key: your-api-key
```

#
### Import static function

- [Utils.py](package1/Utils.py)
```python
def upperCaseName(name):
    return str(name).upper()


def lowerCaseName(name):
    return str(name).lower()
```

- [__init__.py](package1/__init__.py)
```python
from .Utils import upperCaseName, lowerCaseName
```
- [main.py](main.py)
```python
print("Uppercase: ", upperCaseName("alan"))
print("Lowercase: ", lowerCaseName("ALAN"))
```
```text
Uppercase:  ALAN
Lowercase:  alan
```