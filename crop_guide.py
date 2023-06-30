# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crop_guide.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 30, 441, 81))
        self.frame.setStyleSheet("background-color: rgb(255, 227, 65);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_heading = QtWidgets.QLabel(self.frame)
        self.label_heading.setGeometry(QtCore.QRect(90, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_heading.setFont(font)
        self.label_heading.setObjectName("label_heading")
        self.line_acres = QtWidgets.QLineEdit(self.centralwidget)
        self.line_acres.setGeometry(QtCore.QRect(250, 330, 113, 31))
        self.line_acres.setObjectName("line_acres")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_season = QtWidgets.QLabel(self.centralwidget)
        self.label_season.setGeometry(QtCore.QRect(60, 266, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_season.setFont(font)
        self.label_season.setObjectName("label_season")
        self.label_state = QtWidgets.QLabel(self.centralwidget)
        self.label_state.setGeometry(QtCore.QRect(60, 205, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.label_budget = QtWidgets.QLabel(self.centralwidget)
        self.label_budget.setGeometry(QtCore.QRect(60, 400, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_budget.setFont(font)
        self.label_budget.setObjectName("label_budget")
        self.line_budget = QtWidgets.QLineEdit(self.centralwidget)
        self.line_budget.setGeometry(QtCore.QRect(250, 400, 113, 31))
        self.line_budget.setObjectName("line_budget")
        self.label_acres = QtWidgets.QLabel(self.centralwidget)
        self.label_acres.setGeometry(QtCore.QRect(60, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_acres.setFont(font)
        self.label_acres.setObjectName("label_acres")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(160, 470, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_submit.setFont(font)
        self.button_submit.setObjectName("button_submit")
        self.button_submit.clicked.connect(self.submit)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 180, 20, 281))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(450, 210, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_image.setFont(font)
        self.label_image.setObjectName("label_image")
        self.text_info = QtWidgets.QTextEdit(self.centralwidget)
        self.text_info.setGeometry(QtCore.QRect(460, 420, 211, 91))
        self.text_info.setObjectName("text_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submit(self):
        print('clicked')
        state = self.comboBox.currentText()
        season = self.comboBox_2.currentText()
        acres = int(self.line_acres.text())
        budget = int(self.line_budget.text())
        print(state, season, acres, budget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "CROP GUIDE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Chandigarh"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Delhi"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Haryana"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Himachal Pradesh"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Jammu Kashmir"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Ladakh"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Punjab"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Rajasthan"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Uttarakhand"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Uttar Pradesh"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Madhya Pradesh"))
        self.comboBox.setItemText(11, _translate("MainWindow", "West Bengal"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Bihar"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Gujarat"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Andhra Pradesh"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Karnataka"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Kerala"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Lakshadweep"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Puducherry"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Tamil Nadu"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Telangana"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Chennai"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Bengaluru"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Hyderabad"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Kochi"))
        self.comboBox.setItemText(25, _translate("MainWindow", "Warangal"))
        self.comboBox.setItemText(26, _translate("MainWindow", "Thiruvananthapuram"))
        self.comboBox.setItemText(27, _translate("MainWindow", "Coimbatore"))
        self.comboBox.setItemText(28, _translate("MainWindow", "Visakhapatanam"))
        self.comboBox.setItemText(29, _translate("MainWindow", "Mysuru"))
        self.comboBox.setItemText(30, _translate("MainWindow", "Madurai"))
        self.comboBox.setItemText(31, _translate("MainWindow", "Vijayawada"))
        self.comboBox.setItemText(32, _translate("MainWindow", "Kozhikode"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kharif"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Rabi"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Zaid"))
        self.label_season.setText(_translate("MainWindow", "Season"))
        self.label_state.setText(_translate("MainWindow", "State"))
        self.label_budget.setText(_translate("MainWindow", "Budget"))
        self.label_acres.setText(_translate("MainWindow", "Acres"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.label_image.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
