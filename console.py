import sys
from PySide import QtGui  
from PySide import QtCore

import mycli

class Console(QtGui.QTextEdit):
    validchars = xrange(0x20, 0xFF)
    stylesheet = '''QTextEdit{color:rgb(40, 200, 70); 
                    background-color:rgb(10, 10, 10)}'''
    def __init__(self, parent=None):
        super(Console, self).__init__(parent)
        self.parent = parent
        self.setCursorWidth(6)
        self.setStyleSheet(self.stylesheet);
        font = QtGui.QFont('Consolas', 11, QtGui.QFont.Normal)
        self.setFont(font)

        self.cli = mycli.MyCLI()

        self.prompt = self.cli.prompt
        self.lastcontent = ''
        self.lastblock = ''
        self.cursorPosition = 0
        
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)
        self.append(self.prompt)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            if self.cursorPosition > 0: 
                QtGui.QTextEdit.keyPressEvent(self, event)
                self.cursorPosition -= 1
        elif event.key() == QtCore.Qt.Key_Return:
            content = self.toPlainText()
            self.lastblock = content.replace(self.lastcontent, '')
            s = self.lastblock[len(self.prompt):].strip()
            t = self.cli.onecommand(s)
            if t == '!exit': QtCore.QCoreApplication.quit()
            if t != '': self.append(t)
            self.lastcontent = self.toPlainText()
            self.append(self.prompt)
            self.cursorPosition = 0
        
        elif event.key() in self.validchars:
            QtGui.QTextEdit.keyPressEvent(self, event)
            self.cursorPosition += 1
        else: 
            event.ignore()
    
    def mousePressEvent(self, event):
        event.ignore()

    #TODO! add command history (max 10 commands)