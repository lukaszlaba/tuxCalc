import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtGui import QTextCursor

from  greek_dict import greek_dict

from spell import SpellTextEdit

class CodeEditor(SpellTextEdit):
    def __init__(self, parent = None):
        super().__init__()
        #----to overwrite defaul undo
        self.installEventFilter(self)
        #----
        #self.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.customContextMenuRequested.connect(self.show_custom_menu)
        #----
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.setTabStopWidth(self.fontMetrics().width(' ') * 4)
        self.zoomIn(2)
        #--- undo stack
        self.h_stack = []
        self.h_stack_lock = False
        self.h_current_index = None

    def clear_history(self):
        self.h_stack = []
        self.h_stack_lock = False
        self.h_current_index = None

    def add_to_history_stack(self):
        if not self.h_stack_lock:
            if self.h_stack:
                del self.h_stack[0: self.h_current_index]
            text = self.toPlainText()
            pos = self.textCursor().position()
            self.h_stack.insert(0, [text, pos])
            self.h_current_index = 0
            if len(self.h_stack) == 200:
                self.h_stack.pop()

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
                #custom undo logic
                if 0 <= self.h_current_index+1 < len(self.h_stack)-1:
                    self.h_current_index += 1
                    self.h_stack_lock = True
                    self.setPlainText(self.h_stack[self.h_current_index][0])
                    self.h_stack_lock = False
                    cursor = self.textCursor()
                    cursor.setPosition(self.h_stack[self.h_current_index][1])
                    self.setTextCursor(cursor)
            elif event.key() == Qt.Key_Y and event.modifiers() == Qt.ControlModifier:
                #custom redo logic
                if 0 <= self.h_current_index-1 < len(self.h_stack)-1:
                    self.h_current_index -= 1
                    self.h_stack_lock = True
                    self.setPlainText(self.h_stack[self.h_current_index][0])
                    self.h_stack_lock = False
                    cursor = self.textCursor()
                    cursor.setPosition(self.h_stack[self.h_current_index][1])
                    self.setTextCursor(cursor)
        return super().eventFilter(obj, event)
