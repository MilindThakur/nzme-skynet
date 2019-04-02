# -*- coding: utf-8 -*-


class DriverTypes(object):

    FIREFOX = "firefox"
    CHROME = "chrome"
    IE = "ie"
    EDGE = "edge"
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
    DriverTypes.FIREFOX,
    DriverTypes.IE,
    DriverTypes.EDGE,
    DriverTypes.SAFARI
]

MOBILE_APP = [
    DriverTypes.IOS,
    DriverTypes.ANDROID
]