#!/usr/bin/env python
# -*- coding: utf-8 -*

"""An atempt to write a line-oriented tool program for IL2Sturmovik.

"""

import sys
from PySide import QtGui  
from PySide import QtCore

def evalute(text):
    print list(text)
    if 'hello' in text:
        return 'hi!'
    if 'list' in text:
        return u'петя\nвася'
    if 'help' in text:
        return u'sorry, there is no help'
    if text == '': return ''
    else: 
        return 'unknown command'

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
        return cmd, arg #, line

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


class MyCLI(CLInterpreter):
    def __init__(self):
        CLInterpreter.__init__(self)
        self.prompt = '> '

    def do_hello(self, arg):
        return 'hi %s!' % arg


class Console(QtGui.QTextEdit):
    def __init__(self, parent=None):
        super(Console, self).__init__(parent)
        self.cli = MyCLI()

        self.prompt = self.cli.prompt
        self.lastcontent = ''
        self.lastblock = ''
        self.cursorPosition = 0
        
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)
        self.setCursorWidth(6)

        self.append(self.prompt)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            if self.cursorPosition > 0: 
                QtGui.QTextEdit.keyPressEvent(self, event)
                self.cursorPosition -= 1
                print self.cursorPosition

        elif event.key() == QtCore.Qt.Key_Return:
            content = self.toPlainText()
            self.lastblock = content.replace(self.lastcontent, '')
            s = self.lastblock[len(self.prompt):].strip()
            #t =  evalute(s)
            t = self.cli.onecommand(s)
            if t != '': self.append(t)
            self.lastcontent = self.toPlainText()
            self.append(self.prompt)
            self.cursorPosition = 0
        elif (event.key() == QtCore.Qt.Key_Up or
              event.key() == QtCore.Qt.Key_Down or
              event.key() == QtCore.Qt.Key_Left or
              event.key() == QtCore.Qt.Key_Right):
            event.ignore()

        else:
            QtGui.QTextEdit.keyPressEvent(self, event)
            self.cursorPosition += 1
            print self.cursorPosition
       
    def mousePressEvent(self, event):
        event.ignore()

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()
        
    def init_ui(self):
        self.edit = Console(self)
        self.layout = QtGui.QGridLayout(self)
        self.layout.addWidget(self.edit)
        self.setWindowTitle('il2console')  
                
def main():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()