from enum import Enum

GENDER_KEY = 'gender'
FIRST_NAME_KEY = 'first_name'
LAST_NAME_KEY = 'last_name'


class Gender(Enum):
    MALE = 'Man'
    FEMALE = 'Vrouw'


def parse_gender(value: any) -> Gender:
    if type(value) == Gender:
        return value

    if type(value) is not str:
        raise TypeError('Unexpected type error: Only pass Gender or String values.')

    for gender in Gender:
        if gender.value == value:
            return gender


class Person:
    _first_name: str = None
    _last_name: str = None
    _gender: Gender = None

    def as_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender.value,
        }

    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def gender(self, gender: any):
        self._gender = parse_gender(gender)

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name
