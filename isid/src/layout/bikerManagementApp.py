from os import chdir, getcwd
from os.path import join
from pathlib import Path
from tkinter import Tk, PhotoImage
from tkinter.constants import BOTH
from tkinter.ttk import Notebook, Frame, Label

from .overviewFrame import OverviewFrame
from ..models import Bicycle, Accessory, Employee, Customer

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
        bicycle_frame = OverviewFrame(
            self.notebook,
            header_text=HEADER_BICYCLE_TEXT,
            data_location=join('assets', 'data', 'bicycles.csv'),
            data_type=Bicycle
        )
        self.notebook.add(bicycle_frame.frame, text=TAB_BICYCLE_TEXT)

        accessory_frame = OverviewFrame(
            self.notebook,
            header_text=HEADER_ACCESSORY_TEXT,
            data_location=join('assets', 'data', 'accessories.csv'),
            data_type=Accessory
        )
        self.notebook.add(accessory_frame.frame, text=TAB_ACCESSORY_TEXT)

        employee_frame = OverviewFrame(
            self.notebook,
            header_text=HEADER_EMPLOYEE_TEXT,
            data_location=join('assets', 'data', 'employees.csv'),
            data_type=Employee,
            data_headers=EMPLOYEE_HEADERS
        )
        self.notebook.add(employee_frame.frame, text=TAB_EMPLOYEE_TEXT)

        customer_frame = OverviewFrame(
            self.notebook,
            header_text=HEADER_CUSTOMER_TEXT,
            data_location=join('assets', 'data', 'customers.csv'),
            data_type=Customer,
            data_headers=CUSTOMER_HEADERS
        )
        self.notebook.add(customer_frame.frame, text=TAB_CUSTOMER_TEXT)

    def _create_main_menu_frame(self):
        """
        Create the Main menu frame with a logo and an area to show some text.
        """
        self._main_menu_frame = Frame(self._notebook)

        # Add the logo to the main menu frame
        banner = self._create_banner(self._main_menu_frame)
        banner.pack()

        self._main_menu_frame.pack(fill=BOTH, expand=True)
        self._notebook.add(self._main_menu_frame, text=TAB_MAIN_MENU_TEXT)

    def _create_banner(self, parent: Frame) -> Label:
        """
        Creates a logo.
        :param parent: Where the logo will be added to.
        """
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
