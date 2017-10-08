# -*- coding: utf-8 -*-


class AppiumDriver(object):

    def create_driver(self):
        raise NotImplementedError

    def add_capability(self, name, value):
        raise NotImplementedError
