#!/usr/bin/python3

import sys
from typing import List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QHBoxLayout, QVBoxLayout, QSizePolicy, QScrollArea
from PyQt5.QtGui import QIcon, QPaintEvent, QPainter, QPen, QPainterPath, QPalette
from PyQt5.QtCore import Qt, QPoint, QRect

root_tree = ["Root node",
                [["Child Node1",
                    [["Child Node1.1"],
                     ["Child Node1.2"]]],
                 ["Child Node2"]]]


class NodeWidget(QWidget):

    def __init__(self, node_tree):
        super(NodeWidget, self).__init__()
        self.lblRoot = QLabel(node_tree[0])
        self.vboxChildren = QVBoxLayout()
        self.children: List[NodeWidget] = []
        self.linePen = QPen(Qt.gray, 2)
        self.debugPen = QPen(Qt.red, 1)
        self.initUi(node_tree)

    def initUi(self, node_tree):
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        #self.lblRoot.setStyleSheet("border: 1px solid green")

        vbox1 = QVBoxLayout()
        vbox1.addStretch()
        vbox1.addWidget(self.lblRoot)
        vbox1.addStretch()

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)

        self.setLayout(hbox)
        #self.setStyleSheet("border: 1px solid red")

        try:
            children = node_tree[1]
            for child_tree in children:
                child = NodeWidget(child_tree)
                self.vboxChildren.addWidget(child)
                self.children.append(child)
            hbox.addLayout(self.vboxChildren)
        except IndexError:
            pass

    def paintEvent(self, event: QPaintEvent):
        with QPainter(self) as painter:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setPen(self.linePen)

            rect = self.lblRoot.geometry().translated(0, 2)

            # Draw the underline
            width = self.lblRoot.fontMetrics().boundingRect(self.lblRoot.text()).width()

            p = rect.bottomLeft()
            p += QPoint(width, 0)

            painter.drawLine(rect.bottomLeft(), p)

            # Draw Bezier curves to the child nodes
            for child in self.children:
                childBottomLeft : QPoint = child.mapToParent(child.lblRoot.geometry().bottomLeft())
                childBottomLeft += QPoint(0, 2)

                cpX = rect.right() + int((childBottomLeft.x() - rect.right()) / 2)

                start = QPoint(rect.bottomRight())

                cp1 = QPoint(cpX, rect.bottom())
                cp2 = QPoint(cpX, childBottomLeft.y())
                end = QPoint(childBottomLeft)

                path = QPainterPath()
                path.moveTo(start)
                path.cubicTo(cp1, cp2, end)
                painter.drawPath(path)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Mindforge')
        self.setWindowIcon(QIcon('icons/engineering.svg'))
        self.setBackgroundColor(Qt.white)
        self.statusBar().showMessage('New mindmap')

        nw = NodeWidget(root_tree)

        sa = QScrollArea()
        sa.setAlignment(Qt.AlignCenter)
        sa.setWidget(nw)

        self.setCentralWidget(sa)
        self.show()

    def setBackgroundColor(self, color):
        p = QPalette(self.palette())
        p.setColor(QPalette.Background, color)
        self.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())