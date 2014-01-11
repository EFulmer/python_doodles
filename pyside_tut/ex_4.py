# Tutorial 4: Quit Button

import sys
from PySide import QtGui
from PySide import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        # boring, nothing new:
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
       # we've seen all this before:
       quitBtn = QtGui.QPushButton('Quit', self)
       # gui_widget.type_of_action.connect = accepts a fn as argument
       # which dictates behavior on that action?
       # 
       # instance() returns an object representing the current 
       # QApplication? That we then get the quit method of, since we
       # want the application to quit once the quit button is clicked.
       quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
       # ho hum:
       quitBtn.setToolTip('This <b>QPushButton</b> quits the application.')
       quitBtn.resize(quitBtn.sizeHint())

       self.setGeometry(0, 0, 250, 300)
       self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
