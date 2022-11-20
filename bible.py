import sys
import webbrowser
import sqlite3
import os

from PyQt5.QtWidgets import QApplication, QMessageBox, QComboBox, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QListWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


class PopUp(QMainWindow):  # класс всплывающего окна, которое высвечивает информацию о книге
    def __init__(self, ID, title, author, year, link):
        super().__init__()
        self.ID = ID
        self.title = title
        self.author = author
        self.year = year
        self.link = link
        self.setupUi(self)

    def setupUi(self, MainWindow):  # метод который устанавливает графический интерфейс
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setScaledContents(True)
        self.label.setMinimumSize(250, 400)
        self.label.setMaximumSize(250, 400)
        if os.path.exists(f"{self.title}.jpg"):
            self.label.setPixmap(QPixmap(f"{self.title}.jpg"))
        else:
            self.label.setPixmap(QPixmap(f"no_name.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft |
                                  QtCore.Qt.AlignVCenter)
        self.label_3.setText("id")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QLabel(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.setFont(font)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):    # метод который задает текст виджетам в окне
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", f"ID: {self.ID}"))
        self.label_2.setText(_translate("MainWindow", f"Название: {self.title}"))
        self.label_4.setText(_translate("MainWindow", f"Автор: {self.author}"))
        self.label_5.setText(_translate("MainWindow", f"Жанр: {self.year}"))
        self.pushButton.setText(_translate("MainWindow", f"Год издания: {self.link}"))


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(700, 700)
        self.setMaximumSize(700, 700)
        self.setMinimumSize(700, 700)
        self.setWindowTitle('Каталог библиотеки')
        self.qbox = QComboBox(self)
        self.qbox.move(50, 50)
        self.qbox.resize(200, 50)
        self.qbox.addItems(['Автор', 'Название'])
        self.pushbutton = QPushButton(self)
        self.pushbutton.setText('Искать')
        self.pushbutton.move(450, 50)
        self.pushbutton.resize(200, 50)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(50, 150)
        self.lineEdit.resize(200, 50)
        self.listWidget = QListWidget(self)
        self.listWidget.move(50, 250)
        self.listWidget.resize(600, 500)
        con = sqlite3.connect('books_db.db')
        cur = con.cursor()
        self.elements = cur.execute("""SELECT title FROM books ORDER BY id""").fetchall()
        for i in self.elements:
            newButton = QtWidgets.QPushButton(f'{i[0]}')
            newButton.clicked.connect(lambda btn, text=i[0]: self.open_book(text))

            listWidgetItem = QtWidgets.QListWidgetItem()
            listWidgetItem.setSizeHint(newButton.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, newButton)
            self.listWidget.scrollToItem(listWidgetItem)
        self.dialogs = []
        self.pushbutton.clicked.connect(self.poisk)

    def open_book(self, title):  # метод, который открывает новое окно с
        con = sqlite3.connect('books_db.db')
        cur = con.cursor()
        elements = cur.execute(f"""SELECT * FROM books WHERE title == '{title}'""")\
            .fetchall()
        genre = cur.execute(f"""SELECT title FROM genres WHERE id == {elements[0][3]}""").fetchone()
        dialog = PopUp(elements[0][0], elements[0][1], elements[0][2], genre[0],
                       elements[0][4])  # информацией о книге
        self.dialogs.append(dialog)
        dialog.resize(700, 700)
        dialog.setWindowTitle("Информация о книге")
        dialog.show()

    def poisk(self):
        con = sqlite3.connect('books_db.db')
        cur = con.cursor()
        if self.qbox.currentText() == 'Автор':
            elements = cur.execute(f"""SELECT title FROM books WHERE author like '%{self.lineEdit.text().capitalize()}%'""").fetchall()
            self.elements = elements
        else:
            elements = cur.execute(
                f"""SELECT title FROM books WHERE title like '%{self.lineEdit.text()}%'""").fetchall()
            self.elements = elements
        self.listWidget.clear()
        for i in self.elements:
            newButton = QtWidgets.QPushButton(f'{i[0]}')
            newButton.clicked.connect(lambda btn, text=i[0]: self.open_book(text))

            listWidgetItem = QtWidgets.QListWidgetItem()
            listWidgetItem.setSizeHint(newButton.sizeHint())
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, newButton)
            self.listWidget.scrollToItem(listWidgetItem)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())
