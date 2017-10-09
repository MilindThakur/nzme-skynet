# -*- coding: utf-8 -*-


class BrowserDriver(object):

    def create_driver(self):
        raise NotImplementedError

    def add_option(self, option):
        raise NotImplementedError

    def add_extension(self, extension):
        raise NotImplementedError

    @staticmethod
    def get_default_capability():
        raise NotImplementedError

    def set_proxy(self):
        # Implemented here
        pass
