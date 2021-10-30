from enum import Enum

from item import Item
from person import Gender, parse_gender


class Color(Enum):
    BLACK = 'Black'
    ORANGE = 'Orange'
    RED = 'Red'
    SILVER = 'Silver'
    YELLOW = 'Yellow'
    BLUE = 'Blue'
    GREEN = 'Green'
    LIME = 'Lime'


def parse_color(value: any) -> Color:
    if type(value) == Color:
        return value

    if type(value) is not str:
        raise TypeError('Unexpected type error: Only pass Color or String values.')

    for color in Color:
        if color.value == value:
            return color


class Size(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'


def parse_size(value: any) -> Size:
    if type(value) == Size:
        return value

    if type(value) is not str:
        raise TypeError('Unexpected type error: Only pass Size or String values.')

    for size in Size:
        if size.value == value:
            return size


class Bike(Item):
    _build_for_gender: Gender = None
    _electric: bool = False
    _color: Color = None
    _size: Size = None
    _model: str = None

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.cost = arguments['cost']
        self.damaged = arguments['damaged']
        self.is_rented = arguments['rented']
        self.build_for_gender = arguments['build_for_gender']
        self.is_electric = arguments['electric']
        self.color = arguments['color']
        self.size = arguments['size']
        self.model = arguments['model']

    def as_dict(self):
        bike_dict = super().as_dict()

        bike_dict['build_for_gender'] = self.build_for_gender.value
        bike_dict['electric'] = self.is_electric
        bike_dict['color'] = self.color.value
        bike_dict['size'] = self.size.value
        bike_dict['model'] = self.model

        return bike_dict

    @property
    def build_for_gender(self) -> Gender:
        return self._build_for_gender

    @build_for_gender.setter
    def build_for_gender(self, gender: any) -> None:
        self._build_for_gender = parse_gender(gender)

    @property
    def is_electric(self) -> bool:
        return self._electric

    @is_electric.setter
    def is_electric(self, electric: bool) -> None:
        self._electric = electric

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, color: any) -> None:
        self._color = parse_color(color)

    @property
    def size(self) -> Size:
        return self._size

    @size.setter
    def size(self, size: any) -> None:
        self._size = parse_size(size)

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, model: str) -> None:
        self._model = model
