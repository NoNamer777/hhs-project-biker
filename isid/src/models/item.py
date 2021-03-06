KEY_ITEM_BRAND = 'brand'
KEY_ITEM_PRICE = 'price'
KEY_ITEM_DEPOSIT = 'deposit'


class Item:
    @classmethod
    def attributes(cls):
        return ['Brand', 'Price', 'Deposit']

    def __init__(self, data: dict = None):
        if data is None:
            return

        self.brand = data.get(KEY_ITEM_BRAND)
        self.price = data.get(KEY_ITEM_PRICE)
        self.deposit = data.get(KEY_ITEM_DEPOSIT)

    def values(self):
        return [self.brand, self.price, self.deposit]

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
