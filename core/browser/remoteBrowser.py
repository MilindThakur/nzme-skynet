from core.browser.browser import Browser
from core.browser.sauceconnect import constructRemoteCommandExecutor

class RemoteBrowser(Browser):

    def __init__(self, desired_cap):
        super(RemoteBrowser, self).__init__("remote", None, desired_cap)