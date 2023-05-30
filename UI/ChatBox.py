# Form implementation generated from reading ui file 'ChatBox.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 478)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(57, 65, 81);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 221, 451))
        self.frame.setStyleSheet("background-color: rgb(114, 129, 161);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(219, -1, 421, 451))
        self.frame_2.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 161, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(114, 129, 161);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 40, 211, 411))
        self.textBrowser.setStyleSheet("background-color: rgb(114, 129, 161);")
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 221, 411))
        self.textEdit.setStyleSheet("background-color: rgb(114, 129, 161);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(533, 400, 86, 34))
        self.pushButton_2.setStyleSheet("background-color: rgba(78, 88, 110, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 401, 287, 32))
        self.lineEdit_3.setStyleSheet("background-color: rgba(78, 88, 110, 255);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 0, 421, 401))
        self.textEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 0); color: black")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(57, 65, 81);")
        self.menubar.setObjectName("menubar")
        self.menuChatBox = QtWidgets.QMenu(parent=self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menuChatBox.setFont(font)
        self.menuChatBox.setStyleSheet("background-color: rgb(57, 65, 81);")
        self.menuChatBox.setObjectName("menuChatBox")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.menuChatBox.addAction(self.action_2)
        self.menuChatBox.addAction(self.action_3)
        self.menubar.addAction(self.menuChatBox.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatBox"))
        self.label.setText(_translate("MainWindow", "Участники: 0 в сети"))
        self.pushButton_2.setText(_translate("MainWindow", "Отправить"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Напишите сообщение..."))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuChatBox.setTitle(_translate("MainWindow", "ChatBox"))
        self.action.setText(_translate("MainWindow", "Изменить тему"))
        self.action_2.setText(_translate("MainWindow", "Выйти из аккаунта"))
        self.action_3.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())