class Gender:

    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        if value == MALE_GENDER_CONST or value == FEMALE_GENDER_CONST:
            self._value = value

            return

        raise AttributeError()


MALE_GENDER_CONST = 'Man'
FEMALE_GENDER_CONST = 'Vrouw'
