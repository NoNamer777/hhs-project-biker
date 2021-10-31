from isid.src.layout.bikerManagementApp import BikerManagementApp


def main():
    try:
        biker_management_app = BikerManagementApp()

        biker_management_app.app.mainloop()

    except KeyboardInterrupt:
        print('Successfully closed application')


if __name__ == '__main__':
    main()
