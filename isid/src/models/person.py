KEY_PERSON_FIRST_NAME = 'firstname'
KEY_PERSON_LAST_NAME = 'lastname'


class Person:
    def __init__(self, **kwargs):
        self.firstname = kwargs.get(KEY_PERSON_FIRST_NAME)
        self.lastname = kwargs.get(KEY_PERSON_LAST_NAME)

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
