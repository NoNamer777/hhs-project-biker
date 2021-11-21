"""
Project created by Oscar Wellner, 21144192

This application will setup a SQLite in memory database for Bicycles and Accessories.
It will get the data from the CSV files and pass that through to the database.
When the button is clicked on the main menu frame, the data is fetched
from the database and put into the Treeview widgets.
"""

from src.layout import BikerManagementApp


def main():
    biker_management_app = None

    try:
        biker_management_app = BikerManagementApp()

        biker_management_app.app.mainloop()

    except KeyboardInterrupt:
        # Intercept this exception that is introduced when
        # closing the `stop` button in Pycharm
        pass
    finally:
        biker_management_app.database_connection.close_connection()

        print('\nSuccessfully closed application')


if __name__ == '__main__':
    main()
