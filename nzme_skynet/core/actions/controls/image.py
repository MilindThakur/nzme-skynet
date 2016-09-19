# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Image(Component):
    def __init__(self, driver, by_locator):
        super(Image, self).__init__(driver, by_locator)

    def get_src(self):
        return self.get_attribute("src")

    def get_filename(self):
        raise NotImplementedError

    def is_image_loaded(self):
        return self.driver.execute_script("return arguments[0].complete && "
                                          "typeof arguments[0].naturalWidth != \"undefined\" && "
                                          "arguments[0].naturalWidth > 0", self.get_webelement())

    def get_title(self):
        return self.get_attribute("title")

    def get_width(self):
        return self.get_attribute("width")

    def get_height(self):
        return self.get_attribute("height")
