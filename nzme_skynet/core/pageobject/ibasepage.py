# -*- coding: utf-8 -*-
from abc import abstractproperty


class IBasePage(object):

    @abstractproperty
    def locate(self):
        pass
