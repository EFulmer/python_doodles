import sys

from PySide import QtGui


# The superclass is new. QMainWindows are main program windows.
class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # the status bar is the bar at the lower edge of the window 
        # (think the list of tabs that also has the time in tmux)
        # statusBar() returns an object representing it (or creates
        # one for this window, on first call) 
        # and showMessage sets its text to thegiven arg:
        self.statusBar().showMessage('Ready')
        # ho hum, nothing new:
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
