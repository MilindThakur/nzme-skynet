# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.basedriver import BaseDriver


class MobileDriver(BaseDriver):

    def pinch_and_zoom(self):
        raise NotImplementedError

    def swipe(self):
        raise NotImplementedError

    def scroll(self):
        raise NotImplementedError
