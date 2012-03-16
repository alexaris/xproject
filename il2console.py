#!/usr/bin/env python
# -*- coding: utf-8 -*

'''il2console test'''

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

class Console(QtGui.QTextEdit):
    def __init__(self, parent=None):
        super(Console, self).__init__(parent)
        
        self.prompt = '> '
        self.lastcontent = ''
        self.lastblock = ''
        self.counter = 0
        
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)
        self.setCursorWidth(6)

        self.append(self.prompt)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            if self.counter > 0: 
                QtGui.QTextEdit.keyPressEvent(self, event)
                self.counter -= 1
                print self.counter

        elif event.key() == QtCore.Qt.Key_Return:
            content = self.toPlainText()
            self.lastblock = content.replace(self.lastcontent, '')
            s = self.lastblock[len(self.prompt):].strip()
            t =  evalute(s)
            if t != '': self.append(t)
            self.lastcontent = self.toPlainText()
            self.append(self.prompt)
            self.counter = 0
        elif (event.key() == QtCore.Qt.Key_Up or
              event.key() == QtCore.Qt.Key_Down or
              event.key() == QtCore.Qt.Key_Left or
              event.key() == QtCore.Qt.Key_Right):
            event.ignore()

        else:
            QtGui.QTextEdit.keyPressEvent(self, event)
            self.counter += 1
            print self.counter
       
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