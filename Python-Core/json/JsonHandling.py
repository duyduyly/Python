from dataclasses import dataclass
from jsonschema.exceptions import ValidationError
from pydantic import BaseModel
from jsonschema import validate
import json

person = '{"name": "Bob", "age": 30}'
json_data = json.loads(person)
print(json_data["name"])
print(json_data["age"])

json_data["name"] = "Alan"
dumps = json.dumps(person, indent=4)
print(dumps)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Alan", 25)
json_user = json.dumps(user.__dict__)  # Covert from class to json
print(json_user)

json_str = '{"name": "Alice", "age": 25}'
data = json.loads(json_str)

user = User(**data)  # unpack JSON keys into class init
print(user.name)  # Alice


# use dataclasses (python 3.7+)

@dataclass
class User2:
    name: str
    age: int


json_str2 = '{"name": "Bob", "age": 30}'
data = json.loads(json_str2)

user2 = User2(**data)
user2.name = "Alan"
print(user2)
print(json.dumps(user2.__dict__))


# use pydantic
class User3(BaseModel):
    name: str
    age: int


json_str2 = '{"name": "Carol", "age": 35}'
user3 = User3.parse_raw(json_str2)

print(user3.name)  # Carol

person = '{"name": "Bob", "age": 30}'
json_data = json.loads(person)
with open("../resource/data.json", "w") as f:  # save to file
    json.dump(json_data, f)

with open("../resource/data.json") as f:
    data = json.load(f)
    print(data)

# JSON schema
schema = {
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

# JSON data
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"]
}

# Validate it
validate(instance=data, schema=schema)
print("✅ JSON is valid!")

# JSON data
data2 = {
    "name": "Alice",
    "age": "30",
    "skills": ["Python", "SQL"]
}
try:
    validate(instance=data2, schema=schema)
except:
    print("Json is Invalid")

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
