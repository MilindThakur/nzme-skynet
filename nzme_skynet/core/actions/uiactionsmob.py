# coding=utf-8
from nzme_skynet.core.actions.baseuiactions import BaseUIActions


class UIActionsMob(BaseUIActions):
    def __init__(self, driver):
        super(UIActionsMob, self).__init__(driver)

    def button(self, by, locator):
        return super(UIActionsMob, self).button(by, locator)

    def checkbox(self, by, locator):
        return super(UIActionsMob, self).checkbox(by, locator)

    def element(self, by, locator):
        return super(UIActionsMob, self).element(by, locator)

    def image(self, by, locator):
        return super(UIActionsMob, self).image(by, locator)

    def textlink(self, by, locator):
        return super(UIActionsMob, self).textlink(by, locator)

    def radiobutton(self, by, locator):
        return super(UIActionsMob, self).radiobutton(by, locator)

    def selectlist(self, by, locator):
        return super(UIActionsMob, self).selectlist(by, locator)

    def table(self, by, locator):
        return super(UIActionsMob, self).table(by, locator)

    def textinput(self, by, locator):
        return super(UIActionsMob, self).textinput(by, locator)
