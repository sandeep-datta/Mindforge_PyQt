#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QHBoxLayout, QVBoxLayout, QSizePolicy, QScrollArea
from PyQt5.QtGui import QIcon

root_tree = ["Root node",
                [["Child Node1"],
                 ["Child Node2"]]]


class NodeWidget(QWidget):
    def __init__(self, node_tree):
        super(NodeWidget, self).__init__()
        self.initUi(node_tree)

    def initUi(self, node_tree):
        lblRoot = QLabel(node_tree[0])
        lblRoot.setStyleSheet("border: 1px solid green")
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        hbox = QHBoxLayout()
        hbox.addWidget(lblRoot)

        self.setLayout(hbox)
        self.setStyleSheet("border: 1px solid red")

        try:
            children = node_tree[1]
            vbox = QVBoxLayout()
            for child_tree in children:
                child = NodeWidget(child_tree)
                vbox.addWidget(child)
            hbox.addLayout(vbox)
        except IndexError:
            pass


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Mindforge')
        self.setWindowIcon(QIcon('icons/engineering.svg'))
        self.statusBar().showMessage('Ready')
        sa = QScrollArea()
        w = NodeWidget(root_tree)
        sa.setWidget(w)
        self.setCentralWidget(sa)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())