from enum import Enum

from .item import Item

KEY_BICYCLE_TYPE = 'bicycle_type'


class BicycleType(Enum):
    ELECTRIC = 'Electric'
    REGULAR = 'Regular'
    MALE = 'Male'
    FEMALE = 'Female'


def parse_bicycle_type(value) -> BicycleType or None:
    if type(value) is BicycleType or value is None:
        return value

    if type(value) is not str:
        raise TypeError(f'Unable to parse \'{value}\' because it is not of type String')

    for bicycleType in BicycleType:
        if bicycleType.value == value:
            return bicycleType


class Bicycle(Item):
    def __init__(self, data: dict):
        super().__init__(data)

        if data is None:
            return

        self.bicycle_type = data.get(KEY_BICYCLE_TYPE)

    def values(self):
        values = super().values()
        values.extend([self.bicycle_type.value])

        return values

    @property
    def bicycle_type(self):
        return self._bicycle_type

    @bicycle_type.setter
    def bicycle_type(self, bicycle_type):
        self._bicycle_type = bicycle_type if type(bicycle_type) is BicycleType \
            else parse_bicycle_type(bicycle_type)
