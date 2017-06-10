import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMouseEvent, QKeyEvent
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit, QSizePolicy, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal


class FixedEdit(QTextEdit):
    editAccepted = pyqtSignal()
    editRejected = pyqtSignal()

    def __init__(self):
        super().__init__()
        # no scroll bars in this example
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # self.document().contentsChanged.connect(self.contentsChanged)
        #self.setMaximumWidth(600)

        # self.setLineWrapMode(QTextEdit.NoWrap)

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Return:
            self.editAccepted.emit()
            e.accept()
        elif e.key() == Qt.Key_Escape:
            self.editRejected.emit()
            e.accept()
        else:
            super().keyPressEvent(e)


class LabelEdit(QWidget):

    def __init__(self, text):
        super().__init__()
        self.label = QLabel(text)
        self.label.setStyleSheet("border: 1px solid red")
        self.label.setMaximumWidth(600)
        self.label.setWordWrap(True)

        self.editor = FixedEdit()
        self.editor.textChanged.connect(self.textChanged)
        self.editor.editAccepted.connect(self.editAccepted)
        self.editor.editRejected.connect(self.editRejected)

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.label, 0, 0)
        self.mainLayout.addWidget(self.editor, 0, 0)
        self.editor.hide()
        self.setLayout(self.mainLayout)



    def mouseDoubleClickEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            print("Double clicked.")

            self.showEditor()

    def editAccepted(self):
        print("Accepted")
        self.label.setText(self.editor.toPlainText())
        self.showLabel()

    def editRejected(self):
        print("Rejected")
        self.showLabel()

    def showEditor(self):
        self.editor.setText(self.label.text())
        br = self.label.fontMetrics().boundingRect(self.label.text())
        self.editor.setFixedSize(br.width()+30, br.height()+10)
        self.label.hide()
        self.editor.show()

    def showLabel(self):
        self.editor.hide()
        self.label.show()

    def textChanged(self):
        # print("textChanged")
        br = self.editor.fontMetrics().boundingRect(self.editor.toPlainText())
        print("br1:", br)
        print("self.editor.width():", self.editor.width())

        width = min(self.editor.width(), self.editor.maximumWidth())

        print("width:", width)

        if br.width() < width:
            br = self.editor.fontMetrics().boundingRect(0, 0, width, 10, Qt.TextWordWrap, self.editor.toPlainText())
            print("br2:", br)
            self.editor.setFixedSize(br.width(), br. height())


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    txt = LabelEdit("Hello world!")

    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(txt)
    vbox.addStretch()

    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addLayout(vbox)
    hbox.addStretch()

    w = QWidget()
    w.setLayout(hbox)
    w.show()

    sys.exit(app.exec_())