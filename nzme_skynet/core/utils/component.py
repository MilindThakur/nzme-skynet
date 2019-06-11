# -*- coding: utf-8 -*-
class Component(object):
    """
    Custom descriptor class to lazy load reusable components in a page object

    e.g.
    class HomePage(BaseWebPage):

        @Component
        def header(self):
            self._header = HeaderWidgetPO()

        @Component
        def footer(self):
            self._footer = FooterWidgetPO()

    class HeaderWidgetPO(object):

        action1 = Text(By.ID, "id")

    HomePage().header.action1.text
    """

    def __init__(self, func):
        self.loader = func
        self.secretAttr = '_' + func.__name__

    def __get__(self, obj, cls):
        try:
            return getattr(obj, self.secretAttr)
        except AttributeError:
            self.loader(obj)
            return getattr(obj, self.secretAttr)
