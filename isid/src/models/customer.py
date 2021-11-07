from .person import Person

KEY_CUSTOMER_STREET = 'street'
KEY_CUSTOMER_HOUSE_NUMBER = 'house_number'
KEY_CUSTOMER_HOUSE_NUMBER_ADDITION = 'house_number_add'
KEY_CUSTOMER_ZIP_CODE = 'zip_code'
KEY_CUSTOMER_CITY = 'city'
KEY_CUSTOMER_COUNTRY = 'country'
MIN_LENGTH_ZIP_CODE = 6
MAX_LENGTH_ZIP_CODE = 7


class Customer(Person):
    def __init__(self, data: dict):
        super().__init__(data)

        if data is None:
            return

        self.street = data.get(KEY_CUSTOMER_STREET)
        self.house_number = data.get(KEY_CUSTOMER_HOUSE_NUMBER)
        self.house_number_addition = data.get(KEY_CUSTOMER_HOUSE_NUMBER_ADDITION)
        self.zip_code = data.get(KEY_CUSTOMER_ZIP_CODE)
        self.city = data.get(KEY_CUSTOMER_CITY)
        self.country = data.get(KEY_CUSTOMER_COUNTRY)

    def values(self):
        values = super().values()
        values.extend([
            self.street,
            self.house_number,
            self.house_number_addition,
            self.zip_code,
            self.city,
            self.country
        ])

        return values

    def attributes(self):
        attributes = super().attributes()
        attributes.extend(['Street', 'House number', 'Addition', 'Zip code', 'City', 'Country'])

        return attributes

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street: str):
        self._street = street

    @property
    def house_number(self):
        return self._house_number

    @house_number.setter
    def house_number(self, house_number: int):
        if isinstance(house_number, str) and not house_number.isnumeric():
            raise ValueError(f'Expected Customer house number to a number, but received {house_number}')

        self._house_number = int(house_number)

    @property
    def house_number_addition(self):
        return self._house_number_addition

    @house_number_addition.setter
    def house_number_addition(self, house_number_addition: str):
        self._house_number_addition = house_number_addition

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code: str):
        # If the provided zip code is longer then 7 or shorter then 6 characters
        # the zip code is invalid
        if len(zip_code) > MAX_LENGTH_ZIP_CODE or len(zip_code) < MIN_LENGTH_ZIP_CODE:
            raise AttributeError(f'{zip_code} is not a valid zip code')

        # If the zip code has a length of 7 and the 5th character is not a space
        # the zip code is invalid
        if len(zip_code) is MAX_LENGTH_ZIP_CODE and not zip_code[4].isspace():
            raise AttributeError(f'{zip_code} is not a valid zip code')

        # Check if the first 4 characters are numbers
        for index in range(0, 3):
            character = zip_code[index]

            if not character.isnumeric():
                raise AttributeError(f'{zip_code} is not a valid zip code')

        # Check if the last 2 characters are letters
        for index in range(0, 1):
            has_space = zip_code.find(' ') != -1

            character = zip_code[index + (5 if not has_space else 6)]

            if not character.isalpha():
                raise AttributeError(f'{zip_code} is not a valid zip code')

        self._zip_code = zip_code

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country: str):
        self._country = country

