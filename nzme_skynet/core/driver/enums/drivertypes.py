# -*- coding: utf-8 -*-


class DriverTypes(object):

    FIREFOX = "firefox"
    CHROME = "chrome"
    CHROMEHEADLESS = "chromeheadless"
    PHANTOMJS = "phantomjs"
    IE = "IE"
    SAFARI = "safari"
    ANDROID = "android"
    ANDROIDWEB = "androidweb"
    IOSWEB = "iosweb"
    IOS = "ios"


MOBILE_WEBBROWSER = [

    DriverTypes.ANDROIDWEB,
    DriverTypes.IOSWEB
]

DESKTOP_WEBBROWSER = [
    DriverTypes.CHROME,
    DriverTypes.CHROMEHEADLESS,
    DriverTypes.FIREFOX,
    DriverTypes.PHANTOMJS,
    DriverTypes.IE,
    DriverTypes.SAFARI
]

MOBILE_APP = [
    DriverTypes.IOS,
    DriverTypes.ANDROID
]