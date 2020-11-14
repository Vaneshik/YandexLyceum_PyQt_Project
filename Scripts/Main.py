from UI.mainUI import Ui_MainWindow
from UI.searchUI import Ui_Form
from UI.listsUI import Ui_Form as Ui_Form1

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize

import sys
import sqlite3


class QuitedButton(QPushButton):
    """Кнопка брошенных аниме"""

    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        ico = QIcon()
        ico.addFile('../Icons/break_off.png', mode=QIcon.Selected, state=QIcon.Off)
        ico.addFile('../Icons/break_on.png', mode=QIcon.Selected, state=QIcon.On)
        self.setIcon(ico)
        self.setIconSize(QSize(60, 60))
        self.setFixedSize(60, 60)


class ViewedButton(QPushButton):
    """Кнопка просмотренных аниме"""

    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        ico = QIcon()
        ico.addFile('../Icons/done_off.png', mode=QIcon.Selected, state=QIcon.Off)
        ico.addFile('../Icons/done_on.png', mode=QIcon.Selected, state=QIcon.On)
        self.setIcon(ico)
        self.setIconSize(QSize(60, 60))
        self.setFixedSize(60, 60)


class FavourButton(QPushButton):
    """Кнопка избранных аниме"""

    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        ico = QIcon()
        ico.addFile('../Icons/star_off.png', mode=QIcon.Selected, state=QIcon.Off)
        ico.addFile('../Icons/star_on.png', mode=QIcon.Selected, state=QIcon.On)
        self.setIcon(ico)
        self.setIconSize(QSize(60, 60))
        self.setFixedSize(60, 60)


class FutureButton(QPushButton):
    """Кнопка буду смотерть"""

    def __init__(self):
        super().__init__()
        self.setCheckable(True)
        ico = QIcon()
        ico.addFile('../Icons/future_off.png', mode=QIcon.Selected, state=QIcon.Off)
        ico.addFile('../Icons/future_on.png', mode=QIcon.Selected, state=QIcon.On)
        self.setIcon(ico)
        self.setIconSize(QSize(60, 60))
        self.setFixedSize(60, 60)


class AnimeForm(QWidget):
    """Ячейка для данных из аниме"""

    def __init__(self, anime_id, title, orig_name):
        super().__init__()

        self.id = anime_id
        self.title = title
        self.orig_name = orig_name if len(orig_name) < 55 else orig_name[:52] + '...'

        self.btn1 = FavourButton()
        self.btn2 = ViewedButton()
        self.btn3 = QuitedButton()
        self.btn4 = FutureButton()

        self.load_ui()

    def add_to_favourite(self):
        cur.execute("UPDATE anime SET is_favourite=? WHERE id=?", (self.btn1.isChecked(), self.id))

    def add_to_viewed(self):
        cur.execute("UPDATE anime SET is_viewed=? WHERE id=?", (self.btn2.isChecked(), self.id))

    def add_to_quited(self):
        cur.execute("UPDATE anime SET is_quit=? WHERE id=?", (self.btn3.isChecked(), self.id))

    def add_to_future(self):
        cur.execute("UPDATE anime SET is_future=? WHERE id=?", (self.btn4.isChecked(), self.id))

    def load_ui(self):
        self.setStyleSheet("""background: #C4C4C4;
border: 1px solid #000000;
border-radius: 20px;""")
        layout = QHBoxLayout(self)
        self.setLayout(layout)

        img = QLabel(self)
        img_to_add = QPixmap(f'../Data/images/resized/{int(self.id) - 1}.jpg')
        img.setPixmap(img_to_add)
        img.setScaledContents(True)
        img.setFixedSize(60, 60)

        title = QLabel(f'{self.title}\n({self.orig_name})', self)
        title.setFixedHeight(60)

        data = cur.execute("SELECT is_favourite, is_viewed, is_quit, is_future FROM anime WHERE id=?",
                           (self.id,)).fetchone()

        if data[0] == 1:
            self.btn1.setChecked(True)

        if data[1] == 1:
            self.btn2.setChecked(True)

        if data[2] == 1:
            self.btn3.setChecked(True)

        if data[3] == 1:
            self.btn4.setChecked(True)

        layout.addWidget(img)
        layout.addWidget(title)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)

        self.btn1.clicked.connect(self.add_to_favourite)
        self.btn2.clicked.connect(self.add_to_viewed)
        self.btn3.clicked.connect(self.add_to_quited)
        self.btn4.clicked.connect(self.add_to_future)


class Lists(QWidget, Ui_Form1):
    """Окно со спсками"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.layout_scroll = QVBoxLayout(self)
        self.frame = QWidget(self)
        self.frame.setLayout(self.layout_scroll)
        self.scrollArea.setWidget(self.frame)
        self.display_viewed()

        self.pushButton.clicked.connect(to_main)
        self.favour_butn.clicked.connect(self.display_favour)
        self.viewed_butn.clicked.connect(self.display_viewed)
        self.quited_butn.clicked.connect(self.display_quited)
        self.future_butn.clicked.connect(self.display_future)
        self.future_butn.clicked.connect(self.display_future)

    def display_favour(self):
        clear_layout(self.layout_scroll)
        res = cur.execute("SELECT id, title, orig_name FROM anime WHERE is_favourite=TRUE").fetchall()
        for item in res:
            frame = AnimeForm(item[0], item[1], item[2])
            self.layout_scroll.addWidget(frame)

    def display_viewed(self):
        clear_layout(self.layout_scroll)
        res = cur.execute("SELECT id, title, orig_name FROM anime WHERE is_viewed=TRUE").fetchall()
        for item in res:
            frame = AnimeForm(item[0], item[1], item[2])
            self.layout_scroll.addWidget(frame)

    def display_quited(self):
        clear_layout(self.layout_scroll)
        res = cur.execute("SELECT id, title, orig_name FROM anime WHERE is_quit=TRUE").fetchall()
        for item in res:
            frame = AnimeForm(item[0], item[1], item[2])
            self.layout_scroll.addWidget(frame)

    def display_future(self):
        clear_layout(self.layout_scroll)
        res = cur.execute("SELECT id, title, orig_name FROM anime WHERE is_future=TRUE").fetchall()
        for item in res:
            frame = AnimeForm(item[0], item[1], item[2])
            self.layout_scroll.addWidget(frame)


class Search(QWidget, Ui_Form):
    """Окно поиска"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(to_main)
        self.pushButton_2.clicked.connect(self.search_bd)

        self.layout_scroll = QVBoxLayout(self)
        self.wget = QWidget(self)
        self.wget.setLayout(self.layout_scroll)
        self.scrollArea.setWidget(self.wget)

        self.load_all()

    def load_all(self):
        """Вывод всех аниме"""
        res = cur.execute("SELECT id, title, orig_name FROM anime").fetchall()
        for item in res:
            frame = AnimeForm(item[0], item[1], item[2])
            self.layout_scroll.addWidget(frame)

    def search_bd(self):
        """Поиск и вывод аниме"""
        clear_layout(self.layout_scroll)
        text = self.lineEdit.text()
        text = '%' + text.replace(' ', '%') + '%'
        res = cur.execute(
            f'SELECT id, title, orig_name FROM anime WHERE title LIKE ? OR orig_name LIKE ? COLLATE NOCASE',
            (text, text)).fetchall()
        for item in res:
            frame = AnimeForm(item[0], item[1], item[2])
            self.layout_scroll.addWidget(frame)


class Main(QMainWindow, Ui_MainWindow):
    """Главное окно"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.to_search)
        self.pushButton_2.clicked.connect(self.to_lists)

    @staticmethod
    def to_search():
        main_window.hide()
        search_window.show()

    @staticmethod
    def to_lists():
        main_window.hide()
        lists_window.show()


def to_main():
    data_base.commit()
    lists_window.hide()
    search_window.hide()
    main_window.show()


def clear_layout(layout):
    for i in range(layout.count()):
        layout.itemAt(i).widget().deleteLater()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    data_base = sqlite3.connect('../baseDB.db')
    cur = data_base.cursor()
    app = QApplication(sys.argv)
    main_window = Main()
    search_window = Search()
    lists_window = Lists()
    main_window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
