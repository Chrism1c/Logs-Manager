from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from src.code import concateneteLogs, mergeLogs, getHeaders, loadLogs, findExtension
import xlrd


class Ui(QtWidgets.QDialog):
    """
    Main gui-Window class
    """

    def __init__(self):
        """
        init function for the gui window
        """
        super(Ui, self).__init__()
        uic.loadUi('src/gui_design.ui', self)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))
        self.output_path = ""
        self.listof_concatFiles = list()
        self.listof_mergeFiles = list()

        self.Search_1_button = self.findChild(QtWidgets.QPushButton, 'Search_1')
        self.Search_1_button.setToolTip('Select input files names')
        self.Search_1_button.clicked.connect(
            lambda: self.fileDialog(True))
        self.concat_input_text = self.findChild(QtWidgets.QTextEdit, 'text_concat').setToolTip(
            'Selected input files path')
        self.Save_1_button = self.findChild(QtWidgets.QPushButton, 'Save_1')
        self.Save_1_button.setToolTip('Select output file name')
        self.Save_1_button.clicked.connect(
            lambda: self.fileDialogSave(True))
        self.concat_output_text = self.findChild(QtWidgets.QTextEdit, 'text_concat_2').setToolTip(
            'Selected output file path')
        self.ConcatNow_button = self.findChild(QtWidgets.QPushButton, 'Concat_Now')
        self.ConcatNow_button.setToolTip('Execute concatenation on selected files')
        self.ConcatNow_button.clicked.connect(
            lambda: self.concatNow())

        self.Search_2_button = self.findChild(QtWidgets.QPushButton, 'Search_2')
        self.Search_2_button.setToolTip('Select input files names')
        self.Search_2_button.clicked.connect(
            lambda: self.fileDialog(False))
        self.merge_input_text = self.findChild(QtWidgets.QTextEdit, 'text_merge').setToolTip(
            'Selected input files path')
        self.Save_2_button = self.findChild(QtWidgets.QPushButton, 'Save_2')
        self.Save_2_button.setToolTip('Select output file name')
        self.Save_2_button.clicked.connect(
            lambda: self.fileDialogSave(False))
        self.merge_output_text = self.findChild(QtWidgets.QTextEdit, 'text_merge_2').setToolTip(
            'Selected output file path')
        self.MergeNow_button = self.findChild(QtWidgets.QPushButton, 'Merge_Now')
        self.MergeNow_button.setToolTip('Execute merge on selected files')
        self.MergeNow_button.clicked.connect(
            lambda: self.mergeNow())

        self.comboBox_leftKey.setToolTip('Key header from file 1')
        self.comboBox_rightKey.setToolTip('Key header from file 2')
        self.show()

    def fileDialog(self, value):
        """
        Procedure useful to select input files
        :param value: boolean value to choose merge/concat operation
        :return:  none
        """
        try:
            # Clear console labels
            self.Console_merge.setText("")
            self.Console_merge.setStyleSheet("background-color: none;")
            self.Console_concat.setText("")
            self.Console_concat.setStyleSheet("background-color: none;")
            filenames, x = QFileDialog.getOpenFileNames(self, "Select input files (2+ Concat | Only 2 Merge)", "",
                                                        "Cartella di lavoro Excel (*.xlsx);;Cartella di lavoro Excel "
                                                        "97-2003 (*.xls);;CSV (Delimitato dal separatore di elenco) ("
                                                        "*.csv)")
            if value:
                self.text_concat.setPlainText("\n".join(filenames))
                self.listof_concatFiles = filenames
            else:
                self.text_merge.setPlainText("\n".join(filenames))
                self.listof_mergeFiles = filenames
                ext_in = findExtension(x)
                frames = loadLogs(filenames, ext_in)
                leftColumns, rightColumns = getHeaders(frames)
                for elem in leftColumns:
                    self.comboBox_leftKey.addItem(elem)
                for elem in rightColumns:
                    self.comboBox_rightKey.addItem(elem)
            print(filenames)
        except:
            print("***** Error in fileDialog")
            # Clear all data
            self.text_merge.setPlainText("")
            self.text_concat.setPlainText("")
            self.listof_concatFiles.clear
            self.listof_mergeFiles.clear

    def fileDialogSave(self, value):
        """
        Procedure useful to select name and directory of the output file
        :param value: boolean value to choose merge/concat operation
        :return: none
        """

        # Clear console labels
        self.Console_merge.setText("")
        self.Console_merge.setStyleSheet("background-color: none;")
        self.Console_concat.setText("")
        self.Console_concat.setStyleSheet("background-color: none;")

        try:
            filename, x = QFileDialog.getSaveFileName(self, "Save file as:", "",
                                                      "Cartella di lavoro Excel (*.xlsx);;Cartella di lavoro Excel "
                                                      "97-2003 (*.xls);;CSV (Delimitato dal separatore di elenco) ("
                                                      "*.csv)")
            if value:
                self.text_concat_2.setPlainText(filename)
            else:
                self.text_merge_2.setPlainText(filename)

            self.output_path = filename
            print(filename)
        except:
            print("***** Error in fileDialogSave")
            # Clear all data
            self.text_merge_2.setPlainText("")
            self.text_concat_2.setPlainText("")
            self.output_path = ""

    def concatNow(self):
        """
        Procedure useful to control inputs value before concat operation
        :return:
        """
        # try:
        if len(self.listof_concatFiles) > 1 and len(self.output_path) > 1:

            ext_in = findExtension(self.listof_concatFiles[0])
            ext_out = findExtension(self.output_path)

            concateneteLogs(self.listof_concatFiles, self.output_path, ext_in, ext_out)

            print('Concat succesful !')
            self.Console_concat.setText("Concat succesful !")
            self.Console_concat.setStyleSheet("background-color: lightgreen;")
        else:
            print('Concat failed !\n NB:\n- Select two ore more input files [OPEN] \n- Define one output file ['
                  'SAVE]')
            self.Console_concat.setText("Concat failed !")
            self.Console_concat.setStyleSheet("background-color: red;")
        # except:
        #     print("***** Error in concatNow")

        # Clear all data
        self.listof_concatFiles.clear()
        self.output_path = ""
        self.text_concat.setPlainText("")
        self.text_concat_2.setPlainText("")

    def mergeNow(self):
        """
        Procedure useful to control inputs value before merge operation
        :return: none
        """
        try:
            # Keys control
            lkey = self.comboBox_leftKey.currentText()
            rkey = self.comboBox_rightKey.currentText()
            # print("Chiave left corrente = ", self.comboBox_leftKey.currentText())
            # print("Chiave right corrente = ", self.comboBox_rightKey.currentText())

            if len(self.listof_mergeFiles) == 2 and len(self.output_path) > 0:

                ext_in = findExtension(self.listof_mergeFiles[0])
                ext_out = findExtension(self.output_path)

                mergeLogs(lkey, rkey, self.listof_mergeFiles, self.output_path, ext_in, ext_out)

                print('Merge succesful !')
                self.Console_merge.setText("Merge succesful !")
                self.Console_merge.setStyleSheet("background-color: lightgreen;")
            else:
                print('Merge failed !\n NB:\n- Select only two input files [OPEN] \n- Define one output file [SAVE]')
                self.Console_merge.setText("Merge failed !")
                self.Console_merge.setStyleSheet("background-color: red;")
        except:
            print("***** Error in mergeNow")

        # Clear all data
        self.listof_mergeFiles.clear()
        self.output_path = ""
        self.text_merge.setPlainText("")
        self.text_merge_2.setPlainText("")
        self.comboBox_leftKey.clear()
        self.comboBox_rightKey.clear()
