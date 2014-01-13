# Display a menubar
import sys

from PySide import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        # super(Example, self) = "treating self as an instance of
        # Example's first superclass..."
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # QAction = GUI related action? Yes, an interface to handle 
        # user actions.
        # 
        # '&ActionName' = sets A as a shortcut key for the 
        # 'ActionName' menu item, when the menu it's on is open
        # 
        # args = icon, name, callback (aka slot - what handles the 
        # action)
        # am I right in calling this a callback?
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        # pretty self-evident
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        # Connect the related action (triggered - user triggers/clicks 
        # button) to another function.
        exitAction.triggered.connect(self.close)

        # statusBar()/menuBar() refresh (or create, if they don't 
        # exist) the status/menu bars for the QMainWindow. They also 
        # return objects representing status/menu bars; QStatusBar or
        # QMenuBar.
        statusBar = self.statusBar()
        statusBar.showMessage('Menu Bar Demo')
        menuBar = self.menuBar()
        # addMenu is pretty self explanatory, too.
        fileMenu = menuBar.addMenu('&File')
        # and we add the menu option created above.
        fileMenu.addAction(exitAction)

        self.setWindowTitle('Menu Bar')
        self.setGeometry(400, 350, 150, 150)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
