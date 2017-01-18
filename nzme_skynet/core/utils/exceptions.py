# coding=utf-8
"""
Lits of all Exceptions that may happen in the framework.
"""

class SkynetException(Exception):
    """
    Base exception class
    """

    def __init__(self, msg=None, stacktrace=None):
        self.msg=msg
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg

class TimeoutException(SkynetException):
    """
    Thrown when a command does not complete in enough time.
    """
    pass

class NoDockerContainerException(SkynetException):
    """
    Throw when Docker container is not initialised.

    On such exception check:
        - If the Selenium Docker container is running

          docker images | grep "elgalu/selenium" | wc -l
          docker images | grep "dosel/zalenium" | wc -l
          docker ps -a -f name=zalenium_ -q | wc -l
    """
