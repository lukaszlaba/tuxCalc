# -*- coding: utf-8 -*-
#-----------------------------------------------------------------
# Copyright (C) 2025, Lukasz Laba
#
# This file is part of calcText
# calcText is distributed under the terms of GNU General Public License
# The full license can be found in 'license.txt'
#-----------------------------------------------------------------



import sys

from PyQt5.QtWidgets import QApplication

from gui.gui import gui as _gui
from core.core_functions import process

app_name = 'textCalc'

version = '0.0.1'

class _gui(_gui):
    def __init__(self):
        super().__init__()
        #--------
        self.setWindowTitle(f'{app_name} {version}')
        #--------
        self.calculate_action.triggered.connect(calculate)
        self.editor.textChanged.connect(txt_changed_action)

def calculate():
    txt = gui.editor.toPlainText()
    try:
        out_txt = process(txt)
        gui.editor.setPlainText(out_txt)
        gui.editor_style_done()
    except:
        gui.editor_style_alert()

def txt_changed_action():
    gui.editor.textChanged.disconnect()
    gui.editor_style_edit()
    pos = gui.editor.textCursor().position()

    calculate()

    gui.editor.textChanged.connect(txt_changed_action)
    cursor = gui.editor.textCursor()
    cursor.setPosition(pos)
    gui.editor.setTextCursor(cursor)


app = QApplication(sys.argv)
gui =_gui()
gui.show()
app.exec()
