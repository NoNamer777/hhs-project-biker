from person import Person
from gender import Gender

EMPLOYEE_ROLES = [
    'service desk',
    'repair',
    'administration',
    'human resources'
]


class Employee(Person):
    _hourly_wage: float = None
    _role: str = None

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.first_name = arguments['first_name']
        self.last_name = arguments['last_name']
        self.gender = Gender(arguments['gender'])
        self.hourly_wage = arguments['hourly_wage']
        self.role = arguments['role']

    def as_dict(self):
        employee_dict = super().as_dict()

        employee_dict['hourly_wage'] = self.hourly_wage
        employee_dict['role'] = self.role

        return employee_dict

    @property
    def hourly_wage(self) -> float:
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, hourly_wage: float) -> None:
        self._hourly_wage = hourly_wage

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, role: str) -> None:
        if role not in EMPLOYEE_ROLES:
            raise AttributeError(f"'{role}' is not a valid role for employees. {EMPLOYEE_ROLES}")

        self._role = role
