import csv
from enum import Enum
from tabulate import tabulate

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


def write_data(data_src: str, data: []) -> None:
    with open(data_src, 'a+', newline='') as destination_file:
        field_names = list(data[0].as_dict().keys())

        writer = csv.DictWriter(destination_file, field_names)

        for entry in data:
            writer.writerow(entry.as_dict())

        destination_file.close()


def read_data(data_src: str, data_type) -> []:
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


def print_in_table(data: [], data_type) -> None:
    if data_type not in ItemDataType and data_type not in PersonDataType:
        raise AttributeError(
            f"'{data_type}' is not a valid type of data to create. "
            f"Please use one of {ItemDataType} or {PersonDataType}"
        )

    headers = list(data[0].as_dict().keys())
    table_data = []

    for entry in data:
        table_data.append(list(entry.as_dict().values()))

    print(tabulate(table_data, headers, tablefmt='fancy_grid', floatfmt='.2f'))
    print()


def main() -> None:
    customers = read_data('../data/customers.csv', PersonDataType.CUSTOMER)
    employees = read_data('../data/employees.csv', PersonDataType.EMPLOYEE)
    bikes = read_data('../data/bikes.csv', ItemDataType.BIKE)
    accessories = read_data('../data/accessories.csv', ItemDataType.ACCESSORY)

    print_in_table(customers, PersonDataType.CUSTOMER)
    print_in_table(employees, PersonDataType.EMPLOYEE)
    print_in_table(bikes, ItemDataType.BIKE)
    print_in_table(accessories, ItemDataType.ACCESSORY)


if __name__ == '__main__':
    main()
