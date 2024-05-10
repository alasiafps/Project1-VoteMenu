from logic import *

def main() -> None:
    """
    This is the main function that runs to load up the GUI
    :return: None
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()