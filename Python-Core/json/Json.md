# Json Handling

- [**Convert Json To ...**](#covert)
- [**Object to Json (json.dumps(ob))**](#from-object-to-json-jsondumps)
- [**Class To Json**](#class-to-json)
- [**Validate Json (jsonschema)**](#validate-json-jsonschema)

| Task           | Method                       |
|----------------|------------------------------|
| Read JSON str  | `json.loads()`               |
| Write JSON str | `json.dumps()`               |
| Read from file | `json.load()`                |
| Write to file  | `json.dump()`                |
| Handle class   | Use `__dict__` or `asdict()` |
| Avoid errors   | Use `try/except`             |


## Covert

- [**Dictionary**](#json-to-dictionary)
- [**Json To Class**](#json-to-class)
    - [*@dataclasses*](#using-dataclasses-python-37)
    - [ *pydantic*](#using-pydantic-recommended-for-larger-apps-or-apis)
    - [ *Handle nested Json*](#handle-nested-json)

### Json To Dictionary

```python
import json

person = '{"name": "Bob", "age": 30}'
json_data = json.loads(person)
print(json_data["name"])
print(json_data["age"])

with open("../resource/data.json", "r") as f:
    data = json.load(f)
    print(data)

```

#  

### Json To Class

| Method                    | Best For                  | Tools Needed           |
|---------------------------|---------------------------|------------------------|
| `User(**json.loads(...))` | Simple use                | No extra libraries     |
| `@dataclass`              | Clean code, structure     | Python 3.7+            |
| `pydantic`                | Validation, APIs, FastAPI | `pip install pydantic` |

#
#### Using `dataclasses` (Python 3.7+)
```python
from dataclasses import dataclass
import json


@dataclass
class User:
    name: str
    age: int


json_str = '{"name": "Bob", "age": 30}'
data = json.loads(json_str)

user = User(**data)
print(user)

```

#
#### Using `pydantic` (recommended for larger apps or APIs)
```python
from pydantic import BaseModel
import json


class User(BaseModel):
    name: str
    age: int


json_str = '{"name": "Carol", "age": 35}'
user = User.parse_raw(json_str)

print(user.name)  # Carol
```

#
#### Handle `Nested Json`
```python
import json

json_str = '''
{
    "name": "Duy",
    "profile": {
        "email": "duy@example.com",
        "phone": "123456789"
    }
}
'''


class Profile:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone


class User:
    def __init__(self, name, profile):
        self.name = name
        self.profile = Profile(**profile)


data = json.loads(json_str)
user = User(**data)
print(user.profile.email)
```
----------------
<br/>

## From Object to Json (json.dumps())
### Parameters
| Parameter               | Description                     |
|-------------------------|---------------------------------|
| `indent=4`              | Pretty-print with indentation   |
| `sort_keys=True`        | Sort the keys alphabetically    |
| `ensure_ascii=False`    | Allow Unicode characters        |
| `separators=(",", ":")` | Compact output, no extra spaces |

#
### Dictionary to Json file
```python
import json

person = '{"name": "Bob", "age": 30}'
json_data = json.loads(person) #dictionary
with open("../resource/data.json", "w") as f:  # save to file
    json.dump(json_data, f)

person2 = {"name": "Bob", "age": 30} 
json_data2 = json.dumps(person2) # dictionary to Json
print(json_data2)
```

#
### Class to Json
```python
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Alan", 25)
json_user = json.dumps(user.__dict__)  # Covert from class to json
print(json_user)
```

## Validate Json (`jsonschema`)
### Installation
```bash
pip install jsonschema
```

__Example:__

```python
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# JSON schema
schema2 = {
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "age": {"type": "number"},
    "skills": {
      "type": "array",
      "items": {"type": "string"}
    }
  },
  "required": ["name", "age"]
}

data3 = {
  "name": "Alice",
  "age": 30,
  "skills": ["Python", "SQL"]
}
data4 = {
  "name": "Alice",
  "age": "30",
  "skills": ["Python", "SQL"]
}


def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError:
        return False


for isValid in (validate_json(data3, schema2), validate_json(data4, schema2)):
    print("Json is Valid" if isValid else "Json is Invalid")
```
```text
Json is Valid
Json is Invalid
```
- If the data is wrong (e.g., `age` is a string), it will raise a `jsonschema.exceptions.ValidationError.`

All Example: [JsonHandling.py](JsonHandling.py)