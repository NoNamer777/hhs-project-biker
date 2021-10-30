import csv
from enum import Enum
from os import getcwd, chdir

from accessory import Accessory
from bike import Bike
from customer import Customer
from employee import Employee


class PersonDataType(Enum):
    CUSTOMER = 0
    EMPLOYEE = 1


class ItemDataType(Enum):
    BIKE = 0
    ACCESSORY = 1


def read_data(data_src: str, data_type: PersonDataType or ItemDataType):
    if data_type not in ItemDataType and data_type not in PersonDataType:
        raise AttributeError(
            f"'{data_type}' is not a valid type of data to create. "
            f"Please use one of {ItemDataType} or {PersonDataType}"
        )

    objects = []

    with open(data_src, 'r') as source_file:
        reader = csv.DictReader(source_file)

        for row in reader:
            if data_type == PersonDataType.CUSTOMER:
                objects.append(Customer(row))
            if data_type == PersonDataType.EMPLOYEE:
                objects.append(Employee(row))
            if data_type == ItemDataType.BIKE:
                objects.append(Bike(row))
            if data_type == ItemDataType.ACCESSORY:
                objects.append(Accessory(row))

    return objects


def print_in_table(data, data_type: PersonDataType or ItemDataType) -> None:
    if data_type not in ItemDataType and data_type not in PersonDataType:
        raise AttributeError(
            f"'{data_type}' is not a valid type of data to create. "
            f"Please use one of {ItemDataType} or {PersonDataType}"
        )

    headers = list(data[0].as_dict().keys())
    print(str(data_type.name).capitalize())
    print(f"{('-' * 23) * len(headers)}")

    for idx in range(0, len(headers)):
        header = headers[idx]
        headers[idx] = header.replace('_', ' ').capitalize()

    print_row(headers, True)

    for entry in data:
        print_row(list(entry.as_dict().values()))

    print()


def print_row(data, bold: bool = False) -> None:
    for entry in data:
        print(end='| ')

        if bold:
            print(f'\033[1m{entry:^20}\033[0m', end=' ')
        else:
            print(f'{entry:^20}', end=' ')

    print(end='|')
    print()
    print(f"{('-' * 23) * len(data)}")


def main() -> None:
    if getcwd().endswith('src'):
        chdir('../')

    customers = read_data('data/customers.csv', PersonDataType.CUSTOMER)
    employees = read_data('data/employees.csv', PersonDataType.EMPLOYEE)
    bikes = read_data('data/bikes.csv', ItemDataType.BIKE)
    accessories = read_data('data/accessories.csv', ItemDataType.ACCESSORY)

    print_in_table(customers, PersonDataType.CUSTOMER)
    print_in_table(employees, PersonDataType.EMPLOYEE)
    print_in_table(bikes, ItemDataType.BIKE)
    print_in_table(accessories, ItemDataType.ACCESSORY)


if __name__ == '__main__':
    main()
