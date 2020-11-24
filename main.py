from src.gui_interface import *
import sys
import ctypes

myappid = 'Uniba.Logs-Manager'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    """
    main function to execute the app
    """
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
