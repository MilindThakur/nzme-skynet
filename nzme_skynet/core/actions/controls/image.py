# coding=utf-8
import time

from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.component import Component
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


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
                                          "arguments[0].naturalWidth > 0", self.find_element())

    def _wait_for_lazy_loaded_image(self, timeout=DefaultTimeouts.DEFAULT_TIMEOUT):
        start_ms = time.time() * 1000.0
        stop_ms = start_ms + (timeout * 1000.0)
        for x in range(int(timeout * 10)):
            if self.get_attr('data-original') == self.get_attr('src'):
                return True
            else:
                now_ms = time.time() * 1000.0
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        return False

    def wait_for_image_to_load(self, lazy_loading=False, timeout=DefaultTimeouts.DEFAULT_TIMEOUT):
        if lazy_loading:
            return self._wait_for_lazy_loaded_image(timeout)
        else:
            return self.will_be_displayed()

    def get_title(self):
        return self.get_attr("title")

    def get_width(self):
        return self.get_attr("width")

    def get_height(self):
        return self.get_attr("height")
