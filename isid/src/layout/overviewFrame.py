from os import getcwd
from os.path import join
from tkinter import Text, PhotoImage
from tkinter.constants import BOTH, SOLID
from tkinter.font import BOLD, Font
from tkinter.ttk import Frame, Label, Notebook

KEY_HEADER_TEXT = 'header_text'
KEY_DATA_LOCATION = 'data_location'
KEY_DATA_TYPE = 'data_type'


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
        self._overview.grid(row=2, column=1, columnspan=2)

        self.frame.grid_columnconfigure(2, weight=1)

        # read_data(kwargs.get(KEY_DATA_LOCATION), kwargs.get(KEY_DATA_TYPE))

        self.frame.pack(fill=BOTH, expand=True)

    @property
    def frame(self):
        return self._frame

    @property
    def overview(self):
        return self._overview
