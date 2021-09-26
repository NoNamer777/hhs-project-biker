# HHS Project Biker

On this moment we use the `tabulate` module to help us with the printing of the data in good looking tables to the console.
To use this project, Clone it to your desired folder, open the folder with your IDE, open a console/terminal with the project folder as working directory and run:

```shell
pip install tabulate
```

After that you can run the `main.py` file in the terminal and the sript will run and provide the output in the console.

The data sources/destinations in the `/data/*` folder are currently cleaned after every run of the script. This is done to keep the data files small in size and prevent previous writes to interver with future runs. Of course, nothing bad would happen, provided that data that exists in those files follow the data format layed out at the top of each file, but that's a minor detail.

If you'd like to keep the data that is written to the files find the `CLEAN_DATA_FILES` variable at the top of the `main.py` file and set it to `False`.
