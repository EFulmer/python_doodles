# Center a window on the screen.
import sys

from PySide import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Centered Window')
        self.show()

    def center(self):
        # describes geometry of parent object
        geom = self.frameGeometry()
        # QDesktopWidget describes info about user's desktop
        # tne availableGeometry() function returns info about its 
        # parent display's (desktop etc) geometry (size etc.)
        # center() returns the center of the desktop
        cent = QtGui.QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cent)
        # moving top-left corner of window here:
        self.move(geom.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
