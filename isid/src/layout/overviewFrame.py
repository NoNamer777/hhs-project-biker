from os import getcwd
from os.path import join
from tkinter import PhotoImage
from tkinter.constants import BOTH, END, YES, W
from tkinter.font import BOLD, Font
from tkinter.ttk import Frame, Label, Notebook, Treeview

from ..models import Item

KEY_HEADER_TEXT = 'header_text'
KEY_HEADERS = 'table_headers'
KEY_OBJECT_TYPE = 'object_type'


class OverviewFrame:
    def __init__(self, notebook: Notebook, **kwargs):
        print(f"Initializing Overview Frame for {kwargs.get(KEY_HEADER_TEXT).replace(' Overview', '')}")
        self._frame = Frame(notebook)

        # Create a smaller logo
        logo = PhotoImage(file=join(getcwd(), 'assets', 'images', 'biker-banner.png')).subsample(3, 3)

        logo_container = Label(self.frame, image=logo, borderwidth=1)
        logo_container.img = logo
        logo_container.grid(column=0, row=0, pady=8, columnspan=2)

        # Create a Header
        header_text = kwargs.get(KEY_HEADER_TEXT)
        header = Label(self.frame, text=header_text, font=Font(weight=BOLD))

        header.grid(row=1, column=1, columnspan=2, ipady=8)

        # Create a Text widget for showing the data
        headers = kwargs.get(KEY_HEADERS)

        self._overview = Treeview(self.frame, columns=headers)
        self._overview.grid(row=2, column=1, columnspan=2, padx=64)

        self.frame.grid_columnconfigure(2, weight=1)

        is_item = isinstance(kwargs.get(KEY_OBJECT_TYPE)(), Item)
        self._first_column = 'Brand' if is_item else 'Firstname'

        headers = tuple([self._first_column]) + headers

        # Create table columns and headers
        for idx, header in enumerate(headers):
            self.overview.heading(f'#{idx}', text=header, anchor=W)
            self.overview.column(f'#{idx}', anchor=W, minwidth=64, stretch=YES)

        self.frame.pack(fill=BOTH, expand=True)

    def insert_data(self, objects):
        """
        Inserts data into the Table widget
        :param objects: The data to insert
        """
        if len(objects) == 0:
            return

        for index, entry in enumerate(objects):
            print(f'Inserting {type(entry).__name__} data into overview Treeview widget: {entry.values()}')
            column_values = entry.values()

            self.overview.insert('', index=END, iid=index, text=column_values.pop(0), values=tuple(column_values))

        print()

    @property
    def frame(self):
        return self._frame

    @property
    def overview(self):
        return self._overview
