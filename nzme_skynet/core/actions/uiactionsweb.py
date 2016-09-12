# coding=utf-8
from nzme_skynet.core.actions.baseuiactions import BaseUIActions


class UIActionsWeb(BaseUIActions):

    def __init__(self, driver):
        super(UIActionsWeb, self).__init__(driver)

    def button(self, by_locator):
        super(UIActionsWeb, self).button(by_locator)

    def checkbox(self, by_locator):
        super(UIActionsWeb, self).checkbox(by_locator)

    def element(self, by_locator):
        super(UIActionsWeb, self).element(by_locator)

    def webelement(self, webelement):
        super(UIActionsWeb, self).webelement(webelement)

    def image(self, by_locator):
        super(UIActionsWeb, self).image(by_locator)

    def textlink(self, by_locator):
        super(UIActionsWeb, self).textlink(by_locator)

    def radiobutton(self, by_locator):
        super(UIActionsWeb, self).radiobutton(by_locator)

    def selectlist(self, by_locator):
        super(UIActionsWeb, self).selectlist(by_locator)

    def table(self, by_locator):
        super(UIActionsWeb, self).table(by_locator)

    def textinput(self, by_locator):
        super(UIActionsWeb, self).textinput(by_locator)

    class Factory(object):
        @staticmethod
        def create(driver): return UIActionsWeb(driver)
