#!/usr/bin/env python3

import cv2
import abc


class BaseSee(abc.ABC):
    """docstring for BaseSee"""

    def __init__(self):
        pass

    @abc.abstractmethod
    def see(self):
        pass

    @abc.abstractmethod
    def setParams(self):
        pass


class GenericSee(BaseSee):
    """docstring for GenericSee"""

    def __init__(self):
        super(GenericSee, self).__init__()
        self.indexOfOutput = None

    def see(self, image):
        image = getattr(cv2, self.func)(image, *self.args, **self.kargs)
        return image if self.indexOfOutput is None else image[self.indexOfOutput]

    def setParams(self, func, *args, indexOfOutput=None, **kargs):
        self.func = func
        self.args = args
        self.kargs = kargs
        if indexOfOutput is not None:
            self.indexOfOutput = indexOfOutput


class SeeColection():
    """docstring for SeeColection"""

    def __init__(self):
        self.collection = []

    def addGeneric(self, *args, **kargs):
        tmp = GenericSee()
        tmp.setParams(*args, **kargs)
        self.collection.append(tmp)

    def run(self, image):
        for i in self.collection:
            image = i.see(image)
        return image


if __name__ == '__main__':
    image = cv2.imread('one.jpg')
    # g = GenericSee()
    # g.setParams('cvtColor', cv2.COLOR_BGR2GRAY)
    # t = GenericSee()
    # t.setParams('threshold', 127, 255, cv2.THRESH_BINARY, indexOfOutput=1)
    # image = g.see(image)
    # image = t.see(image)

    # c = SeeColection()
    # c.collection.append(GenericSee())
    # c.collection[-1].setParams('cvtColor', cv2.COLOR_BGR2GRAY)
    # c.collection.append(GenericSee())
    # c.collection[-1].setParams('threshold', 127, 255, cv2.THRESH_BINARY, indexOfOutput=1)

    c = SeeColection()
    c.addGeneric('cvtColor', cv2.COLOR_BGR2GRAY)
    c.addGeneric('threshold', 127, 255, cv2.THRESH_BINARY, indexOfOutput=1)
    image2 = c.run(image)
    cv2.imshow('Image', image2)
    cv2.waitKey()

    c.collection[-1].setParams('threshold', 63, 255, cv2.THRESH_BINARY, indexOfOutput=1)
    image2 = c.run(image)
    cv2.imshow('Image', image2)
    cv2.waitKey()
