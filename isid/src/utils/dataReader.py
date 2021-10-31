from csv import DictReader
from typing import Type


def read_data(location: str, object_type: Type):
    objects = []

    with open(location, 'r') as data:
        reader = DictReader(data)

        for row in reader:
            objects.append(object_type(row))

    return objects
