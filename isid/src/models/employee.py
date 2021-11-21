from .person import Person

KEY_EMPLOYEE_ROLE = 'role'
KEY_EMPLOYEE_USERNAME = 'username'
EMPLOYEE_HEADERS = ('Lastname', 'Role', 'Username')

class Employee(Person):
    def __init__(self, data: dict):
        super().__init__(data)

        if data is None:
            return

        self.role = data.get(KEY_EMPLOYEE_ROLE)
        self.username = data.get(KEY_EMPLOYEE_USERNAME)

    def values(self):
        values = super().values()
        values.extend([self.role, self.username])

        return values

    def attributes(self):
        attributes = super().attributes()
        attributes.extend(['Role', 'Username'])

        return attributes

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
