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
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.toolbar.setIconSize(QSize(32,32))

        self.icon_dir = 'icons/'

        self.calculate_action = QAction(QIcon('gui/icons/refresh.png'), 'Calculate', self)
        self.calculate_action.setStatusTip('It calculate text')
        self.calculate_action.setShortcut('Ctrl+E')
        self.toolbar.addAction(self.calculate_action)

        self.autocalculate_action = QAction(QIcon('gui/icons/refresh_auto.png'), 'Auto calculate', self)
        self.autocalculate_action.setStatusTip('When checked it auto calulate text once changed')
        self.autocalculate_action.setCheckable(True)
        self.toolbar.addAction(self.autocalculate_action)

        self.debug_action = QAction(QIcon('gui/icons/debug.png'), 'Debug', self)
        self.debug_action.setStatusTip('When checked it shows bug tracking status')
        self.debug_action.setCheckable(True)
        self.toolbar.addAction(self.debug_action)

        self.status_bar = self.statusBar()

        #--------------------------
        self.setMinimumSize(700, 700)
        self.setWindowIcon(QIcon('gui/icons/app.ico'))

    def editor_style_edit(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: white; font-family: Courier New;}''')

    def editor_style_alert(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: rgb(255, 240, 240); font-family: Courier New;}''')

    def editor_style_done(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: rgb(240, 255, 240); font-family: Courier New;}''')