from enum import Enum

from item import Item


class AccessoryType(Enum):
    CRATE = 'Crate'
    LOCK = 'Lock'
    BELL = 'Bell'
    CLOTHING = 'Clothing'
    BOTTLE = 'Bottle'
    LUGGAGE_CARRIER = 'Luggage Carrier'


def parse_accessory_type(value: any) -> AccessoryType:
    if type(value) == AccessoryType:
        return value

    if type(value) is not str:
        raise TypeError('Unexpected type error: Only pass AccessoryType or String values.')

    for accessoryType in AccessoryType:
        if accessoryType.value == value:
            return accessoryType


class Accessory(Item):
    _name: str = None
    _protective: bool = False
    _accessory_type: AccessoryType = None

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.cost = arguments['cost']
        self.damaged = arguments['damaged']
        self.is_rented = arguments['rented']
        self.name = arguments['name']
        self.is_protective = arguments['protective']
        self.accessory_type = arguments['accessory_type']

    def as_dict(self):
        accessory_dict = super().as_dict()

        accessory_dict['name'] = self.name
        accessory_dict['protective'] = self.is_protective
        accessory_dict['accessory_type'] = self.accessory_type.value

        return accessory_dict

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def is_protective(self) -> bool:
        return self._protective

    @is_protective.setter
    def is_protective(self, protective: bool) -> None:
        self._protective = protective

    @property
    def accessory_type(self) -> AccessoryType:
        return self._accessory_type

    @accessory_type.setter
    def accessory_type(self, accessory_type: any) -> None:
        self._accessory_type = parse_accessory_type(accessory_type)
