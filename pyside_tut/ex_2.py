#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PySide import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        # does all the hidden magic background stuff to set up a 
        # QWidget
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    # this'd fail if we didn't have a QApplication to link our 
    # QWidget (which is what an Example is!) to:
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
