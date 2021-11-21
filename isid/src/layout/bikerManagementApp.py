from os import chdir, getcwd
from os.path import join
from pathlib import Path
from tkinter import Tk, PhotoImage
from tkinter.constants import BOTH
from tkinter.ttk import Notebook, Frame, Label, Button
from typing import Type

from ..models import \
    Bicycle,\
    Accessory,\
    Customer,\
    Employee,\
    BICYCLE_HEADERS,\
    ACCESSORY_HEADERS,\
    CUSTOMER_HEADERS,\
    EMPLOYEE_HEADERS
from .overviewFrame import OverviewFrame
from ..utils import DatabaseConnection

WINDOW_TITLE = 'Biker Management'
WINDOW_DEFAULT_WIDTH = 1152
WINDOW_DEFAULT_HEIGHT = 600
TAB_MAIN_MENU_TEXT = 'Main Menu'
TAB_BICYCLE_TEXT = 'Bicycles'
HEADER_BICYCLE_TEXT = 'Bicycles Overview'
TAB_ACCESSORY_TEXT = 'Accessories'
HEADER_ACCESSORY_TEXT = 'Accessories Overview'
TAB_EMPLOYEE_TEXT = 'Employees'
HEADER_EMPLOYEE_TEXT = 'Employees Overview'
TAB_CUSTOMER_TEXT = 'Customers'
HEADER_CUSTOMER_TEXT = 'Customers Overview'

# Get the current file location of this file
FILE_LOCATION = Path(__file__)

# Change the working directory of the Python script to where the project root would be
chdir(FILE_LOCATION.parent.parent.parent)


class BikerManagementApp:
    def __init__(self):
        # Create and configure the application window
        self._app = Tk()
        self._app.title(WINDOW_TITLE)
        self._app.minsize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT)

        self._notebook = Notebook(self.app)

        # Make sure the notebook uses all available space of the application window
        self._notebook.pack(expand=True, fill=BOTH)

        self._create_main_menu_frame()

        # Create frames for the individual entities
        print('Creating tabs and frame for managed entities')
        self._add_overview_frame(
            OverviewFrame(
                self.notebook,
                header_text=HEADER_ACCESSORY_TEXT,
                table_headers=ACCESSORY_HEADERS,
                object_type=Accessory
            ),
            TAB_ACCESSORY_TEXT,
            Accessory
        )
        self._add_overview_frame(
            OverviewFrame(
                self.notebook,
                header_text=HEADER_BICYCLE_TEXT,
                table_headers=BICYCLE_HEADERS,
                object_type=Bicycle
            ),
            TAB_BICYCLE_TEXT,
            Bicycle
        )
        self._add_overview_frame(
            OverviewFrame(
                self.notebook,
                header_text=HEADER_CUSTOMER_TEXT,
                table_headers=CUSTOMER_HEADERS,
                object_type=Customer
            ),
            TAB_CUSTOMER_TEXT,
            Customer
        )
        self._add_overview_frame(
            OverviewFrame(
                self.notebook,
                header_text=HEADER_EMPLOYEE_TEXT,
                table_headers=EMPLOYEE_HEADERS,
                object_type=Employee
            ),
            TAB_EMPLOYEE_TEXT,
            Employee
        )
        print()

    def _create_main_menu_frame(self) -> None:
        """
        Create the Main menu frame with a logo and an area to show some text.
        """
        print('Creating main menu frame')
        self._main_menu_frame = Frame(self._notebook)

        # Add the logo to the main menu frame
        banner = self._create_banner(self._main_menu_frame)
        banner.pack()

        self._main_menu_frame.pack(fill=BOTH, expand=True)
        self._notebook.add(self._main_menu_frame, text=TAB_MAIN_MENU_TEXT)

    def _add_overview_frame(self, frame: OverviewFrame, tab_text: str, object_type: Type) -> None:
        self.notebook.add(frame.frame, text=tab_text)

        # Add a button to initialize the data of a specific object type
        load_object_data_button = Button(
            self._main_menu_frame,
            text=f'Initialize {tab_text} data',
            command=lambda: self._initialize_data(
                frame,
                object_type.__name__.lower(),
                object_type,
                load_object_data_button,
            )
        )
        load_object_data_button.pack()

    def _initialize_data(self, frame: OverviewFrame, table_name: str, object_type: Type, button: Button) -> None:
        """
        Gets the data of a specific type from the database and puts them in the Treeview widget of the Overviewframe.
        Also navigates to the tab when the task is done, and disable the button to prevent one entry to be shown
        multiple times in the table.
        """
        frame.insert_data(self._database_connection.get_data(table_name, object_type))
        print(f'Navigating to {object_type.__name__} Overview Frame\n')
        self._notebook.select(frame.frame)

        button.config(state='disabled')

    def _create_banner(self, parent: Frame) -> Label:
        """
        Creates a logo.
        :param parent: Where the logo will be added to.
        """
        print('Create the logo')
        # Use the image located at ../assets/images/biker-banner.png
        banner = PhotoImage(file=join(getcwd(), 'assets', 'images', 'biker-banner.png'))

        banner_container = Label(parent, image=banner)
        banner_container.img = banner

        return banner_container

    @property
    def app(self) -> Tk:
        return self._app

    @property
    def notebook(self) -> Notebook:
        return self._notebook
