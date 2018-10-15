# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver

"""
Interface for Driver APIs
"""

class BaseDriver(object):
    """
    Base Driver Interface
    """
    baseurl = None

    def quit(self):
        """
        Quit driver and browser window
        :return: None
        """
        self.webdriver.quit()

    def close(self):
        """
        Close browser
        :return: None
        """
        self.webdriver.close()

    @property
    def webdriver(self):
        # type: () -> WebDriver
        """
        Get Selenium webdriver API instance
        :return: Selenium WebDriver API
        """
        raise NotImplementedError

    @property
    def desired_capabilities(self):
        """
        Current driver desired capabilities
        :return: Desired capabilities dict
        """
        return self.webdriver.desired_capabilities()

    @property
    def name(self):
        """
        Driver name
        :return: Name string
        """
        return self.webdriver.name

    # Browser Specific Interfaces

    @property
    def window_handles(self):
        """
        Return all window handles from current session
        :return: window handles
        """
        raise NotImplementedError

    def switch_to_newest_window(self):
        raise NotImplementedError

    def switch_to_oldest_window(self):
        raise NotImplementedError

    @property
    def title(self):
        """
        Title of the current page
        :return: Title String
        """
        raise NotImplementedError

    @property
    def current_url(self):
        """
        Current page URL
        :return: URL String
        """
        raise NotImplementedError

    def goto_url(self, url, absolute):
        """
        Navigate to a URL
        When absolute=True, navigates to the url provided
        When absolute=False, uses baseurl to navigate to the relative url

        driver.goto_url("/relative")
        driver.goto_url("https://www.google.co.nz", absolute=True)

        :param url: (String) URL to nativate to
        :param absolute: boolean, default False
        """
        raise NotImplementedError

    @property
    def page_source(self):
        """
        Source of current page
        """
        return self.webdriver.page_source

    def maximize_window(self):
        """
        Maximise the current window
        """
        raise NotImplementedError

    def get_window_size(self):
        """
        Return the current window size
        :return: (Tuple) window size
        """
        raise NotImplementedError

    def set_window_size(self, width, height):
        """
        Set window size
        :param width: int
        :param height: int
        """
        raise NotImplementedError

    def back(self):
        """
        Navigate back to the last url
        """
        raise NotImplementedError

    def refresh(self):
        """
        Refresh the current url
        """
        raise NotImplementedError

    def forward(self):
        """
        Navigate to the next url from browser history
        """
        raise NotImplementedError

    def take_screenshot_current_window(self, filename):
        """
        Take screenshot of the current window
        :param filename: (String) filename to save the screenshot to
        """
        raise NotImplementedError

    def take_screenshot_full_page(self, filename):
        """
        Take full page screenshot
        :param filename: (String) filename to save the screenshot to
        """
        raise NotImplementedError

    def wait_for_javascript_return(self, script, return_value):
        """
        Wait until javascript returns a value
        :param script: Javascript to run
        :param return_value: return value to wait for
        """
        raise NotImplementedError

    def set_page_load_timeout(self, time):
        """
        Amount of time to wait for page load to finish before throwing an exception
        This is set across the entire session of the driver
        :param time: (int) time to wait
        """
        raise NotImplementedError

    def switch_to_alert(self, time):
        """
        Wait for alert and then switch to alert
        :param time: (int) time to wait for alert
        """
        raise NotImplementedError

    def switch_and_accept_alert(self, time):
        """
        Wait for alert, switch to alert and then click accept
        :param time: (int) time to wait for alert
        """
        raise NotImplementedError

    def switch_and_dismiss_alert(self, time):
        """
        Wait for alert, switch to alert and dismiss
        :param time: (int) time to wait for alert
        """
        raise NotImplementedError

    def wait_for_page_load(self, timeout, throw_on_timeout):
        raise NotImplementedError
