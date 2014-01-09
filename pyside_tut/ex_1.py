#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PySide import QtGui


def main():
    app = QtGui.QApplication(sys.argv)

    wid = QtGui.QWidget()
    wid.resize(250, 150)
    wid.setWindowTitle('Simple')
    wid.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
