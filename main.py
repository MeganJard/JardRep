import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFormLayout, QGroupBox, QDialog, QPushButton

flag1 = True
flag2 = True
flag3 = True
flag4 = True
DataBaseList = []


class MainWindows(QMainWindow):

    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(966, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 431, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 190, 431, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 370, 431, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 370, 431, 131))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindows.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindows)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 21))
        self.menubar.setObjectName("menubar")
        MainWindows.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindows)
        self.statusbar.setObjectName("statusbar")
        MainWindows.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

        self.pushButton.clicked.connect(self.new_bus_show)
        self.pushButton_2.clicked.connect(self.calend_show)
        self.pushButton_3.clicked.connect(self.my_bus_show)
        self.pushButton_4.clicked.connect(self.my_notes_show)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindows", "MainWindows"))
        self.pushButton.setText(_translate("MainWindows", "Новое дело"))
        self.pushButton_2.setText(_translate("MainWindows", "Календарь"))
        self.pushButton_3.setText(_translate("MainWindows", "Мои дела"))
        self.pushButton_4.setText(_translate("MainWindows", "Мои заметки"))
        self.label.setText(_translate("MainWindows", "JardLawyer"))

    def new_bus_show(self):
        global flag1
        if flag1:
            self.new_bus_show = BusCreate()
            flag1 = False

        self.new_bus_show.show()

    def calend_show(self):

        global flag2
        if flag2:
            self.calend_show = Calend()
            flag2 = False

        self.calend_show.show()

    def my_bus_show(self):
        global flag3
        if flag3:
            self.my_bus_show = Busines()
            flag3 = False

        self.my_bus_show.show()

    def my_notes_show(self):
        global flag4
        if flag4:
            self.my_notes_show = Note()
            flag4 = False
        # self.hide()
        self.my_notes_show.show()

    def ret(self):
        self.show()


class BusCreate(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 645)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 70, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 130, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(80, 250, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(80, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(80, 370, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(80, 430, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(80, 490, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(80, 550, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 130, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 190, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 250, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 310, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 370, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 430, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 490, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 550, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(540, 520, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.pushButton.setObjectName("pushButton")
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
        self.pushButton.clicked.connect(self.hide)
        self.commandLinkButton.clicked.connect(self.dialog)

    def dialog(self):
        global DataBaseList
        DataBaseList = [self.textBrowser.toPlainText(), self.textBrowser_2.toPlainText(),
                        self.textBrowser_3.toPlainText(),
                        self.textBrowser_4.toPlainText(), self.textBrowser_5.toPlainText(),
                        self.textBrowser_6.toPlainText(), self.textBrowser_7.toPlainText(),
                        self.textBrowser_8.toPlainText(),
                        self.textBrowser_9.toPlainText()]
        print(DataBaseList[1])
        if "" not in DataBaseList:
            self.dial = BusCreateDialog()

            self.dial.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Новое дело"))
        self.label_2.setText(_translate("MainWindow", "Фамилия, Имя, Отчество"))
        self.label_3.setText(_translate("MainWindow", "Адрес"))
        self.label_4.setText(_translate("MainWindow", "Место рождения"))
        self.label_5.setText(_translate("MainWindow", "ИНН"))
        self.label_6.setText(_translate("MainWindow", "СНИЛС"))
        self.label_7.setText(_translate("MainWindow", "Номер телефона"))
        self.label_8.setText(_translate("MainWindow", "Реквезиты соглашения"))
        self.label_9.setText(_translate("MainWindow", "Реквезиты органа адвоката"))
        self.label_10.setText(_translate("MainWindow", "Реквизиты квитанции к ПКАО"))
        self.commandLinkButton.setText(_translate("MainWindow", "Создать дело"))
        self.pushButton.setText(_translate("MainWindow", "<<-- Назад"))


class BusCreateDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 158)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 381, 41))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.append)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def append(self):
        cn = sqlite3.connect('Database.db')
        cur = cn.cursor()
        a = list(DataBaseList)
        print(self.textEdit.toPlainText())
        a.append(self.textEdit.toPlainText())
        a.append(len(list(cur.execute('SELECT fio FROM clients').fetchall())))
        print(a)
        for i in range(len(a)):
            a[i] = "'" + str(a[i]) + "'"

        print(', '.join(a))

        cur.execute('INSERT INTO clients VALUES(' + ', '.join(a) + ')')
        cn.commit()
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите удобное для Вас название дела"))


class Note(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 601, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 460, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.pushButton_2.clicked.connect(self.hide)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Заметки"))
        self.pushButton.setText(_translate("MainWindow", "Новая заметка"))
        self.pushButton_2.setText(_translate("MainWindow", "<<-- Назад"))


class Calend(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.new_sob)
        self.updateBar()
        self.calendarWidget.selectionChanged.connect(self.updateBar)
        self.listView.doubleClicked.connect(self.soblook)

    def setupUi(self, Calender):
        Calender.setObjectName("Calender")
        Calender.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Calender)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(480, 70, 311, 341))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 440, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 70, 431, 461))
        self.listView.setObjectName("listView")
        Calender.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calender)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Calender.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calender)
        self.statusbar.setObjectName("statusbar")
        Calender.setStatusBar(self.statusbar)

        self.retranslateUi(Calender)
        QtCore.QMetaObject.connectSlotsByName(Calender)

    def retranslateUi(self, Calender):
        _translate = QtCore.QCoreApplication.translate
        Calender.setWindowTitle(_translate("Calender", "MainWindow"))
        self.label.setText(_translate("Calender", "Календарь"))
        self.pushButton.setText(_translate("Calender", "Новое событие "))
        self.pushButton_2.setText(_translate("Calender", "<<-- Назад"))

    def updateBar(self):
        self.listView.clear()
        cn = sqlite3.connect('Database.db')
        cur = cn.cursor()
        date = self.calendarWidget.selectedDate()
        dat = '-'.join([str(date.year()), str(date.month()), str(date.day())])

        li = []
        val = cur.execute(
            f"SELECT name FROM sobit WHERE date = '{dat}'").fetchall()
        val1 = cur.execute(
            f"SELECT id FROM sobit WHERE date = '{dat}'").fetchall()

        for i in range(len(val)):
            a1 = ''.join([str(j) for j in val1[i]])
            a2 = ''.join(val[i])
            a = '                                '.join(
                [a2, a1])
            li.append(a)
        self.listView.addItems(li)

    def new_sob(self):
        a = self.calendarWidget.selectedDate()
        self.newsob = newSob(a)
        self.newsob.show()

    def soblook(self):
        id = self.listView.currentItem().text().split()[-1]
        print(id)

        db = str(sqlite3.connect('Database.db').cursor().execute(f"SELECT text FROM sobit WHERE id = '{id}'").fetchall())
        print(self.listView.currentItem().text().split()[-1], ' '.join(self.listView.currentItem().text().split()[:-1]), db, self)
        self.sobLOok = SobLook(self.listView.currentItem().text().split()[-1], ' '.join(self.listView.currentItem().text().split()[:-1]), db, self)
        self.sobLOok.show()


class SobLook(Calend, QMainWindow):
    def __init__(self, id, title, text, rodit):
        super(QMainWindow).__init__()
        self.id = id
        self.text = text
        self.title = title
        self.rodit = rodit
        self.setupUi(self)
        print(self.text)
        self.textEdit.setText(self.text.split("'")[1])
        self.textEdit_2.setText(''.join(self.title))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 248)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 201, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 70, 561, 131))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Краткое имя заметки"))
        self.label.setText(_translate("MainWindow", "Редактирование события"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "<<-- Назад"))


class Busines(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 781, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
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
        self.pushButton.clicked.connect(self.hide)
        formLayout = QFormLayout()
        groupBox = QGroupBox()
        comboList = []

        cn = sqlite3.connect('Database.db')
        cur = cn.cursor()

        val = len(list(cur.execute('SELECT fio FROM clients')))
        print(val)

        li = list(cur.execute('SELECT nameBus FROM clients'))
        print(li)
        for i in range(val):
            a = QPushButton(str(li[i][0]))
            a.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
            comboList.append(a)
            formLayout.addRow(comboList[i])
        groupBox.setLayout(formLayout)
        self.scrollArea.setWidget(groupBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Мои дела"))
        self.pushButton.setText(_translate("MainWindow", "<<-- Назад"))


class newSob(QMainWindow):
    def __init__(self, date):
        super().__init__()
        self.date = date
        self.setupUi(self)
        self.pushButton.clicked.connect(self.newsobit)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 256)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 70, 561, 131))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 201, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Новое событие"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "<<-- Назад"))
        self.label_2.setText(_translate("MainWindow", "Краткое имя заметки"))

    def newsobit(self):
        cn = sqlite3.connect('Database.db')
        cur = cn.cursor()
        day = str(self.date.day())
        month = str(self.date.month())
        year = str(self.date.year())
        date = '-'.join([year, month, day])
        a = f"INSERT INTO sobit(date, text, name) VALUES('{date}', '{self.textEdit.toPlainText()}', '{self.textEdit_2.toPlainText()}')"
        cur.execute(a)
        cn.commit()
        self.close()


class Main(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())

#коммит, если что