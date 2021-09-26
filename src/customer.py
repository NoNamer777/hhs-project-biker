from person import Person
from gender import Gender


class Customer(Person):
    _regular_customer: bool = False
    _clumsy: bool = False

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.first_name = arguments['first_name']
        self.last_name = arguments['last_name']
        self.gender = Gender(arguments['gender'])
        self.is_regular_customer = arguments['regular_customer']
        self.is_clumsy = arguments['clumsy']

    def as_dict(self):
        customer_dict = super().as_dict()

        customer_dict['regular_customer'] = self.is_regular_customer
        customer_dict['clumsy'] = self.is_clumsy

        return customer_dict

    @property
    def is_regular_customer(self) -> bool:
        return self._regular_customer

    @is_regular_customer.setter
    def is_regular_customer(self, regular_customer) -> None:
        self._regular_customer = regular_customer

    @property
    def is_clumsy(self) -> bool:
        return self._clumsy

    @is_clumsy.setter
    def is_clumsy(self, clumsy) -> None:
        self._clumsy = clumsy
