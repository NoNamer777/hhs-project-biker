from os import getcwd
from os.path import join
from tkinter import Text, PhotoImage
from tkinter.constants import BOTH, SOLID, END, DISABLED
from tkinter.font import BOLD, Font
from tkinter.ttk import Frame, Label, Notebook

from ..utils import read_data

KEY_HEADER_TEXT = 'header_text'
KEY_DATA_LOCATION = 'data_location'
KEY_DATA_TYPE = 'data_type'
KEY_DATA_HEADERS = 'data_headers'
WIDTH_OVERVIEW = 136


class OverviewFrame:
    def __init__(self, notebook: Notebook, **kwargs):
        self._frame = Frame(notebook)

        logo = PhotoImage(file=join(getcwd(), 'assets', 'images', 'biker-banner.png')).subsample(3, 3)

        logo_container = Label(self.frame, image=logo, borderwidth=1)
        logo_container.img = logo
        logo_container.grid(column=0, row=0, pady=8, columnspan=2)

        header_text = kwargs.get(KEY_HEADER_TEXT)
        header = Label(self.frame, text=header_text, font=Font(weight=BOLD))

        header.grid(row=1, column=1, columnspan=2, ipady=8)

        self._overview = Text(self.frame, borderwidth=1, relief=SOLID)
        self.overview.config(width=WIDTH_OVERVIEW)
        self._overview.grid(row=2, column=1, columnspan=2)

        self.frame.grid_columnconfigure(2, weight=1)

        objects = read_data(kwargs.get(KEY_DATA_LOCATION), kwargs.get(KEY_DATA_TYPE))
        headers = kwargs.get(KEY_DATA_HEADERS)

        self._insert_data(objects, headers)

        self.overview['state'] = DISABLED

        self.frame.pack(fill=BOTH, expand=True)

    def _insert_data(self, objects, headers):
        formatted_headers = self._format_line(headers)
        self.overview.insert(END, formatted_headers)

        line = '-' * WIDTH_OVERVIEW + '\n'
        self.overview.insert(END, line)

        for entry in objects:
            formatted_entry = self._format_line(entry.values())
            self.overview.insert(END, formatted_entry)

    def _format_line(self, data) -> str:
        number_of_items = len(data)
        space_per_item = (WIDTH_OVERVIEW // number_of_items) - 2
        formatted_line = ''

        for idx in range(0, len(data)):
            entry = data[idx]

            formatted_line += f'{str(entry).center(space_per_item)}'

            if idx is not len(data) - 1:
                formatted_line += ' |'

        return formatted_line + '\n'

    @property
    def frame(self):
        return self._frame

    @property
    def overview(self):
        return self._overview
