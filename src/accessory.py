from item import Item


class Accessory(Item):
    _name: str = None
    _protective: bool = False

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.cost = arguments['cost']
        self.damaged = arguments['damaged']
        self.is_rented = arguments['rented']
        self.name = arguments['name']
        self.is_protective = arguments['protective']

    def as_dict(self):
        accessory_dict = super().as_dict()

        accessory_dict['name'] = self.name
        accessory_dict['protective'] = self.is_protective

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
