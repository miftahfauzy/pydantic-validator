from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError

"""
Methods and attributes under BaseModel
Classes that inherit the BaseModel will have the following methods and attributes:
    dict()          — returns a dictionary of the model’s fields and values
    json()          — returns a JSON string representation dictionary
    copy()          — returns a deep copy of the model
    parse_obj()     — a utility for loading any object into a model with error handling if the object is not a dictionary
    parse_raw()     — a utility for loading strings of numerous formats
    parse_field()   — similar to parse_raw() but meant for files
    from_orm()      — loads data into a model from an arbitrary class
    schema()        — returns a dictionary representing the model as JSON schema
    schema_json()   — returns a JSON string representation of schema()
    construct()     — a class method for creating models without running validation
    __fields_set__  — Set of names of fields which were set when the model instance was initialized
    __fields__      — a dictionary of the model’s fields
    __config__      — the configuration class for the model
"""


class User(BaseModel):
    id: int
    username: str
    password: str
    confirm_password: str
    alias = 'anonymous'
    timestamp: Optional[datetime] = None
    friends: List[int] = []


data = {'id': '12345', 'username': 'wai foong', 'password': 'Password123', 'confirm_password': 'Password123',
        'timestamp': '2020-08-03 10:30', 'friends': [1, '2', b'3']}

# this will cause trigger error on validation
# data = {'id': 'random string', 'username': 'wai foong', 'password': 'Password123', 'confirm_password':
#         'Password123', 'timestamp': '2020-08-03 10:30', 'friends': [1, '2', b'3']}

"""
[
  {
    "loc": [
      "id"
    ],
    "msg": "value is not a valid integer",
    "type": "type_error.integer"
  }
]
"""

try:
    user = User(**data)
    print("Printing to dict format output:")
    print(user.dict())
    print()
    print("Printing to json format output:")
    print(user.json())
except ValidationError as e:
    print(e.json())
