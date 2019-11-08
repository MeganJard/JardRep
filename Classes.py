import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog

flag1 = True
flag2 = True
flag3 = True
flag4 = True
DataBaseList = []


class MainWindows(QMainWindow):  # Форма с главным окном

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

    # Открытие окон из главного
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


class BusCreate(QMainWindow):  # окно для создания дела
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.commandLinkButton.clicked.connect(self.dialog)

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
        font.setPointSize(12)
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
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(80, 250, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(80, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(80, 370, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(80, 430, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(80, 490, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(80, 550, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
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

    # Диалог для создания дела, создает новый класс
    def dialog(self):
        global DataBaseList
        DataBaseList = [self.textBrowser, self.textBrowser_2,
                        self.textBrowser_3,
                        self.textBrowser_4, self.textBrowser_5,
                        self.textBrowser_6, self.textBrowser_7,
                        self.textBrowser_8,
                        self.textBrowser_9]
        print(DataBaseList)
        print(DataBaseList[1])
        if not '' in DataBaseList:
            self.dial = BusCreateDialog([i.toPlainText() for i in DataBaseList])
            self.dial.show()
            for i in DataBaseList:
                i.clear()
            self.close()

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


class BusCreateDialog(QDialog):  # класс для диалога с сохранением в БД
    def __init__(self, li):
        super().__init__()
        self.li = li
        self.setupUi(self)

    def setupUi(self, Dialog):
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.textEdit.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 301, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.append)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def append(self):  # Сохранение в БД
        cn = sqlite3.connect("Database.db")
        cur = cn.cursor()

        self.li.append(self.textEdit.toPlainText())

        for i in range(len(self.li)):
            self.li[i] = "'" + str(self.li[i]) + "'"

        cur.execute(
            'INSERT INTO clients(fio, adess, place, inn, snils, telnumber, resogl, reorg, repkao, nameBus) VALUES(' + ', '.join(
                self.li) + ')')
        cn.commit()
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите удобное для Вас название дела"))


class Note(MainWindows, QMainWindow):  # Клаcс для заметок
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updatel()
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.updatel)
        self.pushButton.clicked.connect(self.newnote)
        self.listWidget.doubleClicked.connect(self.redact)

    def keyPressEvent(self, event):  # Обработка нажатия del для удаления
        if event.key() == Qt.Key_Delete:
            col = sqlite3.connect("Database.db")
            cur = col.cursor()
            ids = self.listWidget.currentItem().text().split()[-1]
            cur.execute(f'DELETE FROM notes WHERE id == "{ids}"')
            col.commit()
            self.updatel()

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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 360, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 591, 491))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFont(font)
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

    def updatel(self):  # Обновление виджета
        self.listWidget.clear()
        cn = sqlite3.connect("Database.db")
        cur = cn.cursor()
        li = []
        val = cur.execute(
            f"SELECT name FROM notes").fetchall()
        val1 = cur.execute(
            f"SELECT id FROM notes").fetchall()

        for i in range(len(val)):
            a1 = ''.join([str(j) for j in val1[i]])
            a2 = ''.join([str(j) for j in val[i]])
            a = '                                                                                                    ' \
                '  '.join(
                [a2, a1])
            li.append(a)
        self.listWidget.addItems(li)

    # Создание новой заметки через новое окно
    def newnote(self):
        self.newNOte = newNote()
        self.newNOte.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Заметки"))
        self.pushButton.setText(_translate("MainWindow", "Новая заметка"))
        self.pushButton_2.setText(_translate("MainWindow", "<<-- Назад"))
        self.pushButton_3.setText(_translate("MainWindow", "Обновить"))

    # снятие блока для редактирования полей
    def redact(self):
        self.noteLOok = noteLook(self.listWidget.currentItem().text().split()[-1])
        self.noteLOok.show()


# класс для просмотра заметки и ее редактирования
class noteLook(QMainWindow):
    def __init__(self, ids):
        super().__init__()
        self.id = ids
        self.setupUi(self)
        self.pushButton.clicked.connect(self.appends)
        self.pushButton_2.clicked.connect(self.close)
        li = sqlite3.connect("Database.db").cursor().execute(
            f'SELECT name, text FROM notes WHERE id == {self.id}').fetchall()[0]
        self.textEdit_2.setText(li[0])
        self.textEdit.setText(li[1])

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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 201, 33))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 70, 561, 131))
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
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

    def appends(self):  # запись в БД
        cn = sqlite3.connect("Database.db")
        cur = cn.cursor()
        name, text = self.textEdit_2.toPlainText(), self.textEdit.toPlainText()
        print(name, text)
        a = f'''UPDATE notes
    SET name = '{name}', text = '{text}'
    WHERE id= {self.id}
    '''
        print(a)
        cur.execute(a)
        cn.commit()
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Краткое имя заметки"))
        self.label.setText(_translate("MainWindow", "Редактирование заметки"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "<<-- Назад"))


# класс для создания новой заметки
class newNote(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.appends)
        self.pushButton_2.clicked.connect(self.close)

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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 201, 33))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 70, 561, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
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

    def appends(self):  # сохранение в БД
        cn = sqlite3.connect("Database.db")
        cur = cn.cursor()
        name, text = self.textEdit_2.toPlainText(), self.textEdit.toPlainText()
        a = f"INSERT INTO notes(name, text) VALUES('{name}', '{text}')"
        cur.execute(a)
        cn.commit()
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Краткое имя заметки"))
        self.label.setText(_translate("MainWindow", "Создание заметки"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "<<-- Назад"))


class Calend(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.new_sob)
        self.updateBar()
        self.calendarWidget.selectionChanged.connect(self.updateBar)
        self.listWidget.doubleClicked.connect(self.soblook)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.updateBar)

    # Нажатие del для удаления
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            col = sqlite3.connect("Database.db")
            cur = col.cursor()
            ids = self.listWidget.currentItem().text().split()[-1]
            print(f'DELETE FROM sobit WHERE id == "{ids}"')
            cur.execute(f'DELETE FROM sobit WHERE id == "{ids}"')
            col.commit()
            self.updateBar()

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
        self.calendarWidget.setGeometry(QtCore.QRect(470, 80, 311, 341))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 430, 311, 101))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 441, 451))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFont(font)
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
        self.pushButton_3.setText(_translate("Calender", "Обновить"))

    # обновление виджета QListWidget
    def updateBar(self):
        self.listWidget.clear()
        cn = sqlite3.connect("Database.db")
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
            a2 = ''.join([str(j) for j in val[i]])
            a = '                                                                                                    ' \
                '  '.join(
                [a2, a1])
            li.append(a)
        self.listWidget.addItems(li)

    # новое событие через класс newSob()
    def new_sob(self):
        a = self.calendarWidget.selectedDate()
        self.newsob = newSob(a)
        self.newsob.show()

    # просмотр события и редактирование
    def soblook(self):
        id = self.listWidget.currentItem().text().split()[-1]
        print(id)

        db = str(
            sqlite3.connect("Database.db").cursor().execute(f"SELECT text FROM sobit WHERE id = '{id}'").fetchall())

        self.sobLOok = SobLook(self.listWidget.currentItem().text().split()[-1],
                               ' '.join(self.listWidget.currentItem().text().split()[:-1]), db)
        self.sobLOok.show()


class SobLook(QMainWindow):
    def __init__(self, id, title, text):
        super().__init__()
        self.id = id
        self.text = text
        self.title = title
        self.setupUi(self)
        self.textEdit.setText(self.text.split("'")[1])
        self.textEdit_2.setText(''.join(self.title))
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.close)

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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 201, 33))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 70, 561, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
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

    def save(self):  # сохранение в БД
        a = sqlite3.connect("Database.db")
        a.cursor().execute(f'''UPDATE sobit
    SET text = '{self.textEdit.toPlainText()}', name = '{self.textEdit_2.toPlainText()}'
    WHERE id = {self.id}''')
        a.commit()
        self.close()


# класс для просмотра всех дел
class Busines(MainWindows, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget.doubleClicked.connect(self.redact)
        self.pushButton_2.clicked.connect(self.update_l)
        self.pushButton.clicked.connect(self.hide)
        self.update_l()

    # Нажатие на del для удаления записей
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            col = sqlite3.connect("Database.db")
            cur = col.cursor()
            ids = self.listWidget.currentItem().text().split()[-1]
            cur.execute(f'DELETE FROM clients WHERE id == "{ids}"')
            col.commit()
            self.update_l()

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
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 60, 731, 491))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 20, 101, 31))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Обновление виджета
    def update_l(self):
        self.listWidget.clear()
        comboList = []
        cn = sqlite3.connect("Database.db")
        cur = cn.cursor()
        val = len(list(cur.execute('SELECT fio FROM clients')))
        ids = list(cur.execute('SELECT id FROM clients'))
        li = list(cur.execute('SELECT nameBus FROM clients'))
        for i in range(val):
            a = str(li[i][
                        0]) + '                                                                   ' \
                              '                                                                      ' \
                              '                     ' + str(
                ids[i][0])
            comboList.append(a)

        self.listWidget.addItems(comboList)

    # редактирование дела через новый класс
    def redact(self):
        a = self.listWidget.currentItem().text().split()[-1]
        self.buslook = BusLook(a)
        self.buslook.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Мои дела"))
        self.pushButton.setText(_translate("MainWindow", "<-- Назад"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить"))


# Просмотр записей в деле
class BusLook(QMainWindow):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setupUi(self)
        self.pols = [self.textEdit_11, self.textEdit_12, self.textEdit_13, self.textEdit_14, self.textEdit_15,
                     self.textEdit_16,
                     self.textEdit_17,
                     self.textEdit_18, self.textEdit_19, self.textEdit_20]
        self.write()
        self.pushButton.clicked.connect(self.setreadFalse)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.close)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 130, 241, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 121, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 121, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 290, 121, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 330, 121, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 121, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 410, 121, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 450, 121, 31))
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 490, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 490, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.label_13.setObjectName("label_13")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(130, 90, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(130, 130, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_13.setGeometry(QtCore.QRect(130, 170, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_13.setFont(font)
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_14.setGeometry(QtCore.QRect(130, 210, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_14.setFont(font)
        self.textEdit_14.setObjectName("textEdit_14")
        self.textEdit_15 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_15.setGeometry(QtCore.QRect(130, 250, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_15.setFont(font)
        self.textEdit_15.setObjectName("textEdit_15")
        self.textEdit_16 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_16.setGeometry(QtCore.QRect(130, 290, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_16.setFont(font)
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_17.setGeometry(QtCore.QRect(130, 330, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_17.setFont(font)
        self.textEdit_17.setObjectName("textEdit_17")
        self.textEdit_18 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_18.setGeometry(QtCore.QRect(130, 370, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_18.setFont(font)
        self.textEdit_18.setObjectName("textEdit_18")
        self.textEdit_19 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_19.setGeometry(QtCore.QRect(130, 410, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_19.setFont(font)
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_20 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_20.setGeometry(QtCore.QRect(130, 450, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_20.setFont(font)
        self.textEdit_20.setObjectName("textEdit_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        db = sqlite3.connect("Database.db").cursor()
        self.var = db.execute(
            f'SELECT nameBus, fio, adess, place, inn, snils, telnumber, resogl, reorg, repkao FROM clients WHERE id = {self.id}').fetchall()[
            0]
        print(self.var[0])

    def setreadFalse(self):
        for i in self.pols:
            i.setReadOnly(False)

    # сохранение в БД
    def save(self):
        li = ['nameBus', 'fio', 'adess', 'place', 'inn', 'snils', 'telnumber', 'resogl', 'reorg', 'repkao']
        db = sqlite3.connect("Database.db")
        db1 = db.cursor()
        print()
        for i in range(len(self.pols)):
            db1.execute(f'''UPDATE clients
    SET {li[i]} = '{self.pols[i].toPlainText()}'
    WHERE id={self.id}
    ''')
        db.commit()
        for i in [self.textEdit_11, self.textEdit_12, self.textEdit_13, self.textEdit_14, self.textEdit_15,
                  self.textEdit_16, self.textEdit_17, self.textEdit_18, self.textEdit_19, self.textEdit_20]:
            i.clear()
        self.close()

    def write(self):
        print(len(self.pols))

        for i in range(len(self.pols)):
            self.pols[i].setText(str(self.var[i]))
            self.pols[i].setReadOnly(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Просмотр дела "))
        self.label_4.setText(_translate("MainWindow", "ФИО клиента"))
        self.label_5.setText(_translate("MainWindow", "Адрес"))
        self.label_6.setText(_translate("MainWindow", "Место рождения"))
        self.label_7.setText(_translate("MainWindow", "ИНН"))
        self.label_8.setText(_translate("MainWindow", "Снилс"))
        self.label_9.setText(_translate("MainWindow", "Номер телефона"))
        self.label_10.setText(_translate("MainWindow", "Реквизиты согл."))
        self.label_11.setText(_translate("MainWindow", "Рекв. орг. адвоката"))
        self.label_12.setText(_translate("MainWindow", "Рекв. квит. к ПКАО"))
        self.pushButton.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_3.setText(_translate("MainWindow", "<<--Назад"))
        self.label_13.setText(_translate("MainWindow", "Название"))


# Новое событие в календарь
class newSob(QMainWindow):
    def __init__(self, date):
        super().__init__()
        self.date = date
        self.setupUi(self)
        self.pushButton.clicked.connect(self.newsobit)
        self.pushButton_2.clicked.connect(self.close)

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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 70, 561, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 201, 33))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(font)
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

    # Новое событие в календарь
    def newsobit(self):
        cn = sqlite3.connect("Database.db")
        cur = cn.cursor()
        day = str(self.date.day())
        month = str(self.date.month())
        year = str(self.date.year())
        date = '-'.join([year, month, day])
        a = f"INSERT INTO sobit(date, text, name) VALUES('{date}', '{self.textEdit.toPlainText()}', '{self.textEdit_2.toPlainText()}')"
        cur.execute(a)
        cn.commit()
        self.close()
