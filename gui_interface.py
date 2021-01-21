import os
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog

from src.code import concateneteLogs, mergeLogs, getHeaders, loadLogs, findExtension, resource_path
from gui_interface import *


class Ui(QtWidgets.QDialog):
    """
    Main gui-Window class
    """

    def __init__(self):
        """
        init function for the gui window
        """
        super(Ui, self).__init__()

        gui_full_path = resource_path('gui_design.ui')
        icon_full_path = resource_path('src\images\icon.png')

        # uic.loadUi(r'src\gui_design.ui', self)
        uic.loadUi(gui_full_path, self)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        # self.setWindowIcon(QtGui.QIcon(r"images\icon.png"))
        self.setWindowIcon(QtGui.QIcon(icon_full_path))
        self.output_path = ""
        self.listof_concatFiles = list()
        self.listof_mergeFiles = list()

        self.ConcatNow_button = self.findChild(QtWidgets.QPushButton, 'Concat_Now')
        self.ConcatNow_button.setToolTip('Execute concatenation on selected files')
        self.ConcatNow_button.clicked.connect(
            lambda: self.concatNow())

        self.Search_2_button = self.findChild(QtWidgets.QPushButton, 'Search_2')
        self.Search_2_button.setToolTip('Select input files names')
        self.Search_2_button.clicked.connect(
            lambda: self.fileDialog())
        self.merge_input_text = self.findChild(QtWidgets.QTextEdit, 'text_merge').setToolTip(
            'Selected input files path')
        self.Save_2_button = self.findChild(QtWidgets.QPushButton, 'Save_2')
        self.Save_2_button.setToolTip('Select output file name')
        self.Save_2_button.clicked.connect(
            lambda: self.fileDialogSave())
        self.merge_output_text = self.findChild(QtWidgets.QTextEdit, 'text_merge_2').setToolTip(
            'Selected output file path')
        self.MergeNow_button = self.findChild(QtWidgets.QPushButton, 'Merge_Now')
        self.MergeNow_button.setToolTip('Execute merge on selected files')
        self.MergeNow_button.clicked.connect(
            lambda: self.mergeNow())

        self.comboBox_leftKey.setToolTip('Key header from file 1')
        self.comboBox_rightKey.setToolTip('Key header from file 2')
        self.comboBox_mergeType.setToolTip('Select the type of merge to perform')

        self.design.setToolTip('https://github.com/Chrism1c/Logs-Manager')

        self.show()

    def fileDialog(self):
        """
        Procedure useful to select input files
        :return:  none
        """
        try:
            # Clear console labels
            self.Console.setText("")
            self.Console.setStyleSheet("background-color: none;")
            filenames, x = QFileDialog.getOpenFileNames(self, "Select input files (2+ Concat | Only 2 Merge)", "",
                                                        "CSV (Delimitato dal separatore di elenco) (*.csv);;"
                                                        "Cartella di lavoro Excel (*.xlsx);;"
                                                        "Cartella di lavoro Excel 97-2003 (*.xls)")

            self.listof_concatFiles = filenames
            self.listof_mergeFiles = filenames
            self.text_merge.setPlainText(" -- ".join(self.path_leaf(filenames)))
            ext_in = findExtension(x)
            frames = loadLogs(filenames, ext_in)
            leftColumns, rightColumns = getHeaders(frames)
            mergeTypes = ['left', 'right', 'outer', 'inner']
            for elem in leftColumns:
                self.comboBox_leftKey.addItem(elem)
            for elem in rightColumns:
                self.comboBox_rightKey.addItem(elem)
            for elem in mergeTypes:
                self.comboBox_mergeType.addItem(elem)
            print(filenames)
        except:
            print("***** exception in fileDialog")
            # Clear all data
            self.text_merge.setPlainText("")
            self.listof_concatFiles.clear
            self.listof_mergeFiles.clear

    def fileDialogSave(self):
        """
        Procedure useful to select name and directory of the output file
        :param value: boolean value to choose merge/concat operation
        :return: none
        """

        # Clear console labels
        self.Console.setText("")
        self.Console.setStyleSheet("background-color: none;")

        try:
            filename, x = QFileDialog.getSaveFileName(self, "Save file as:", "",
                                                      "CSV (Delimitato dal separatore di elenco) (*.csv);;"
                                                      "Cartella di lavoro Excel (*.xlsx);;"
                                                      "Cartella di lavoro Excel 97-2003 (*.xls)")

            self.text_merge_2.setPlainText(os.path.basename(filename))
            self.output_path = filename
            print(filename)
        except:
            print("***** exception in fileDialogSave")
            # Clear all data
            self.text_merge_2.setPlainText("")
            self.output_path = ""

    def concatNow(self):
        """
        Procedure useful to control inputs value before concat operation
        :return:
        """
        try:
            if len(self.listof_concatFiles) > 1 and len(self.output_path) > 1:
                ext_in = findExtension(self.listof_concatFiles[0])
                ext_out = findExtension(self.output_path)

                concateneteLogs(self.listof_concatFiles, self.output_path, ext_in, ext_out)

                print('Concat succesful !')
                self.Console.setText("Concat succesful !")
                self.Console.setStyleSheet("background-color: lightgreen;")
            else:
                print('Concat failed !\n NB:\n- Select two ore more input files [OPEN] \n- Define one output file ['
                      'SAVE]')
                self.Console.setText("Concat failed !")
                self.Console.setStyleSheet("background-color: red;")
        except:
            print("***** exception in concatNow")

        # Clear all data
        self.listof_concatFiles.clear()
        self.output_path = ""
        self.text_merge.setPlainText("")
        self.text_merge_2.setPlainText("")
        self.comboBox_leftKey.clear()
        self.comboBox_rightKey.clear()
        self.comboBox_mergeType.clear()

    def mergeNow(self):
        """
        Procedure useful to control inputs value before merge operation
        :return: none
        """
        try:
            # Keys control
            lkey = self.comboBox_leftKey.currentText()
            rkey = self.comboBox_rightKey.currentText()
            how_merge = self.comboBox_mergeType.currentText()

            if len(self.listof_mergeFiles) == 2 and len(self.output_path) > 0:

                ext_in = findExtension(self.listof_mergeFiles[0])
                ext_out = findExtension(self.output_path)

                mergeLogs(how_merge, lkey, rkey, self.listof_mergeFiles, self.output_path, ext_in, ext_out)

                print('Merge succesful !')
                self.Console.setText("Merge succesful !")
                self.Console.setStyleSheet("background-color: lightgreen;")
            else:
                print('Merge failed !\n NB:\n- Select only two input files [OPEN] \n- Define one output file [SAVE]')
                self.Console.setText("Merge failed !")
                self.Console.setStyleSheet("background-color: red;")
        except:
            print("***** exception in mergeNow")

        # Clear all data
        self.listof_mergeFiles.clear()
        self.output_path = ""
        self.text_merge.setPlainText("")
        self.text_merge_2.setPlainText("")
        self.comboBox_leftKey.clear()
        self.comboBox_rightKey.clear()
        self.comboBox_mergeType.clear()

    def path_leaf(self, listofpath):
        base = list()
        for path in listofpath:
            base.append(os.path.basename(path))
        return base

    # # Define function to import external files when using PyInstaller.
    # def resource_path(relative_path):
    #     """ Get absolute path to resource, works for dev and for PyInstaller """
    #     try:
    #     # PyInstaller creates a temp folder and stores path in _MEIPASS
    #         base_path = sys._MEIPASS
    #     except Exception:
    #         base_path = os.path.abspath(".")
    #     return os.path.join(base_path, relative_path)
