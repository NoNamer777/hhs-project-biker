from person import Person


class Customer(Person):
    _regular_customer: bool = False
    _insured: bool = False

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.first_name = arguments['first_name']
        self.last_name = arguments['last_name']
        self.gender = arguments['gender']
        self.is_regular_customer = arguments['regular_customer']
        self.is_insured = arguments['insured']

    def as_dict(self):
        customer_dict = super().as_dict()

        customer_dict['regular_customer'] = self.is_regular_customer
        customer_dict['insured'] = self.is_insured

        return customer_dict

    @property
    def is_regular_customer(self) -> bool:
        return self._regular_customer

    @is_regular_customer.setter
    def is_regular_customer(self, regular_customer) -> None:
        self._regular_customer = regular_customer

    @property
    def is_insured(self) -> bool:
        return self._insured

    @is_insured.setter
    def is_insured(self, insured) -> None:
        self._insured = insured
