# coding=utf-8
from nzme_skynet.core.actions.controls.button import Button
from nzme_skynet.core.actions.controls.checkbox import Checkbox
from nzme_skynet.core.actions.controls.elem import Elem
from nzme_skynet.core.actions.controls.image import Image
from nzme_skynet.core.actions.controls.radiobutton import RadioButton
from nzme_skynet.core.actions.controls.select import Select
from nzme_skynet.core.actions.controls.table import Table
from nzme_skynet.core.actions.controls.textinput import TextInput
from nzme_skynet.core.actions.controls.textlink import TextLink


class BaseUIActions(object):
    def __init__(self, driver):
        self._driver = driver

    def button(self, by_locator):
        return Button(self._driver, by_locator)

    def checkbox(self, by_locator):
        return Checkbox(self._driver, by_locator)

    def element(self, by_locator):
        return Elem(self._driver, by_locator)

    def webelement(self, webelement):
        return Elem(self._driver, webelement)

    def image(self, by_locator):
        return Image(self._driver, by_locator)

    def textlink(self, by_locator):
        return TextLink(self._driver, by_locator)

    def radiobutton(self, by_locator):
        return RadioButton(self._driver, by_locator)

    def selectlist(self, by_locator):
        return Select(self._driver, by_locator)

    def table(self, by_locator):
        return Table(self._driver, by_locator)

    def textinput(self, by_locator):
        return TextInput(self._driver, by_locator)
