# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Image(Component):
    def __init__(self, by_locator):
        super(Image, self).__init__(by_locator)

    def getSrc(self):
        pass

    def getFileName(self):
        pass

    def isImageLoaded(self):
        pass

    def getTitle(self):
        pass

    def getWidth(self):
        pass

    def getHeight(self):
        pass
