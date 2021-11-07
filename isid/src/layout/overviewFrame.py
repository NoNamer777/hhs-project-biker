from os import getcwd
from os.path import join
from tkinter import Text, PhotoImage
from tkinter.constants import BOTH, SOLID, END, DISABLED, NORMAL
from tkinter.font import BOLD, Font
from tkinter.ttk import Frame, Label, Notebook

KEY_HEADER_TEXT = 'header_text'
WIDTH_OVERVIEW = 136


class OverviewFrame:
    def __init__(self, notebook: Notebook, **kwargs):
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
        self._overview = Text(self.frame, borderwidth=1, relief=SOLID)
        self.overview.config(width=WIDTH_OVERVIEW)
        self._overview.grid(row=2, column=1, columnspan=2)

        self.frame.grid_columnconfigure(2, weight=1)
        self.overview.config(state=DISABLED)

        self.frame.pack(fill=BOTH, expand=True)

    def insert_data(self, objects):
        """
        Inserts data into the Text Widget in a table like style
        :param objects: The data to insert
        """
        self.overview.config(state=NORMAL)
        headers = objects[0].attributes()

        # Insert the entity attributes as headers.
        formatted_headers = self._format_line(headers)
        self.overview.insert(END, formatted_headers)

        # Insert a line between the headers and the actual data
        line = '-' * WIDTH_OVERVIEW + '\n'
        self.overview.insert(END, line)

        # Insert every entity in Text widget
        for entry in objects:
            formatted_entry = self._format_line(entry.values())
            self.overview.insert(END, formatted_entry)

        self.overview.config(state=DISABLED)

    def _format_line(self, data) -> str:
        """
        Takes the data a creates a formatted String representation of it.
        :param data: Data that needs to be formatted into a single line
        :return: A single line ready to be inserted into the Text widget
        """
        # Determine how many items there needs to be on one line
        number_of_items = len(data)

        # Determine how many space a single item takes
        space_per_item = (WIDTH_OVERVIEW // number_of_items) - 2
        formatted_line = ''

        # Add all values onto the formatted line separating them with a pipe `|`
        for idx in range(0, len(data)):
            entry = data[idx]

            formatted_line += f'{str(entry).center(space_per_item)}'

            # Don't add a pipe after the last value
            if idx is not len(data) - 1:
                formatted_line += ' |'

        return formatted_line + '\n'

    @property
    def frame(self):
        return self._frame

    @property
    def overview(self):
        return self._overview
