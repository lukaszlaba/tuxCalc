from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QToolBar, QAction, QStatusBar

from editor import CodeEditor


class gui(QMainWindow):
    def __init__(self):
        super().__init__()
        #--------------------------
        self.editor = CodeEditor()
        self.setCentralWidget(self.editor)
        self.editor_style_edit()
        self.editor.zoomIn(2)

        self.toolbar = QToolBar('My main toolbar')
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.toolbar.setIconSize(QSize(32,32))

        self.icon_dir = 'icons/'

        self.open_action = QAction(QIcon('gui/icons/open.png'), 'Open', self)
        self.toolbar.addAction(self.open_action)

        self.save_action = QAction(QIcon('gui/icons/save.png'), 'Save [Ctrl+S]', self)
        self.save_action.setShortcut('Ctrl+S')
        self.toolbar.addAction(self.save_action)

        self.saveas_action = QAction(QIcon('gui/icons/saveas.png'), 'Save_as', self)
        self.toolbar.addAction(self.saveas_action)

        self.toolbar.addSeparator()

        self.calculate_action = QAction(QIcon('gui/icons/refresh.png'), 'Calculate [Ctrl+E]', self)
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

        self.toolbar.addSeparator()

        self.float_precision_action = QAction(QIcon('gui/icons/float.png'), 'Float display precision', self)
        self.float_precision_action.setStatusTip('It allow to set float display precision ')
        self.toolbar.addAction(self.float_precision_action)

        self.toolbar.addSeparator()

        self.zoon_in_action = QAction(QIcon('gui/icons/zoom_in.png'), 'Zoom in', self)
        self.zoon_in_action.setStatusTip('Zoom in font in editor')
        self.zoon_in_action.triggered.connect(self.editor.zoomIn)
        self.toolbar.addAction(self.zoon_in_action)

        self.zoon_out_action = QAction(QIcon('gui/icons/zoom_out.png'), 'Zoom out', self)
        self.zoon_out_action.setStatusTip('Zoom out font in editor')
        self.zoon_out_action.triggered.connect(self.editor.zoomOut)
        self.toolbar.addAction(self.zoon_out_action)

        self.toolbar.addSeparator()

        self.udot_action = QAction(QIcon('gui/icons/udot.png'), 'Format udot', self)
        self.udot_action.setStatusTip('Update u.m into [m]')
        self.toolbar.addAction(self.udot_action)

        self.greek_action = QAction(QIcon('gui/icons/greek.png'), 'Insert greek letter [Ctrl+G]', self)
        self.greek_action.setStatusTip('It isert greek letter')
        self.greek_action.triggered.connect(self.editor.insert_greek_letter)
        self.greek_action.setShortcut('Ctrl+G')
        self.toolbar.addAction(self.greek_action)

        self.prime_action = QAction(QIcon('gui/icons/prime.png'), 'Insert prime sign', self)
        self.prime_action.setStatusTip('It insert prime_action')
        self.prime_action.triggered.connect(self.editor.insert_unicode_prime_character)
        self.toolbar.addAction(self.prime_action)

        self.asign_action = QAction(QIcon('gui/icons/asign.png'), 'Insert asign := sign [Ctrl+;]', self)
        self.asign_action.setStatusTip('It insert asign sign')
        self.asign_action.triggered.connect(self.editor.insert_asign_sign)
        self.asign_action.setShortcut('Ctrl+;')
        self.toolbar.addAction(self.asign_action)

        self.toolbar.addSeparator()

        self.print_action = QAction(QIcon('gui/icons/print.png'), 'Print', self)
        self.toolbar.addAction(self.print_action)

        self.status_bar = self.statusBar()

        #--------------------------
        self.setMinimumSize(750, 700)
        self.setWindowIcon(QIcon('gui/icons/app.ico'))

    def editor_style_edit(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: white; font-family: Courier New;}''')

    def editor_style_alert(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: rgb(255, 240, 240); font-family: Courier New;}''')

    def editor_style_done(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: rgb(240, 255, 240); font-family: Courier New;}''')