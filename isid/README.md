# HHS Project Biker

This Python project is created by Oscar Wellner, 21144192, and is structured as follows:

```
Project (isid)
|    README.md
|    main.py
└─── assets
|    └─── data
|    |        accessories.csv
|    |        bicycles.csv
|    |        (biker.db)
|    |        customers.csv
|    |        employees.csv
|    |
|    └─── images
|             biker-banner.png
|
└─── src
|    └─── layout
|    |        bikerManagementApp.py
|    |        overviewFrame.py
|    |
|    └─── models
|    |        accessory.py
|    |        bicycle.py
|    |        customer.py
|    |        employee.py
|    |        item.py
|    |        person.py
|    |
|    └─── utils
|             dataReader.py
└────────────────────────────
```

## Main app structure

---
The `data` folder holds all the raw data and acts as the database location for the application. The `layout` folder
holds all the logic that is necessary to produce the GUI of the application. The `models` folders holds all the
information about the class models that are used in this application. The `utils` folder holds all the logic to
transform the raw data located in the `data` folder, into Python class objects.

This structure was chosen based on the MVC ideology that helps with separating logic used for setting up the Views (GUI),
from the logic used for declaring the domain (Models).

I've created two extra models (`Person` and `Item`) which act as the Parent classes for the other classes. This helps
with reducing repeated code and thus tries to keep the codebase DRY (Don't Repeat Yourself).

The `__init__.py` files are necessary for declaring packages and could be left empty if desired. I however specifically
specified what is imported into those files, to limit what is exposed from those packages. This helps with keeping code
private, which should not be used in other locations of the application.

## Application flow

---
The application will be started by calling the constructor of the `BikerManagementApp` in the `main.py` module.

Before the GUI is constructed the database is prepared in the background. The database is located at `<root>/assets/data/biker.db`
or is created there if it is not found. When the database does not exist, the necessary tables are generated. To
populate the database, the data is read from the CSV-files and inserted into the relevant database tables. Should the
database file already exist, the table generation and data insertion steps are skipped.

In the application constructor the application window will be constructed (title, default height and width), and the
notebook widget is added for navigation purposes. A main menu frame is added with a logo (also known as a banner) and
from there various overview frames are added for the different types of data that are present.  
An OverviewFrame has a smaller logo in the top left corner and a Treeview widget (Table) to show of the data. By default,
the Treeview widget does not show any data entries.

When an OverviewFrame is added to the application a button is added to the main menu frame to get the data from database
and forward that data to the Treeview of the OverviewFrame. After the data is inserted into the Treeview the User is
navigated to that OverviewFrame/ tab, and the button is disabled to prevent data being inserted multiple times into
the Treeview. The user can navigate back and forth to different overview using the notebook tabs, at the top of the window.

After the User closes the application the database connection is closed.

### To improve

---
To further improve this I would have liked to make more in depth checks on the database upon creation of the application.
Currently, it only checks how many tables are present, but it doesn't check which tables are present and what their
format is (the columns that are used in those tables). If those tables and their columns would match with the required
data structure for this application, then it would be a much more safe check. Now, the application still fails when there
are multiple tables in the database file, but not the tables that the application needs, or if the tables do exist, but
they use other columns then expected.

---
