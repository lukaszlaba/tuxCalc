# -*- coding: utf-8 -*-
#-----------------------------------------------------------------
# Copyright (C) 2025, Lukasz Laba
#
# This file is part of tuxCalc
# tuxCalc is distributed under the terms of GNU General Public License
# The full license can be found in 'license.txt'
#-----------------------------------------------------------------
import sys
import os

import enchant
import unum


import codecs

from PyQt5.QtWidgets import QApplication, QInputDialog, QFileDialog, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtGui import QClipboard

from gui.gui import gui as _gui
from pycore import ctext_process
from pycore.ctext_process import process, remove_debug_notyfications, format_udot

APPNAME = 'tuxCalc'
VERSION = '0.2.1'
FILEPATH = ''
SAVEDIR = ''

class _gui(_gui):
    def __init__(self):
        super().__init__()
        #--------
        self.updateWindowTitle()
        #--------
        self.open_action.triggered.connect(open_file)
        self.save_action.triggered.connect(save_file)
        self.saveas_action.triggered.connect(save_file_as)
        self.calculate_action.triggered.connect(calculate)
        self.autocalculate_action.triggered.connect(calculate)
        self.debug_action.triggered.connect(calculate)
        self.float_precision_action.triggered.connect(set_float_precision)
        self.udot_action.triggered.connect(replace_udot)
        self.print_action.triggered.connect(print_file)
        self.clbrd_paste_in_action.triggered.connect(paste_in_from_clipboard)
        self.clbrd_copy_out_action.triggered.connect(copy_out_to_clipboard)
        self.clbrd_reload_action.triggered.connect(update_clipboard)

        #--------
        self.editor.textChanged.connect(txt_changed_action)

    def updateWindowTitle(self):
        if FILEPATH:
            title = f'{APPNAME} {VERSION} - {FILEPATH}'
        else:
            title = f'{APPNAME} {VERSION} - Untitled'
        self.setWindowTitle(title)

def calculate():
    txt = gui.editor.toPlainText()
    #---
    out = process(txt)
    out_txt = out[0]
    if not gui.debug_action.isChecked():
        out_txt = remove_debug_notyfications(out_txt)
    has_no_bugs = out[1]
    #---
    gui.editor.update_text(out_txt)
    #---
    gui.editor_style_done()
    gui.status_bar.showMessage('Calculated with no bugs')
    if not has_no_bugs:
        gui.editor_style_alert()
        gui.status_bar.showMessage('Calculated with bugs ( !!! )')

def txt_changed_action():
    # change backgroud color in to edit style
    gui.editor_style_edit()
    gui.editor.add_to_history_stack()
    # if autocalculate checked recalulate
    if gui.autocalculate_action.isChecked():
        # turn off text watching for now
        gui.editor.textChanged.disconnect()
        #----------
        calculate()
        #----------
        # turn on back text watching after all
        gui.editor.textChanged.connect(txt_changed_action)

def set_float_precision():
    #---asking for precision as int number
    value = QInputDialog.getInt(    None,
                                    'Float display precysion', 'Set the precison:',
                                    value = ctext_process.float_precision,
                                    min = 1, max = 9, step = 1)[0]
    ctext_process.set_float_precision(value)
    calculate()

def replace_udot():
    txt = gui.editor.toPlainText()
    txt = format_udot(txt)
    gui.editor.setPlainText(txt)
    calculate()

def open_file(self):
    global FILEPATH
    global SAVEDIR
    filename = QFileDialog.getOpenFileName(caption = 'Open text file',
                                            directory = SAVEDIR,
                                            filter = "Text file (*.txt);;All (*.*)")
    filename = str(filename[0])
    #---
    try:
        SAVEDIR = os.path.dirname(filename)
        FILEPATH = filename
        file = codecs.open(FILEPATH, 'r', 'utf-8')
        text = file.read()
        file.close()
        gui.editor.setPlainText(text)
        gui.updateWindowTitle()
        gui.status_bar.showMessage(f'opened {FILEPATH}')
        gui.editor.clear_history()
    except:
        gui.status_bar.showMessage('opening not successful')

def save_file():
    if FILEPATH:
        new_file = codecs.open(FILEPATH,'w', 'utf-8')
        new_file.write(gui.editor.toPlainText())
        new_file.close()
        gui.status_bar.showMessage('saved')
    else:
        save_file_as()

def save_file_as():
    global FILEPATH
    global SAVEDIR
    if FILEPATH:
        newname = 'Copy_' + os.path.basename(FILEPATH)
    else:
        newname = 'new_textcalc.txt'
    #---asking for file path
    initdir = SAVEDIR + '/' + newname
    filename = QFileDialog.getSaveFileName(caption = 'Save as',
                                            directory = initdir,
                                            filter = "Text file (*.txt)")
    filename = str(filename[0])
    try:
        new_file = codecs.open(filename,'w', 'utf-8')
        new_file.write(gui.editor.toPlainText())
        new_file.close()
        #---
        FILEPATH = filename
        SAVEDIR = os.path.dirname(filename)
        gui.updateWindowTitle()
        gui.status_bar.showMessage(f'saved as {FILEPATH}')
    except:
        gui.status_bar.showMessage('saving not successful')

def print_file():
    dialog = QPrintDialog(gui)
    if dialog.exec_() == QDialog.Accepted:
        gui.editor.document().print_(dialog.printer())

def copy_out_to_clipboard():
    text = gui.editor.toPlainText()
    cb = QApplication.clipboard()
    cb.setText(text)
    gui.status_bar.showMessage('text in clipboard')

def paste_in_from_clipboard():
    cb = QApplication.clipboard()
    text = cb.text()
    if text:
        gui.editor.setPlainText(text)
        gui.status_bar.showMessage('text pasted')
        return True
    else:
        gui.status_bar.showMessage('no text in clipboard')
        return False


def update_clipboard():
    if paste_in_from_clipboard():
        calculate()
        copy_out_to_clipboard()
        gui.status_bar.showMessage('recalulated text in clipboard')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui =_gui()
    gui.show()
    ctext_process.set_float_precision(2)
    # welcome text
    gui.show_welcom_text()
    calculate()
    #--------
    app.exec()


#Icon
#https://icon-icons.com/icon/math-plus-minus/158290
#command used to frozening with pyinstaller
#pyinstaller --noconsole --icon=app.ico C:\Users\Lenovo\Dropbox\PYAPPS_STRUCT\SOURCE_TUXCALC\source\scr\tuxCalc.py