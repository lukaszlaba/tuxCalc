# This file is part of tuxCalc
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QToolBar, QAction, QStatusBar, QSplitter

from editor import CodeEditor
import content_text_welcome, content_text_help, content_text_about

class gui(QMainWindow):
    def __init__(self):
        super().__init__()
        #--------------------------
        self.help_editor = QPlainTextEdit()
        self.help_editor.setReadOnly(True)
        self.help_editor_style()
        self.help_editor.zoomIn(2)

        self.editor = CodeEditor()
        self.editor.highlighter.is_active = False

        self.splitter = QSplitter(Qt.Horizontal)
        self.setCentralWidget(self.splitter)

        self.splitter.addWidget(self.editor)
        self.splitter.addWidget(self.help_editor)
        self.help_editor.hide()

        self.editor_style_edit()
        self.editor.zoomIn(2)
        self.help_editor.zoomIn(2)

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
        self.zoon_in_action.setStatusTip('Zoom in font')
        self.zoon_in_action.triggered.connect(self.editor.zoomIn)
        self.zoon_in_action.triggered.connect(self.help_editor.zoomIn)
        self.toolbar.addAction(self.zoon_in_action)

        self.zoon_out_action = QAction(QIcon('gui/icons/zoom_out.png'), 'Zoom out', self)
        self.zoon_out_action.setStatusTip('Zoom out font')
        self.zoon_out_action.triggered.connect(self.editor.zoomOut)
        self.zoon_out_action.triggered.connect(self.help_editor.zoomOut)
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

        self.clbrd_paste_in_action = QAction(QIcon('gui/icons/clbrd_paste_in.png'), 'Paste in from clbrd', self)
        self.clbrd_paste_in_action.setStatusTip('Replace text by clipborard content')
        self.toolbar.addAction(self.clbrd_paste_in_action)

        self.clbrd_copy_out_action = QAction(QIcon('gui/icons/clbrd_copy_out.png'), 'Copy out to clbrd', self)
        self.clbrd_copy_out_action.setStatusTip('Copy entire text to clipboard')
        self.toolbar.addAction(self.clbrd_copy_out_action)

        self.clbrd_reload_action = QAction(QIcon('gui/icons/clbrd_reload.png'), 'Reload clbrd', self)
        self.clbrd_reload_action.setStatusTip('It paste in, calulate and then copy out to clipboard')
        self.toolbar.addAction(self.clbrd_reload_action)

        self.toolbar.addSeparator()

        self.help_action = QAction(QIcon('gui/icons/help.png'), 'Help', self)
        self.help_action.setCheckable(True)
        self.help_action.triggered.connect(self.show_help)
        self.toolbar.addAction(self.help_action)

        self.about_action = QAction(QIcon('gui/icons/about.png'), 'About', self)
        self.about_action.setCheckable(True)
        self.about_action.triggered.connect(self.show_about)
        self.toolbar.addAction(self.about_action)

        self.toolbar.addSeparator()

        self.spelling_action = QAction(QIcon('gui/icons/spelling.png'), 'Spelling check', self)
        self.spelling_action.setCheckable(True)
        self.spelling_action.triggered.connect(self.activate_spelling)
        self.toolbar.addAction(self.spelling_action)

        self.toolbar.addSeparator()

        self.print_action = QAction(QIcon('gui/icons/print.png'), 'Print', self)
        self.toolbar.addAction(self.print_action)

        self.status_bar = self.statusBar()

        #--------------------------
        self.setMinimumSize(750, 820)
        self.setWindowIcon(QIcon('gui/icons/app.ico'))

    def editor_style_edit(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: white; font-family: Courier New;}''')

    def editor_style_alert(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: rgb(255, 240, 240); font-family: Courier New;}''')

    def editor_style_done(self):
        self.editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: rgb(240, 255, 240); font-family: Courier New;}''')

    def help_editor_style(self):
        self.help_editor.setStyleSheet('''QPlainTextEdit {padding-left:2; background-color: rgb(235, 235, 255); font-family: Courier New;}''')

    def show_help(self):
        self.about_action.setChecked(False)
        if self.help_action.isChecked():
            self.help_editor.show()
            self.help_editor.setPlainText(content_text_help.text)
        else:
            self.help_editor.hide()

    def show_about(self):
        self.help_action.setChecked(False)
        if self.about_action.isChecked():
            self.help_editor.show()
            self.help_editor.setPlainText(content_text_about.text)
        else:
            self.help_editor.hide()

    def activate_spelling(self):
        if self.spelling_action.isChecked():
            self.editor.highlighter.is_active = True
        else:
            self.editor.highlighter.is_active = False
        self.editor.highlighter.rehighlight()

    def show_welcom_text(self):
        self.editor.setPlainText(content_text_welcome.text)
