import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtGui import QTextCursor

from  greek_dict import greek_dict

class CodeEditor(QPlainTextEdit):
    def __init__(self, parent = None):
        super().__init__()

        self.installEventFilter(self)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_custom_menu)

        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.setTabStopWidth(self.fontMetrics().width(' ') * 4)
        self.zoomIn(2)

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor(Qt.lightGray).lighter(120)
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def insert_greek_letter(self):
        #what is the letter before cursor
        cursor_possition = self.textCursor().position()
        letter_before_cursor = self.toPlainText()[cursor_possition-1]
        if letter_before_cursor in greek_dict.keys():
            #what is the greek letter assigned to letter before cursor
            greek_letter = greek_dict[letter_before_cursor]
            #replace letter before cursor by the assigned greek letter
            self.textCursor().deletePreviousChar()
            self.insertPlainText(greek_letter)
        else:
            pass

    def update_text(self, text):
        # get cursor position to place it back later
        pos = self.textCursor().position()
        # get scrol position to place it back later
        vsb = self.verticalScrollBar()
        old_pos_ratio = vsb.value() / (vsb.maximum() or 1)
        #--------------updateing text-------------------
        self.setPlainText(text)
        # place cursor back after all so user can easly continue editing the text
        cursor = self.textCursor()
        cursor.setPosition(pos)
        self.setTextCursor(cursor)
        # place scrolback after all so user can easly continue editing the text
        vsb.setValue(round(old_pos_ratio * vsb.maximum()))


    def insert_unicode_prime_character(self):
        self.insertPlainText("ʹ") # this is U+02B9 unicode prime character that can be used for variable name

    def insert_asign_sign(self):
        self.insertPlainText(":=")



    def show_custom_menu(self, position):
        # Create a custom context menu
        menu = QMenu()
        cut_action = menu.addAction(QIcon('gui/icons/cut.png'), "Cut")
        copy_action = menu.addAction(QIcon('gui/icons/copy.png'),"Copy")
        paste_action = menu.addAction(QIcon('gui/icons/paste.png'),"Paste")
        # Connect actions to their respective methods
        cut_action.triggered.connect(self.cut)
        copy_action.triggered.connect(self.copy)
        paste_action.triggered.connect(self.paste)
        # Show the menu at the cursor position
        menu.exec_(self.mapToGlobal(position))

    def eventFilter(self, obj, event):
        if obj == self and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Z and event.modifiers() == Qt.ControlModifier:
                print("Custom undo triggered")
                # Perform custom undo logic here
                return True
            elif event.key() == Qt.Key_Y and event.modifiers() == Qt.ControlModifier:
                print("Custom redo triggered")
                # Perform custom redo logic here
                return True
        return super().eventFilter(obj, event)


