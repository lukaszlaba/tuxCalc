from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QToolBar, QAction, QStatusBar


class gui(QMainWindow):
    def __init__(self):
        super().__init__()
        #--------------------------
        self.editor = QPlainTextEdit()
        self.setCentralWidget(self.editor)
        self.editor_style_edit()
        self.editor.zoomIn(5)

        self.toolbar = QToolBar('My main toolbar')
        self.addToolBar(self.toolbar)
        self.toolbar.setIconSize(QSize(32,32))

        self.icon_dir = 'icons/'

        self.calculate_action = QAction(QIcon('gui/icons/refresh.png'), 'Calculate', self)
        self.calculate_action.setStatusTip('It calculate text')
        self.calculate_action.setShortcut('Ctrl+E')
        self.toolbar.addAction(self.calculate_action)

        self.autocalculate_action = QAction(QIcon('gui/icons/refresh_auto.png'), 'Auto calculate', self)
        self.autocalculate_action.setStatusTip('It auto calulate test once chaged')
        self.autocalculate_action.setCheckable(True)
        self.toolbar.addAction(self.autocalculate_action)

        self.status_bar = self.statusBar()

        #--------------------------
        self.setMinimumSize(500, 500)
        self.setWindowIcon(QIcon('gui/icons/textcalc.png'))

    def editor_style_edit(self):
        self.editor.setStyleSheet('''QPlainTextEdit {background-color: white; font-family: Courier New;}''')

    def editor_style_alert(self):
        self.editor.setStyleSheet('''QPlainTextEdit {background-color: rgb(255, 240, 240); font-family: Courier New;}''')

    def editor_style_done(self):
        self.editor.setStyleSheet('''QPlainTextEdit {background-color: rgb(240, 255, 240); font-family: Courier New;}''')