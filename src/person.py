from gender import Gender

GENDER_KEY = 'gender'
FIRST_NAME_KEY = 'first_name'
LAST_NAME_KEY = 'last_name'


class Person:
    _first_name: str = None
    _last_name: str = None
    _gender: Gender = None

    def as_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': None if self.gender is None else self.gender.value,
        }

    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def gender(self, gender: Gender):
        self._gender = gender

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