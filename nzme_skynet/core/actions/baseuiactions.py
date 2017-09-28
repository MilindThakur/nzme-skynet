# coding=utf-8
from nzme_skynet.core.actions.controls.button import Button
from nzme_skynet.core.actions.controls.checkbox import Checkbox
from nzme_skynet.core.actions.controls.elem import Elem
from nzme_skynet.core.actions.controls.image import Image
from nzme_skynet.core.actions.controls.radiobutton import RadioButton
from nzme_skynet.core.actions.controls.select import SelectElem
from nzme_skynet.core.actions.controls.table import Table
from nzme_skynet.core.actions.controls.text import Text
from nzme_skynet.core.actions.controls.textinput import TextInput
from nzme_skynet.core.actions.controls.textlink import TextLink


class BaseUIActions(object):
    def __init__(self, driver):
        self.__driver = driver

    def button(self, by, locator):
        return Button(self.__driver, locator, by)

    def checkbox(self, by, locator):
        return Checkbox(self.__driver, locator, by)

    def element(self, by, locator):
        return Elem(self.__driver, locator, by)

    def image(self, by, locator):
        return Image(self.__driver, locator, by)

    def textlink(self, by, locator):
        return TextLink(self.__driver, locator, by)

    def radiobutton(self, by, locator):
        return RadioButton(self.__driver, locator, by)

    def selectlist(self, by, locator):
        return SelectElem(self.__driver, locator, by)

    def table(self, by, locator):
        return Table(self.__driver, locator, by)

    def textinput(self, by, locator):
        return TextInput(self.__driver, locator, by)

    def text(self, by, locator):
        return Text(self.__driver, locator, by)
