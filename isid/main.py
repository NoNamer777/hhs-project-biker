"""
Project created by Oscar Wellner, 21144192

This application will read the CSV-files when the button on the main tab is pressed and insert the
found data into the Text widgets of the overview tabs of the corresponding entities.
"""

from src.layout import BikerManagementApp


def main():
    try:
        biker_management_app = BikerManagementApp()

        biker_management_app.app.mainloop()

    except KeyboardInterrupt:
        print('Successfully closed application')


if __name__ == '__main__':
    main()
