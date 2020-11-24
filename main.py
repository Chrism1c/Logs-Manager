from src.gui_interface import *
import sys

if __name__ == "__main__":
    """
    main function to execute the app
    """
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
