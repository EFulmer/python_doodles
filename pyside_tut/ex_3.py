import sys
from PySide import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        # super(first, second) = treat second as an instance of 
        # first's superclass
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # assuming QFont gets a default sans-serif font, renders it in
        # 10pt size here:
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        # self-evident
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        # QPushButton args: label/text on button, parent object
        btn = QtGui.QPushButton('Button', self)
        # self-evident
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # resize is self-evident in its purpose:
        # sizeHint lets PySide do the thinking on how big the button
        # should be:
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # first 2 params: x-pos and y-pos on screen
        # second 2: height and width
        self.setGeometry(300, 300, 250, 150)
        # self-evident what setWindowTitle does
        self.setWindowTitle('Tooltips')
        # have to call show to actually display the window
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
