from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow) -> None:
        """
        This is the function that builds the GUI for the vote menu.
        :param MainWindow:
        :return: None
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.john_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.john_label.setGeometry(QtCore.QRect(0, -20, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.john_label.setFont(font)
        self.john_label.setObjectName("john_label")
        self.jane_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.jane_label.setGeometry(QtCore.QRect(0, 30, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.jane_label.setFont(font)
        self.jane_label.setObjectName("jane_label")
        self.total_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(0, 70, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.total_label.setFont(font)
        self.total_label.setObjectName("total_label")
        self.button_john = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.button_john.setGeometry(QtCore.QRect(0, 140, 101, 31))
        self.button_john.setObjectName("button_john")
        self.button_jane = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.button_jane.setGeometry(QtCore.QRect(0, 170, 82, 17))
        self.button_jane.setObjectName("button_jane")
        self.id_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(10, 190, 381, 41))
        self.id_input.setObjectName("id_input")
        self.vote_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vote_button.setGeometry(QtCore.QRect(150, 10, 91, 81))
        self.vote_button.setObjectName("vote_button")
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(270, 10, 91, 81))
        self.exit_button.setObjectName("exit_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        """
        This function helps set the text for some of the attributes within the gui
        :param MainWindow:
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vote Menu"))
        self.john_label.setText(_translate("MainWindow", "John - 0"))
        self.jane_label.setText(_translate("MainWindow", "Jane - 0"))
        self.total_label.setText(_translate("MainWindow", "Total - 0"))
        self.button_john.setText(_translate("MainWindow", "Vote for John"))
        self.button_jane.setText(_translate("MainWindow", "Vote for Jane"))
        self.id_input.setPlaceholderText(_translate("MainWindow", "Enter 4 digit ID"))
        self.vote_button.setText(_translate("MainWindow", "Vote"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())