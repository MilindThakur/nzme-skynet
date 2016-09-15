from nzme_skynet.core.browsers.web.remotebrowser import RemoteBrowser


class RemoteBrowserBuilder(object):
    def __init__(self, browser_type, base_url, capabilities):
        self.browser_type = browser_type
        self.base_url = base_url
        self.capabilities = capabilities

    def build(self):
        browser = self._construct_remote_browser()
        browser.init_browser()

    def _construct_remote_browser(self):
        return RemoteBrowser(self.base_url, self.capabilities)
