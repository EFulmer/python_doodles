# Confirmation message box tutorial:
import sys
from PySide import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Confirmation Message Box')
        self.show()
    
    def closeEvent(self, event):
        # worth noting: this function is inherited from QWidget.
        # question is obviously a specific, predefined type of message
        # box
        # 
        # then you provide the title for the message box, the main
        # text contents, the answer buttons (which may be predefined; 
        # see Yes and No here, etc.) bitwise or'd, and the default 
        # option.
        reply = QtGui.QMessageBox.question(self, 'Message',
                'Are you sure you want to quit?', QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
