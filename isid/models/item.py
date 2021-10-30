KEY_ITEM_BRAND = 'brand'
KEY_ITEM_PRICE = 'price'
KEY_ITEM_DEPOSIT = 'deposit'


class Item:
    def __init__(self, **kwargs):
        self.brand = kwargs.get(KEY_ITEM_BRAND)
        self.price = kwargs.get(KEY_ITEM_PRICE)
        self.deposit = kwargs.get(KEY_ITEM_DEPOSIT)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, deposit: float):
        self._deposit = deposit
