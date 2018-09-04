# -*- coding: utf-8 -*-


class DriverTypes(object):

    FIREFOX = "firefox"
    FIREFOXHEADLESS = "firefoxheadless"
    CHROME = "chrome"
    CHROMEHEADLESS = "chromeheadless"
    PHANTOMJS = "phantomjs"
    IE = "internet explorer"
    EDGE = "MicrosoftEdge"
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
    DriverTypes.FIREFOXHEADLESS,
    DriverTypes.FIREFOX,
    DriverTypes.PHANTOMJS,
    DriverTypes.IE,
    DriverTypes.EDGE,
    DriverTypes.SAFARI
]

MOBILE_APP = [
    DriverTypes.IOS,
    DriverTypes.ANDROID
]