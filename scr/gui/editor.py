# This file is part of tuxCalc
import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

#--spelling imports
import enchant
from enchant import tokenize
from enchant.errors import TokenizerNotFoundError
from enchant.utils import trim_suggestions

from  greek_dict import greek_dict

class CodeEditor(QPlainTextEdit):
    def __init__(self, parent = None):
        super().__init__()
        #----to overwrite defaul undo
        self.installEventFilter(self)
        #----
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.setTabStopWidth(self.fontMetrics().width(' ') * 4)
        self.zoomIn(2)
        #--- undo stack
        self.h_stack = []
        self.h_stack_lock = False
        self.h_current_index = None
        #-----------------------------------
        #---------spelling------------------
        #-----------------------------------
        self.max_suggestions = 20
        self.highlighter = EnchantHighlighter(self.document())
        self.highlighter.setDict(enchant.Dict("en_US"))

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

    # def show_custom_menu(self, position):
    #     # Create a custom context menu
    #     menu = QMenu()
    #     cut_action = menu.addAction(QIcon('gui/icons/cut.png'), "Cut")
    #     copy_action = menu.addAction(QIcon('gui/icons/copy.png'),"Copy")
    #     paste_action = menu.addAction(QIcon('gui/icons/paste.png'),"Paste")
    #     # Connect actions to their respective methods
    #     cut_action.triggered.connect(self.cut)
    #     copy_action.triggered.connect(self.copy)
    #     paste_action.triggered.connect(self.paste)
    #     # Show the menu at the cursor position
    #     menu.exec_(self.mapToGlobal(position))

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
                    self.centerCursor()
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
                    self.centerCursor()
        return super().eventFilter(obj, event)
    #------------------------------------------------------------------
    #-------------------------spelling---------------------------------
    #------------------------------------------------------------------
    def contextMenuEvent(self, event):
        """Custom context menu handler to add a spelling suggestions submenu"""
        popup_menu = self.createSpellcheckContextMenu(event.pos())
        popup_menu.exec_(event.globalPos())
        self.focusInEvent(QFocusEvent(QEvent.FocusIn))

    def createSpellcheckContextMenu(self, pos):
        """Create and return an augmented default context menu """
        menu = QMenu()

        cut_action = menu.addAction(QIcon('gui/icons/cut.png'), "Cut")
        copy_action = menu.addAction(QIcon('gui/icons/copy.png'),"Copy")
        paste_action = menu.addAction(QIcon('gui/icons/paste.png'),"Paste")

        cut_action.triggered.connect(self.cut)
        copy_action.triggered.connect(self.copy)
        paste_action.triggered.connect(self.paste)

        if self.highlighter.is_active:
            menu.addSeparator()
            menu.addMenu(self.createLanguagesMenu(menu))
            # Try to retrieve a menu of corrections for the right-clicked word
            spell_menu = self.createCorrectionsMenu(
                self.cursorForMisspelling(pos), menu)
            if spell_menu:
                menu.insertSeparator(menu.actions()[0])
                menu.insertMenu(menu.actions()[0], spell_menu)

        return menu

    def createCorrectionsMenu(self, cursor, parent=None):
        """Create and return a menu for correcting the selected word."""
        if not cursor:
            return None

        text = cursor.selectedText()
        suggests = trim_suggestions(text,
                                    self.highlighter.dict().suggest(text),
                                    self.max_suggestions)

        spell_menu = QMenu('Spelling Suggestions', parent)
        for word in suggests:
            action = QAction(word, spell_menu)
            action.setData((cursor, word))
            spell_menu.addAction(action)

        # Only return the menu if it's non-empty
        if spell_menu.actions():
            spell_menu.triggered.connect(self.cb_correct_word)
            return spell_menu

        return None

    def createLanguagesMenu(self, parent=None):
        """Create and return a menu for selecting the spell-check language."""
        curr_lang = self.highlighter.dict().tag
        lang_menu = QMenu("Language", parent)
        lang_actions = QActionGroup(lang_menu)

        for lang in enchant.list_languages():
            action = lang_actions.addAction(lang)
            action.setCheckable(True)
            action.setChecked(lang == curr_lang)
            action.setData(lang)
            lang_menu.addAction(action)

        lang_menu.triggered.connect(self.cb_set_language)
        return lang_menu

    def cursorForMisspelling(self, pos):
        """Return a cursor selecting the misspelled word at ``pos`` or ``None``

        This leverages the fact that QPlainTextEdit already has a system for
        processing its contents in limited-size blocks to keep things fast.
        """
        cursor = self.cursorForPosition(pos)
        misspelled_words = getattr(cursor.block().userData(), 'misspelled', [])

        # If the cursor is within a misspelling, select the word
        for (start, end) in misspelled_words:
            if start <= cursor.positionInBlock() <= end:
                block_pos = cursor.block().position()

                cursor.setPosition(block_pos + start, QTextCursor.MoveAnchor)
                cursor.setPosition(block_pos + end, QTextCursor.KeepAnchor)
                break

        if cursor.hasSelection():
            return cursor
        else:
            return None

    def cb_correct_word(self, action):  # pylint: disable=no-self-use
        """Event handler for 'Spelling Suggestions' entries."""
        cursor, word = action.data()

        cursor.beginEditBlock()
        cursor.removeSelectedText()
        cursor.insertText(word)
        cursor.endEditBlock()

    def cb_set_language(self, action):
        """Event handler for 'Language' menu entries."""
        lang = action.data()
        self.highlighter.setDict(enchant.Dict(lang))

class EnchantHighlighter(QSyntaxHighlighter):
    """QSyntaxHighlighter subclass which consults a PyEnchant dictionary"""
    tokenizer = None
    token_filters = (tokenize.EmailFilter, tokenize.URLFilter)

    # Define the spellcheck style once and just assign it as necessary
    # XXX: Does QSyntaxHighlighter.setFormat handle keeping this from
    #      clobbering styles set in the data itself?
    err_format = QTextCharFormat()
    err_format.setUnderlineColor(Qt.red)
    err_format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)

    def __init__(self, *args):
        QSyntaxHighlighter.__init__(self, *args)

        # Initialize private members
        self._sp_dict = None
        self._chunkers = []
        self.is_active = True

    def chunkers(self):
        """Gets the chunkers in use"""
        return self._chunkers

    def dict(self):
        """Gets the spelling dictionary in use"""
        return self._sp_dict

    def setDict(self, sp_dict):
        """Sets the spelling dictionary to be used"""
        try:
            self.tokenizer = tokenize.get_tokenizer(sp_dict.tag,
                chunkers=self._chunkers, filters=self.token_filters)
        except TokenizerNotFoundError:
            # Fall back to the "good for most euro languages" English tokenizer
            self.tokenizer = tokenize.get_tokenizer(
                chunkers=self._chunkers, filters=self.token_filters)
        self._sp_dict = sp_dict

        self.rehighlight()

    def highlightBlock(self, text):
        """Overridden QSyntaxHighlighter method to apply the highlight"""

        if not self._sp_dict or not self.is_active:
            return

        # Build a list of all misspelled words and highlight them
        misspellings = []
        for (word, pos) in self.tokenizer(text):
            if not self._sp_dict.check(word):
                self.setFormat(pos, len(word), self.err_format)
                misspellings.append((pos, pos + len(word)))

        # Store the list so the context menu can reuse this tokenization pass
        # (Block-relative values so editing other blocks won't invalidate them)
        data = QTextBlockUserData()
        data.misspelled = misspellings
        self.setCurrentBlockUserData(data)

#spelling check based on:
#https://gist.github.com/ssokolow/0e69b9bd9ca442163164c8a9756aa15f

#On Windows, if you have installed PyEnchant from a wheel, you can download the hunspell dictionary files you need (both the .dic and .aff extensions) and put them inside /path/to/enchant/data/mingw<bits>/enchant/share/hunspell. You can find many dictionaries in:
#https://github.com/LibreOffice/dictionaries