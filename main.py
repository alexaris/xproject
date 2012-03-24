#!/usr/bin/env python
# -*- coding: utf-8 -*

"""An atempt to write a line-oriented tool program for IL2Sturmovik.

"""

import sys
from PySide import QtGui  
from PySide import QtCore
import console


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()
        
    def init_ui(self):
        self.textEdit = console.Console(self)
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