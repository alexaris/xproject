# -*- coding: utf-8 -*
import sys
from PySide import QtGui  
from PySide import QtCore

import mycli
import history

class Console(QtGui.QTextEdit):
    hackcmd = 'hack_'
    validchars = xrange(0x20, 0xFF)
    stylesheet = '''QTextEdit{color:rgb(40, 200, 70); 
                    background-color:rgb(10, 10, 10)}'''

    history = history.History()
    pos = 0
    recent_line = ''

    def __init__(self, parent=None):
        super(Console, self).__init__(parent)
        self.parent = parent
        self.setCursorWidth(6)
        self.setStyleSheet(self.stylesheet);
        font = QtGui.QFont('Consolas', 10, QtGui.QFont.Normal)
        self.setFont(font)

        self.cli = mycli.MyCLI()

        self.prompt = self.cli.prompt
        self.cursorPosition = 0
        
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)
        self.append(self.prompt)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            if self.cursorPosition > 0: 
                QtGui.QTextEdit.keyPressEvent(self, event)
                self.cursorPosition -= 1
        
        elif event.key() == QtCore.Qt.Key_Return:
            self.recent_line = self.textCursor().block().text()[len(self.prompt):]
            self.history.add(self.recent_line)
            t = self.cli.onecommand(self.recent_line)
            if t != None:
                if t[:len(self.hackcmd)] == self.hackcmd:
                    self.handle_hackcmd(t)
                else:
                    if t != '': 
                        self.append(t.strip())
                        
                
            self.lastcontent = self.toPlainText()
            self.append(self.prompt)
            self.cursorPosition = 0
            self.pos = self.history.size() - 1
        
        elif event.key() in self.validchars:
            QtGui.QTextEdit.keyPressEvent(self, event)
            self.cursorPosition += 1
        
        elif event.key() == QtCore.Qt.Key_Up:
            self.show_history('up')
        
        elif event.key() == QtCore.Qt.Key_Down:
            self.show_history('down')
        
        else: 
            event.ignore()
    
    def mousePressEvent(self, event):
        event.ignore()

    def show_history(self, direction):
        if direction == 'up': self.pos -= 1
        if direction == 'down': self.pos += 1
        if self.pos < 0: self.pos = self.history.size() - 1
        if self.pos >= self.history.size(): self.pos = 0

        s = self.textCursor().block().text()[len(self.prompt):]
        for i in range(len(s)):
            self.textCursor().deletePreviousChar()
        self.textCursor().insertText(self.history.queue[self.pos])
     
        
    def handle_hackcmd(self, cmd):
        cmd = cmd.replace(self.hackcmd, '')
        if cmd == 'exit':
            self.parent.close()
        if cmd == 'clear':
            self.setText('')

