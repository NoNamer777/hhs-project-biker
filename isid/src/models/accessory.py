from enum import Enum

from .item import Item

KEY_ACCESSORY_TYPE = 'accessory_type'
KEY_ACCESSORY_NEW_PRICE = 'new_price'


class AccessoryType(Enum):
    CHILD_SEAT = 'Child seat'
    HELMET = 'Helmet'
    BIKE_BAG = 'Bicycle bag'


def parse_accessory_type(value) -> AccessoryType or None:
    if type(value) is AccessoryType or value is None:
        return value

    if type(value) is not str:
        raise TypeError(f'Unable to parse \'{value}\' because it is not of type String')

    for accessoryType in AccessoryType:
        if accessoryType.value == value:
            return accessoryType


class Accessory(Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.accessory_type = kwargs.get(KEY_ACCESSORY_TYPE)
        self.new_price = kwargs.get(KEY_ACCESSORY_NEW_PRICE)

    @property
    def new_price(self):
        return self._new_price

    @new_price.setter
    def new_price(self, new_price: float):
        self._new_price = new_price

    @property
    def accessory_type(self):
        return self._accessory_type

    @accessory_type.setter
    def accessory_type(self, accessory_type):
        self._accessory_type = accessory_type if type(accessory_type) is AccessoryType \
            else parse_accessory_type(accessory_type)
