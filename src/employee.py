from enum import Enum
from person import Person


class EmployeeRole(Enum):
    SERVICE_DESK = 'Service Desk'
    REPAIR = 'Repair'
    ADMINISTRATION = 'Administration'
    HUMAN_RESOURCES = 'Human Resources'


def parse_employee_role(value: any) -> EmployeeRole:
    if type(value) == EmployeeRole:
        return value

    if type(value) is not str:
        raise TypeError('Unexpected type error: Only pass EmployeeRole or String values.')

    for role in EmployeeRole:
        if role.value == value:
            return role


class Employee(Person):
    _hourly_wage: float = None
    _role: EmployeeRole = None

    def __init__(self, arguments: dict = None):
        if arguments is None:
            return

        self.first_name = arguments['first_name']
        self.last_name = arguments['last_name']
        self.gender = arguments['gender']
        self.hourly_wage = arguments['hourly_wage']
        self.role = arguments['role']

    def as_dict(self):
        employee_dict = super().as_dict()

        employee_dict['hourly_wage'] = self.hourly_wage
        employee_dict['role'] = self.role.value

        return employee_dict

    @property
    def hourly_wage(self) -> float:
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, hourly_wage: float) -> None:
        self._hourly_wage = hourly_wage

    @property
    def role(self) -> EmployeeRole:
        return self._role

    @role.setter
    def role(self, role: any) -> None:
        self._role = parse_employee_role(role)
