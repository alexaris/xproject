#!/usr/bin/env python
# -*- coding: utf-8 -*

"""An atempt to write a line-oriented tool program for IL2Sturmovik.

"""

import sys
from PySide import QtGui  
from PySide import QtCore
import console
import config

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.config_file = '.config' 
        self.config = config.read(self.config_file)
        self.init_ui()
        
    def init_ui(self):
        self.textEdit = console.Console(self)
        self.layout = QtGui.QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.textEdit)
        self.setWindowTitle('il2console')  
        self.setGeometry(self.config['left'], self.config['top'], 
                         self.config['width'], self.config['height'])

    def save_config(self):
        self.config['width'] = self.width()
        self.config['height'] = self.height()
        self.config['left'] = self.mapToGlobal(self.rect().topLeft()).x()
        self.config['top'] = self.mapToGlobal(self.rect().topLeft()).y()
        config.write(self.config_file, self.config)

    def closeEvent(self, event):
        self.save_config() # write settings
        event.accept()
          
        
                
def main():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()