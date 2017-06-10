from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QDialog):

    def __init__(self):
        super(Window, self).__init__()
        self.resize(600,400)

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        #self.mainLayout.setMargin(10)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.mainLayout.addWidget(self.scroll)

        scrollContents = QtWidgets.QWidget()
        self.scroll.setWidget(scrollContents)

        self.textLayout = QtWidgets.QVBoxLayout(scrollContents)
        #self.textLayout.setMargin(10)

        for _ in range(5):
            text = GrowingTextEdit()
            text.setMinimumHeight(50)
            self.textLayout.addWidget(text)


class GrowingTextEdit(QtWidgets.QTextEdit):

    def __init__(self, *args, **kwargs):
        super(GrowingTextEdit, self).__init__(*args, **kwargs)
        self.document().contentsChanged.connect(self.sizeChange)

        self.heightMin = 0
        self.heightMax = 65000

    def sizeChange(self):
        docHeight = int(self.document().size().height())
        if self.heightMin <= docHeight <= self.heightMax:
            self.setMinimumHeight(docHeight)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec_())