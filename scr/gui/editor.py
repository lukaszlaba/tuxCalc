from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from  greek_dict import greek_dict

class CodeEditor(QPlainTextEdit):
    def __init__(self, parent = None):
        super().__init__()
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

    def insert_unicode_prime_character(self):
        self.insertPlainText("ʹ") # this is U+02B9 unicode prime character that can be used for variable name
        
    def insert_asign_sign(self):
        self.insertPlainText(":=")
        
    def open_file(self):
        print('open')

    def save_file(self):
        print('save')

    def save_file_as(self):
        print('save as')