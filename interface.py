#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys
import cv2
import re
import inspect
import see

path = './one.jpg'

listOfFunctions = sorted([i for i in cv2.__dir__() if inspect.isbuiltin(getattr(cv2, i))])
listOfConstants = ['cv2.' + x for x in dir(cv2) if type(getattr(cv2, x)) == int]

func = sorted([i for i in cv2.__dir__() if inspect.isbuiltin(getattr(cv2, i))])
arguments = re.compile(r'\w+\((.*?)\)')
w = {}
for i in func:
    args = arguments.search(getattr(cv2, i).__doc__).group(1)
    need, *dontneed = args.replace(' ', '').split('[,')
    need = need.split(',')
    dontneed = [x.replace(']', '') for x in dontneed]
    w.update({i: [need, dontneed]})


class FormBox(QWidget):
    """docstring for FormBox"""

    def __init__(self):
        super(FormBox, self).__init__()

        # self.setObjectName('FormBoxWidget')
        # self.setStyleSheet('QWidget#FormBoxWidget { background-color: #ffffff; color: #f8f8f8}')

        # self.listOfFunctions = sorted(
        #     [i for i in cv2.__dir__() if inspect.isbuiltin(getattr(cv2, i))])

        self.form = QFormLayout()

        self.funcName = QLineEdit()
        self.funcName.returnPressed.connect(self.addLineArgs)
        completer = QCompleter(listOfFunctions)
        completer.setCaseSensitivity(False)
        self.funcName.setCompleter(completer)
        self.funcName.setPlaceholderText('Function name')
        self.form.addRow(self.funcName)
        # self.form.addRow(QLabel('Name'), self.funcName)

        # f = QFormLayout()
        # f.addRow(QLabel('123'), QLineEdit())
        # f.addRow(QLabel('222'), QLineEdit())
        # self.form.addRow(QLabel('args'), f)
        # self.funcArgs = QLineEdit()
        # self.funcKwargs = QLineEdit()
        self.funcArgs = QFormLayout()
        self.funcArgs.addRow(QLineEdit())

        self.funcKwargs = QFormLayout()
        self.funcKwargs.addRow(QLineEdit())

        self.funcIndex = QLineEdit()

        self.form.addRow(QLabel('args'), self.funcArgs)
        self.form.addRow(QLabel('kwargs'), self.funcKwargs)
        self.form.addRow(QLabel('index'), self.funcIndex)

        a = QPushButton()
        a.clicked.connect(self.getKwargs)
        self.form.addRow(a)

        self.setLayout(self.form)

    def addLineArgs(self):
        # return
        print(self.getName())
        args = w[self.getName()]
        print(args)
        need = [x for x in args[0] if (x != 'src') and (x != 'image')]
        dontneed = [x for x in args[1] if x != 'dst']

        # print(self.form.itemAt(1).widget())
        # print(self.form.itemAt(3).widget())
        # for i in range(self.form.count()):
        #     print(i, self.form.itemAt(i).widget())

        # self.form.takeAt(3) = QFormLayout()

        completer = QCompleter(listOfConstants)
        completer.setCaseSensitivity(False)
        for arg in need:
            a = QLineEdit()
            a.setCompleter(completer)
            # fa.addRow(QLabel(arg), a)
            self.funcArgs.addRow(QLabel(arg), a)

        for arg in dontneed:
            a = QLineEdit()
            a.setCompleter(completer)
            self.funcKwargs.addRow(QLabel(arg), a)

    def getName(self):
        return self.funcName.text()

    def getArgs(self):
        # return self.funcArgs.text()
        a = []
        for i in range(self.funcArgs.count()):
            if type(self.funcArgs.itemAt(i).widget()) == QLineEdit:
                if self.funcArgs.itemAt(i).widget().text() == '':
                    continue
                a.append(self.funcArgs.itemAt(i).widget().text())
        return ';'.join(a)

    def getKwargs(self):
        # return self.funcKwargs.text()
        a = []
        # a.append(self.funcKwargs.itemAt(0).widget().text())
        b = self.funcKwargs.itemAt(0).widget().text()
        if b and b[-1] == ';':
            b = b[:-1]
        a.append(b)
        for i in range(1, self.funcKwargs.count()):
            print(self.funcKwargs.itemAt(i).widget())
            if type(self.funcKwargs.itemAt(i).widget()) == QLineEdit:
                if self.funcKwargs.itemAt(i).widget().text() == '':
                    continue
                b = self.funcKwargs.itemAt(i - 1).widget().text() + "=" + \
                    self.funcKwargs.itemAt(i).widget().text()
                a.append(b)
                # a.append(self.funcKwargs.itemAt(i).widget().text())
        print(a)
        return ';'.join(a)

    def getIndex(self):
        return self.funcIndex.text()

    def getParams(self):
        return self.getName(), self.getArgs(), self.getKwargs(), self.getIndex()

    def delete(self):
        self.deleteLater()
        # for item in reversed(range(self.form.count())):
        # print(self.layout().count())
        # while (self.layout().count()):
        #     item = self.layout().takeAt(0)
        #     widget = item.widget()
        #     if widget is not None:
        #         widget.deleteLater()
        # self.layout().removeItem(self.layout().takeAt(0))
        # for i in reversed(range(self.count())):
        #     # self.lay.takeAt(i).deleteLater()
        #     # self.lay.removeItem(self.lay.takeAt(i))
        #     for j in reversed(range(self.lay.itemAt(i).count())):
        #         # print(self.lay.itemAt(i).itemAt(j))
        #         self.lay.itemAt(i).takeAt(j).widget().deleteLater()
        #     self.lay.removeItem(self.lay.takeAt(i))


class MainWindow(QWidget):
    """docstring for MainWindow"""
    ''' QMainWindow '''

    def __init__(self):
        super(MainWindow, self).__init__()

        # self.listOfFunctions = sorted(
        #     [i for i in cv2.__dir__() if inspect.isbuiltin(getattr(cv2, i))])

        # self.w = QWidget()
        # self.w.resize(250, 150)
        # self.w.move(300, 300)
        # self.w.setWindowTitle('Simple')
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Simple')

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

        self.setLayout(self.l)

        self.show()

    def addL(self):
        # item = QFormLayout()

        # cbname = QComboBox()
        # cbname.setEditable(True)
        # cbname.addItems(self.listOfFunctions)

        # completer = QCompleter(self.listOfFunctions)
        # completer.setCaseSensitivity(False)

        # cbname.setCompleter(completer)
        # item.addRow(QLabel('Name'), cbname)
        # # item.addRow(QLabel('Name'), QLineEdit())
        # item.addRow(QLabel('args'), QLineEdit())
        # item.addRow(QLabel('kwargs'), QLineEdit())
        # item.addRow(QLabel('index'), QLineEdit())

        # w = QWidget()
        # w.setLayout(item)
        # frame = QFrame(w)
        # frame.setStyleSheet("background-color: rgb(255,0,0); margin:5px; border:1px solid rgb(0, 255, 0); ")
        # self.lay.addWidget(w)

        # self.lay.addLayout(item)
        self.lay.addWidget(FormBox())

    def resetL(self):
        # self.lay = QVBoxLayout()
        # self.l.insertLayout(self.l.count()-1, self.lay)
        # for i in reversed(range(self.lay.count())):
        #     print(self.lay.removeItem(self.lay.takeAt(i)))
        for i in reversed(range(self.lay.count())):
            # self.lay.takeAt(i).widget().delete()
            self.lay.takeAt(i).widget().deleteLater()
            # self.lay.takeAt(i).deleteLater()
            # self.lay.removeItem(self.lay.takeAt(i))
            # for j in reversed(range(self.lay.itemAt(i).count())):
            #     # print(self.lay.itemAt(i).itemAt(j))
            #     self.lay.itemAt(i).takeAt(j).widget().deleteLater()
            # self.lay.removeItem(self.lay.takeAt(i))

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
            item = self.lay.itemAt(i).widget()
            params = item.getParams()
            # for j in range(self.lay.itemAt(i).count()):
            #     # print(j)
            #     # print(self.lay.itemAt(i).itemAt(j).widget().currentText())
            #     # print(type(self.lay.itemAt(i).itemAt(j).widget()) == QLineEdit)
            #     if type(self.lay.itemAt(i).itemAt(j).widget()) == QComboBox:
            #         params.append(self.lay.itemAt(
            #             i).itemAt(j).widget().currentText())
            #     if type(self.lay.itemAt(i).itemAt(j).widget()) == QLineEdit:
            #         # print(self.lay.itemAt(i).itemAt(j).widget().text(), len(params))
            #         params.append(self.lay.itemAt(i).itemAt(j).widget().text())
            print(params)
            name = params[0]
            args = list()
            if params[1]:
                args = [eval(x) for x in params[1].split(';')]
            kwargs = dict()
            if params[2]:
                kwargs = dict([(x.split('=')[0], eval(x.split('=')[1]))
                               for x in params[2].split(';')])
            indexOfOutput = int(params[3]) if params[3] else None
            # print(name, args, kwargs, indexOfOutput)
            c.addGeneric(name, *args, **kwargs, indexOfOutput=indexOfOutput)
        return c


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else './one.jpg'

    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
