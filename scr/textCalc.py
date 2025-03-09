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
from PyQt5.QtGui import QIcon

from gui.gui import gui as _gui
from pycore.ctxext_process import process, remove_debug_notyfications

app_name = 'textCalc'

version = '0.0.1'

class _gui(_gui):
    def __init__(self):
        super().__init__()
        #--------
        self.setWindowTitle(f'{app_name} {version}')
        #--------
        self.calculate_action.triggered.connect(calculate)
        self.autocalculate_action.triggered.connect(calculate)
        self.editor.textChanged.connect(txt_changed_action)
        self.debug_action.triggered.connect(calculate)

def calculate():
    # get cursor position to plece it back later
    pos = gui.editor.textCursor().position()
    #----
    txt = gui.editor.toPlainText()
    #---
    out = process(txt)
    out_txt = out[0]
    if not gui.debug_action.isChecked():
        out_txt = remove_debug_notyfications(out_txt)
    has_no_bugs = out[1]
    #---
    gui.editor.setPlainText(out_txt)
    gui.editor_style_done()
    gui.status_bar.showMessage('Calculated with no bugs.')
    if not has_no_bugs:
        gui.editor_style_alert()
        gui.status_bar.showMessage('Calculated with bugs. ( !!! )')
    # place cursor back after all so user can easly continue editing the text
    cursor = gui.editor.textCursor()
    cursor.setPosition(pos)
    gui.editor.setTextCursor(cursor)

def txt_changed_action():
    # change backgroud color in to white as text changed
    gui.editor_style_edit()
    # if autocalculate checked recalulate
    if gui.autocalculate_action.isChecked():
        # turn off text watching for now
        gui.editor.textChanged.disconnect()
        #----------
        calculate()
        #----------
        # turn on back text watching after all
        gui.editor.textChanged.connect(txt_changed_action)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui =_gui()
    gui.show()
    # welcom text
    from pycore.start_ctext import ctext
    gui.editor.setPlainText(ctext)
    #--------
    app.exec()

'''
Icon
https://icon-icons.com/icon/math-plus-minus/158290
command used to frozening with pyinstaller
pyinstaller --noconsole --icon=app.ico C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_TEXTCALC\source\scr\textCalc.py
'''