# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Image(Component):
    def __init__(self, driver, by_locator):
        super(Image, self).__init__(driver, by_locator)

    def get_src(self):
        pass

    def get_filename(self):
        pass

    def is_image_loaded(self):
        pass

    def get_title(self):
        pass

    def get_width(self):
        pass

    def get_height(self):
        pass
