# coding=utf-8
class UIActionsFactory(object):
    factories = {}

    @staticmethod
    def create_ui_action(action, driver):
        if action not in UIActionsFactory.factories:
            UIActionsFactory.factories[action] = eval(action + '.Factory()')
            return UIActionsFactory.factories[action].create(driver)
