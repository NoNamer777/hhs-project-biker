from csv import DictReader
from os.path import join
from sqlite3 import connect, Row
from typing import Type

from ..models import Accessory, Bicycle, Customer, Employee


class DatabaseConnection:
    def __init__(self):
        self._connection = connect(join('assets', 'data', 'biker.db'))
        self._connection.row_factory = Row

        self._prepare_db()

    def _prepare_db(self):
        if self._are_tables_created():
            print('Database is already initialized. Skip database creation\n')
            return

        print('Initializing database\n')

        # Create tables
        self._connection.execute("""
            CREATE TABLE IF NOT EXISTS bicycle (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand VARCHAR(32) NOT NULL,
                price DECIMAL(6, 2) NOT NULL,
                deposit DECIMAL(6, 2) NOT NULL,
                bicycle_type VARCHAR(32) NOT NULL,
                CHECK (price >= 0),
                CHECK (deposit >= 0),
                CHECK (
                    bicycle_type = 'Electric' OR
                    bicycle_type = 'Regular' OR
                    bicycle_type = 'Male' OR
                    bicycle_type = 'Female'
                )
            );
        """)

        self._connection.execute("""
            CREATE TABLE IF NOT EXISTS accessory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand VARCHAR(64) NOT NULL,
                price DECIMAL(6, 2) NOT NULL,
                deposit DECIMAL(6, 2) NOT NULL,
                new_price DECIMAL(6, 2) NOT NULL,
                accessory_type VARCHAR(32) NOT NULL,
                CONSTRAINT valid_price_check CHECK (price >= 0),
                CONSTRAINT valid_deposit_check CHECK (deposit >= 0),
                CONSTRAINT valid_accessory_type_check CHECK (
                    accessory_type = 'Child seat' OR
                    accessory_type = 'Helmet' OR
                    accessory_type = 'Bicycle bag'
                )
            );
        """)

        self._connection.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname VARCHAR(64) NOT NULL,
                lastname VARCHAR(64) NOT NULL,
                street VARCHAR(124) NOT NULL,
                house_number INTEGER NOT NULL,
                house_number_addition VARCHAR(8),
                zip_code VARCHAR(8) NOT NULL,
                city VARCHAR(64) NOT NULL,
                country VARCHAR(64) NOT NULL,
                CONSTRAINT valid_zip_code_check CHECK (zip_code NOT LIKE '[1-9][0-9][0-9][0-9] [A-Z][A-Z]')
            );
        """)

        self._connection.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname VARCHAR(64) NOT NULL,
                lastname VARCHAR(64) NOT NULL,
                username VARCHAR(64) NOT NULL,
                role VARCHAR(64) NOT NULL,
                CONSTRAINT unique_username UNIQUE (username)
            );
        """)

        self._connection.commit()

        print('Database initialized')
        print('Inserting data into database\n')

        # Pass the CSV data to the db
        self._insert_date(_read_data(join('assets', 'data', 'accessories.csv'), Accessory), 'accessory', Accessory)
        self._insert_date(_read_data(join('assets', 'data', 'bicycles.csv'), Bicycle), 'bicycle', Bicycle)
        self._insert_date(_read_data(join('assets', 'data', 'customers.csv'), Customer), 'customer', Customer)
        self._insert_date(_read_data(join('assets', 'data', 'employees.csv'), Employee), 'employee', Employee)

        print('Database is initialized\n')

    def get_data(self, table_name: str, object_type: Type) -> list:
        """
        Selects all data from a table
        :param table_name: the name of the table to select the data from
        :param object_type: the type to transform the selected data to
        :return:
        """
        print('Fetching data from the database')
        objects = []
        cursor = self._connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')

        rows = cursor.fetchall()

        for row in rows:
            print(f'Fetched {object_type.__name__} from "{table_name}" table: {dict(row)}')
            objects.append(object_type(dict(row)))

        print()

        return objects

    def close_connection(self) -> None:
        self._connection.close()

    def _are_tables_created(self) -> bool:
        """
        Checks whether there are already tables present in the database file.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table';")

        number_of_tables = dict(cursor.fetchall()[0]).get('count(*)')

        return number_of_tables > 0

    def _insert_date(self, objects, table_name: str, object_type: Type) -> None:
        """
        Inserts data into a database table
        :param objects: the data to insert
        :param table_name: the name of the table to insert the data into
        :param object_type: the type of the data objects
        """
        columns = object_type.attributes()
        # Determines how many attributes/ values to insert for the provided object_type
        markers = '?, ' * len(columns)
        markers = markers[0: len(markers) - 2]

        # Makes sure the column names used are all lower cased and spaces are replaced with '_'
        for index, column in enumerate(columns):
            columns[index] = column.lower().replace(' ', '_')

        for entry in objects:
            print(f'inserting {object_type.__name__} into the "{table_name}" table: {tuple(entry.values())}')
            self._connection.execute(
                f'INSERT INTO {table_name} {tuple(columns)} VALUES ({markers});',
                tuple(entry.values())
            )
        print()

        self._connection.commit()


def _read_data(location: str, object_type: Type) -> list:
    """
    Read data from a CSV-file and transforms the raw data into a Python class and returns the data into a list
    :param location: the location of the CSV-file to read
    :param object_type: The Python class to transform the data into
    """
    objects = []

    print(f'Reading CSV-file at {location}')

    with open(location, 'r') as data:
        reader = DictReader(data)

        for row in reader:
            print(f'Creating {object_type.__name__} instance from the CSV-file: {row}')
            objects.append(object_type(row))

        print()

    return objects
