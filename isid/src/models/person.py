KEY_PERSON_FIRST_NAME = 'firstname'
KEY_PERSON_LAST_NAME = 'lastname'


class Person:
    def __init__(self, data: dict):
        if data is None:
            return

        self.firstname = data.get(KEY_PERSON_FIRST_NAME)
        self.lastname = data.get(KEY_PERSON_LAST_NAME)

    def values(self):
        return [self.firstname, self.lastname]

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self._lastname = lastname
