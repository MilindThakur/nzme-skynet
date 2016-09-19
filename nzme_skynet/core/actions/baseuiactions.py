# coding=utf-8
from nzme_skynet.core.actions.controls.button import Button
from nzme_skynet.core.actions.controls.checkbox import Checkbox
from nzme_skynet.core.actions.controls.elem import Elem
from nzme_skynet.core.actions.controls.image import Image
from nzme_skynet.core.actions.controls.radiobutton import RadioButton
from nzme_skynet.core.actions.controls.select import SelectElem
from nzme_skynet.core.actions.controls.table import Table
from nzme_skynet.core.actions.controls.textinput import TextInput
from nzme_skynet.core.actions.controls.textlink import TextLink


class BaseUIActions(object):
    def __init__(self, driver):
        self.driver = driver

    def button(self, by_locator):
        return Button(self.driver, by_locator)

    def checkbox(self, by_locator):
        return Checkbox(self.driver, by_locator)

    def element(self, by_locator):
        return Elem(self.driver, by_locator)

    def webelement(self, webelement):
        return Elem(self.driver, webelement)

    def image(self, by_locator):
        return Image(self.driver, by_locator)

    def textlink(self, by_locator):
        return TextLink(self.driver, by_locator)

    def radiobutton(self, by_locator):
        return RadioButton(self.driver, by_locator)

    def selectlist(self, by_locator):
        return SelectElem(self.driver, by_locator)

    def table(self, by_locator):
        return Table(self.driver, by_locator)

    def textinput(self, by_locator):
        return TextInput(self.driver, by_locator)
