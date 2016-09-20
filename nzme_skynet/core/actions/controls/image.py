# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.component import Component

class Image(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(Image, self).__init__(driver, locator, by)

    def get_src(self):
        return self.get_attr("src")

    def get_filename(self):
        raise NotImplementedError

    def is_image_loaded(self):
        return self.driver.execute_script("return arguments[0].complete && "
                                          "typeof arguments[0].naturalWidth != \"undefined\" && "
                                          "arguments[0].naturalWidth > 0", self.get_webelement())

    def get_title(self):
        return self.get_attr("title")

    def get_width(self):
        return self.get_attr("width")

    def get_height(self):
        return self.get_attr("height")
