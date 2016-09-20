# coding=utf-8
from nzme_skynet.core.actions.baseuiactions import BaseUIActions


class UIActionsMob(BaseUIActions):
    def __init__(self, driver):
        super(UIActionsMob, self).__init__(driver)

    def button(self, by_locator):
        super(UIActionsMob, self).button(by_locator)

    def checkbox(self, by_locator):
        super(UIActionsMob, self).checkbox(by_locator)

    def element(self, by_locator):
        super(UIActionsMob, self).element(by_locator)

    def webelement(self, webelement):
        super(UIActionsMob, self).webelement(webelement)

    def image(self, by_locator):
        super(UIActionsMob, self).image(by_locator)

    def textlink(self, by_locator):
        super(UIActionsMob, self).textlink(by_locator)

    def radiobutton(self, by_locator):
        super(UIActionsMob, self).radiobutton(by_locator)

    def selectlist(self, by_locator):
        super(UIActionsMob, self).selectlist(by_locator)

    def table(self, by_locator):
        super(UIActionsMob, self).table(by_locator)

    def textinput(self, by_locator):
        super(UIActionsMob, self).textinput(by_locator)
