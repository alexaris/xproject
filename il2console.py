#!/usr/bin/env python
# -*- coding: utf-8 -*

"""An atempt to write a line-oriented tool program for IL2Sturmovik.

"""

import sys
from PySide import QtGui  
from PySide import QtCore

import string
class CLInterpreter:
    """A simple class for writing line-oriented command interpreters.

    """
    prompt = '> '
    identchars = string.ascii_letters + string.digits + '_'
    
    def __init__(self):
        pass

    def parseline(self, line):
        """Parse the line into a command name and arguments.
        Returns a tuple containing (command, args).

        """
        line = line.strip()
        if not line:
            return None, None
        i, n = 0, len(line)
        while i < n and line[i] in self.identchars: i += 1
        cmd, arg = line[:i], line[i:].strip()
        return cmd, arg

    def onecommand(self, line):
        """Interpret the command.

        """
        cmd, arg = self.parseline(line)
        if not line:
            return ''
        if cmd is None:
            return ''
        if cmd == '':
            return ''
        else: 
            try:
                func = getattr(self, 'do_' + cmd)
            except AttributeError:
                return ''
            return func(arg)

    def do_help(self, arg):
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        return '%s' % str(doc)
                except AttributeError:
                    pass
                return 'there is no help for %s' % arg
            func()

class MyCLI(CLInterpreter):
    
    def __init__(self):
        CLInterpreter.__init__(self)
        self.prompt = '> '

    def do_hello(self, arg):
        """Greeting message.
        """
        if arg: arg = ' ' +  arg
        return 'hi%s!' % arg

    def do_stat(self, arg):
        return 'Tom: 12%\nJohn: 0.31%'

class Console(QtGui.QTextEdit):
    validchars = xrange(0x20, 0xFF)
    stylesheet = '''QTextEdit{color:rgb(40, 200, 70); 
                    background-color:rgb(10, 10, 10)}'''
    def __init__(self, parent=None):
        super(Console, self).__init__(parent)

        self.setCursorWidth(6)
        self.setStyleSheet(self.stylesheet);
        font = QtGui.QFont('Consolas', 11, QtGui.QFont.Bold)
        self.setFont(font)

        self.cli = MyCLI()

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

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()
        
    def init_ui(self):
        self.textEdit = Console(self)
        self.layout = QtGui.QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.textEdit)
        self.setWindowTitle('il2console')  
        self.resize(600, 300)
                
def main():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()