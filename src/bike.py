from item import Item
from gender import Gender


class Bike(Item):
    _build_for_gender: Gender = None
    _electric: bool = False

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.cost = arguments['cost']
        self.damaged = arguments['damaged']
        self.is_rented = arguments['rented']
        self.build_for_gender = arguments['build_for_gender']
        self.is_electric = arguments['electric']

    def as_dict(self):
        bike_dict = super().as_dict()

        bike_dict['build_for_gender'] = self.build_for_gender
        bike_dict['electric'] = self.is_electric

        return bike_dict

    @property
    def build_for_gender(self) -> Gender:
        return self._build_for_gender

    @build_for_gender.setter
    def build_for_gender(self, gender: Gender) -> None:
        self._build_for_gender = gender

    @property
    def is_electric(self) -> bool:
        return self._electric

    @is_electric.setter
    def is_electric(self, electric: bool) -> None:
        self._electric = electric
