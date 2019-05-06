#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys
import cv2
import see

path = './one.jpg'

class MainWindow(QMainWindow):
    """docstring for MainWindow"""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.w = QWidget()
        self.w.resize(250, 150)
        self.w.move(300, 300)
        self.w.setWindowTitle('Simple')

        self.l = QVBoxLayout()
        self.l.addWidget(QLabel('Hello world!'))

        button = QPushButton('Add')
        button.clicked.connect(self.addL)
        self.l.addWidget(button)

        button = QPushButton('Reset')
        button.clicked.connect(self.resetL)
        self.l.addWidget(button)

        button = QPushButton('Show')
        button.clicked.connect(self.showL)
        self.l.addWidget(button)

        self.lay = QVBoxLayout()

        self.l.addLayout(self.lay)

        self.w.setLayout(self.l)

        self.w.show()

    def addL(self):
        item = QFormLayout()
        item.addRow(QLabel('Name'), QLineEdit())
        item.addRow(QLabel('args'), QLineEdit())
        item.addRow(QLabel('kwargs'), QLineEdit())
        item.addRow(QLabel('index'), QLineEdit())

        self.lay.addLayout(item)

    def resetL(self):
        # self.lay = QVBoxLayout()
        # self.l.insertLayout(self.l.count()-1, self.lay)
        # for i in reversed(range(self.lay.count())):
        #     print(self.lay.removeItem(self.lay.takeAt(i)))
        for i in reversed(range(self.lay.count())):
            # self.lay.takeAt(i).deleteLater()
            # self.lay.removeItem(self.lay.takeAt(i))
            for j in reversed(range(self.lay.itemAt(i).count())):
                # print(self.lay.itemAt(i).itemAt(j))
                self.lay.itemAt(i).takeAt(j).widget().deleteLater()
            self.lay.removeItem(self.lay.takeAt(i))

    def showL(self):
        # path = '/home/dave/Sync/cvsee/one.jpg'
        image = cv2.imread(path)
        c = self.createTransform()
        # print(c.collection)
        image = c.run(image)
        cv2.imshow('Image', image)
        cv2.waitKey()

    def createTransform(self):
        c = see.SeeColection()
        for i in range(self.lay.count()):
            # print('#', i)
            params = []
            for j in range(self.lay.itemAt(i).count()):
                # print(j)
                # print(self.lay.itemAt(i).itemAt(j).widget().text())
                # print(type(self.lay.itemAt(i).itemAt(j).widget()) == QLineEdit)
                if type(self.lay.itemAt(i).itemAt(j).widget()) == QLineEdit:
                    # print(self.lay.itemAt(i).itemAt(j).widget().text(), len(params))
                    params.append(self.lay.itemAt(i).itemAt(j).widget().text())
            # print(params)
            name = params[0]
            args = list()
            if params[1]:
                args = [eval(x) for x in params[1].split(';')]
            kwargs = dict()
            if params[2]:
                kwargs = dict([(x.split('=')[0], eval(x.split('=')[1])) for x in params[2].split(';')])
            indexOfOutput = int(params[3]) if params[3] else None
            # print(name, args, kwargs, indexOfOutput)
            c.addGeneric(name, *args, **kwargs, indexOfOutput=indexOfOutput)
        return c


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else './one.jpg'

    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
