# coding=utf-8
from nzme_skynet.core.actions.baseuiactions import BaseUIActions


class UIActionsWeb(BaseUIActions):

    def __init__(self, driver):
        super(UIActionsWeb, self).__init__(driver)

    def button(self, by, locator):
        return super(UIActionsWeb, self).button(by, locator)

    def checkbox(self, by, locator):
        return super(UIActionsWeb, self).checkbox(by, locator)

    def element(self, by, locator):
        return super(UIActionsWeb, self).element(by, locator)

    def image(self, by, locator):
        return super(UIActionsWeb, self).image(by, locator)

    def textlink(self, by, locator):
        return super(UIActionsWeb, self).textlink(by, locator)

    def radiobutton(self, by, locator):
        return super(UIActionsWeb, self).radiobutton(by, locator)

    def selectlist(self, by, locator):
        return super(UIActionsWeb, self).selectlist(by, locator)

    def table(self, by, locator):
        return super(UIActionsWeb, self).table(by, locator)

    def textinput(self, by, locator):
        return super(UIActionsWeb, self).textinput(by, locator)

    def text(self, by, locator):
        return super(UIActionsWeb, self).text(by, locator)
