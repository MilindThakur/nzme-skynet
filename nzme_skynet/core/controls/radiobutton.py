# coding=utf-8
from nzme_skynet.core.controls.button import Button


class RadioButton(Button):
    """
    This class extends Button class and contains methods that help in performing actions specific to RadioButton

    :param by: type of locator
    :param locator: locator value
    """

    def __init__(self, by, locator):
        super(RadioButton, self).__init__(by, locator)

    def is_selected(self):
        """
        This method
        validates DOM for visibility of the element, highlights the same when present.
        Checks whether the element/ radiobutton is selected and returns 1 when the radio button is selected.
        Returns 0 when the radio button is not selected. Returns False when the element is not visible.

        :return: 1 or 0 or False
        """
        self._highlight()
        return self._find_element().is_selected()
