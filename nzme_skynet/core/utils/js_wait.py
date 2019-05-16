# coding=utf-8


class for_return(object):
    """An expectation for checking the javascript return.
    return_value is the expected return on javascript execution, which must be an exact match
    returns True if the return value matches, false otherwise."""

    def __init__(self, script, return_value):
        self.script = script
        self.return_value = return_value

    def __call__(self, driver):
        return True if driver.execute_scipt(self.script) == self.return_value else False
