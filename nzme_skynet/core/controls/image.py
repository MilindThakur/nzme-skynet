# coding=utf-8
import time

from nzme_skynet.core.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts


class Image(Clickable):

    @property
    def src(self):
        self._highlight()
        return self.get_attribute("src")

    def get_filename(self):
        raise NotImplementedError

    def is_image_loaded(self):
        return self.driver.execute_script("return arguments[0].complete && "
                                          "typeof arguments[0].naturalWidth != \"undefined\" && "
                                          "arguments[0].naturalWidth > 0", self._find_element())

    def _wait_for_lazy_loaded_image(self, timeout=DefaultTimeouts.DEFAULT_TIMEOUT):
        start_ms = time.time() * 1000.0
        stop_ms = start_ms + (timeout * 1000.0)
        for x in range(int(timeout * 10)):
            if self.get_attribute('data-original') == self.get_attribute('src'):
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
            return self.will_be_visible()

    @property
    def title(self):
        return self.get_attribute("title")

    @property
    def width(self):
        return self.get_attribute("width")

    @property
    def height(self):
        return self.get_attribute("height")
