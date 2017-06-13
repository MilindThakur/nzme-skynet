from nzme_skynet.core.browsers.web.remotebrowser import RemoteBrowser


class RemoteBrowserBuilder(object):
    def __init__(self, sel_grid_url, desired_capabilities, base_url,):
        self.command_executor = sel_grid_url
        self.desired_capabilities = desired_capabilities
        self.base_url = base_url

    def build(self):
        browser = self._construct_remote_browser()
        browser.init_browser()
        return browser

    def _construct_remote_browser(self):
        return RemoteBrowser(self.command_executor,  self.desired_capabilities, self.base_url,)
