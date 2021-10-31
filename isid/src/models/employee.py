from .person import Person

KEY_EMPLOYEE_ROLE = 'role'
KEY_EMPLOYEE_USERNAME = 'username'


class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.role = kwargs.get(KEY_EMPLOYEE_ROLE)
        self.username = kwargs.get(KEY_EMPLOYEE_USERNAME)

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role: str):
        self._role = role

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username
