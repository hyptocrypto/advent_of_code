import time
import json
from pydantic import BaseModel

# from jsonschema import validate
from typing import Union
from uuid import UUID


schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "*": {
            "type": "object",
            "properties": {"id": {"type": "string"}},
            "required": ["id"],
        },
        "1": {
            "type": "object",
            "properties": {"id": {"type": "string"}},
            "required": ["id"],
        },
    },
    "required": ["0", "1"],
}


class Data(BaseModel):
    id: Union[UUID, str]


class DataPoint(BaseModel):
    data: Data


if __name__ == "__main__":
    with open("json_data.json") as f:
        data = json.loads(f.read())

    start = time.time()
    for i in data:
        DataPoint(data=data[i])

    print(time.time() - start)

    start = time.time()
