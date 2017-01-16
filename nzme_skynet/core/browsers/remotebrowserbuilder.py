from nzme_skynet.core.browsers.web.remotebrowser import RemoteBrowser


class RemoteBrowserBuilder(object):
    def __init__(self, desired_capabilities, base_url,):
        self.desired_capabilities = desired_capabilities
        self.base_url = base_url

    def build(self):
        browser = self._construct_remote_browser()
        browser.init_browser()
        return browser

    def _construct_remote_browser(self):
        return RemoteBrowser(self.base_url, self.desired_capabilities)
