import csv
from tabulate import tabulate

from customer import Customer
from employee import Employee
from bike import Bike
from accessory import Accessory
from gender import Gender

ALLOWED_PERSON_DATA_TYPE = [
    'customer',
    'employee'
]

ALLOWED_ITEM_DATA_TYPE = [
    'bike',
    'accessory'
]


def write_data(data_src: str, data: []) -> None:
    with open(data_src, 'a+', newline='') as destination_file:
        field_names = list(data[0].as_dict().keys())

        writer = csv.DictWriter(destination_file, field_names)

        for entry in data:
            writer.writerow(entry.as_dict())

        destination_file.close()


def create_customers() -> None:
    customers = []

    customer_1 = Customer()
    customer_1.first_name = 'Anakin'
    customer_1.last_name = 'Skywalker'
    customer_1.gender = Gender('Man')
    customer_1.is_regular_customer = True
    customer_1.is_clumsy = False
    customers.append(customer_1)

    customer_2 = Customer()
    customer_2.first_name = 'Ahsoko'
    customer_2.last_name = 'Tano'
    customer_2.gender = Gender('Vrouw')
    customer_2.is_regular_customer = False
    customer_2.is_clumsy = False
    customers.append(customer_2)

    customer_3 = Customer()
    customer_3.first_name = 'Padme'
    customer_3.last_name = 'Amidala'
    customer_3.gender = Gender('Vrouw')
    customer_3.is_regular_customer = True
    customer_3.is_clumsy = True
    customers.append(customer_3)

    customer_4 = Customer()
    customer_4.first_name = 'Obi-wan'
    customer_4.last_name = 'Kenobi'
    customer_4.gender = Gender('Man')
    customer_4.is_regular_customer = False
    customer_4.is_clumsy = False
    customers.append(customer_4)

    write_data('../data/customers.csv', customers)


def create_employees() -> None:
    employees = []

    employee_1 = Employee()
    employee_1.first_name = 'Wim'
    employee_1.last_name = 'Eggink'
    employee_1.gender = Gender('Man')
    employee_1.hourly_wage = 8.52
    employee_1.role = 'repair'
    employees.append(employee_1)

    employee_2 = Employee()
    employee_2.first_name = 'Marloes'
    employee_2.last_name = 'Swaan'
    employee_2.gender = Gender('Vrouw')
    employee_2.hourly_wage = 7.23
    employee_2.role = 'service desk'
    employees.append(employee_2)

    employee_3 = Employee()
    employee_3.first_name = 'Karlijn'
    employee_3.last_name = 'Timan'
    employee_3.gender = Gender('Vrouw')
    employee_3.hourly_wage = 9.18
    employee_3.role = 'human resources'
    employees.append(employee_3)

    employee_4 = Employee()
    employee_4.first_name = 'Maaike'
    employee_4.last_name = 'Weterink'
    employee_4.gender = Gender('Vrouw')
    employee_4.hourly_wage = 8.43
    employee_4.role = 'administration'
    employees.append(employee_4)

    write_data('../data/employees.csv', employees)


def create_bikes() -> None:
    bikes = []

    bike_1 = Bike()
    bike_1.cost = 125.68
    bike_1.damaged = False
    bike_1.rented = True
    bike_1.build_for_gender = Gender('Man')
    bike_1.is_electric = False
    bikes.append(bike_1)

    bike_2 = Bike()
    bike_2.cost = 246.38
    bike_2.damaged = False
    bike_2.rented = False
    bike_2.build_for_gender = Gender('Vrouw')
    bike_2.is_electric = True
    bikes.append(bike_2)

    bike_3 = Bike()
    bike_3.cost = 268.17
    bike_3.damaged = True
    bike_3.rented = False
    bike_3.build_for_gender = Gender('Vrouw')
    bike_3.is_electric = False
    bikes.append(bike_3)

    bike_4 = Bike()
    bike_4.cost = 136.46
    bike_4.damaged = True
    bike_4.rented = False
    bike_4.build_for_gender = Gender('Man')
    bike_4.is_electric = True
    bikes.append(bike_4)

    write_data('../data/bikes.csv', bikes)


def create_accessories() -> None:
    accessories = []

    accessory_1 = Accessory()
    accessory_1.cost = 12.03
    accessory_1.damaged = True
    accessory_1.rented = False
    accessory_1.name = 'Helm'
    accessory_1.protective = True
    accessories.append(accessory_1)

    accessory_2 = Accessory()
    accessory_2.cost = 5.30
    accessory_2.damaged = False
    accessory_2.rented = True
    accessory_2.name = 'Handschoenen'
    accessory_2.protective = True
    accessories.append(accessory_2)

    accessory_3 = Accessory()
    accessory_3.cost = 40.2
    accessory_3.damaged = False
    accessory_3.rented = True
    accessory_3.name = 'Kinderzittje'
    accessory_3.protective = False
    accessories.append(accessory_3)

    accessory_4 = Accessory()
    accessory_4.cost = 4.67
    accessory_4.damaged = False
    accessory_4.rented = False
    accessory_4.name = 'Regenjas'
    accessory_4.protective = False
    accessories.append(accessory_4)

    write_data('../data/accessories.csv', accessories)


def read_data(data_src: str, data_type: str) -> []:
    if data_type.lower() not in ALLOWED_PERSON_DATA_TYPE and data_type.lower() not in ALLOWED_ITEM_DATA_TYPE:
        raise AttributeError(
            f"'{data_type}' is not a valid type of data to create. "
            f"Please use one of {ALLOWED_PERSON_DATA_TYPE} or {ALLOWED_ITEM_DATA_TYPE}"
        )

    objects = []

    with open(data_src, 'r') as source_file:
        reader = csv.DictReader(source_file)

        for row in reader:
            if data_type.lower() == ALLOWED_PERSON_DATA_TYPE[0]:
                objects.append(Customer(row))
            if data_type.lower() == ALLOWED_PERSON_DATA_TYPE[1]:
                objects.append(Employee(row))
            if data_type.lower() == ALLOWED_ITEM_DATA_TYPE[0]:
                objects.append(Bike(row))
            if data_type.lower() == ALLOWED_ITEM_DATA_TYPE[1]:
                objects.append(Accessory(row))

    return objects


def print_in_table(data: [], data_type: str) -> None:
    if data_type.lower() not in ALLOWED_PERSON_DATA_TYPE and data_type.lower() not in ALLOWED_ITEM_DATA_TYPE:
        raise AttributeError(
            f"'{data_type}' is not a valid type of data to create. "
            f"Please use one of {ALLOWED_PERSON_DATA_TYPE} or {ALLOWED_ITEM_DATA_TYPE}"
        )

    headers = list(data[0].as_dict().keys())
    table_data = []

    for entry in data:
        table_data.append(list(entry.as_dict().values()))

    print(tabulate(table_data, headers, tablefmt='fancy_grid', floatfmt='.2f'))
    print()


def clean_up():
    with open('../data/customers.csv', 'w') as customers_file:
        writer = csv.writer(customers_file)
        customer = Customer()

        writer.writerow(list(customer.as_dict()))

    customers_file.close()

    with open('../data/employees.csv', 'w') as employees_file:
        writer = csv.writer(employees_file)
        employee = Employee()

        writer.writerow(list(employee.as_dict().keys()))

    employees_file.close()

    with open('../data/bikes.csv', 'w') as bikes_file:
        writer = csv.writer(bikes_file)
        bike = Bike()

        writer.writerow(list(bike.as_dict().keys()))

    bikes_file.close()

    with open('../data/accessories.csv', 'w') as accessories_file:
        writer = csv.writer(accessories_file)
        accessory = Accessory()

        writer.writerow(list(accessory.as_dict().keys()))

    accessories_file.close()


def main() -> None:
    create_customers()
    create_employees()
    create_bikes()
    create_accessories()

    customers = read_data('../data/customers.csv', 'customer')
    employees = read_data('../data/employees.csv', 'employee')
    bikes = read_data('../data/bikes.csv', 'bike')
    accessories = read_data('../data/accessories.csv', 'accessory')

    print_in_table(customers, 'customer')
    print_in_table(employees, 'employee')
    print_in_table(bikes, 'bike')
    print_in_table(accessories, 'accessory')

    clean_up()


if __name__ == '__main__':
    main()
