# -*- coding: utf-8 -*-

"""
A global register to keep track of driver created by the Driver Factory.
Any feature that wants to get the driver can call get_driver() method.
Currently supports registration of only one driver at any time.
At a later state this may support multiple drivers and can even return
driver of particular type e.g. webdriver, apidriver, windowsdriver etc.
"""

_registered_driver = None


def register_driver(driver):
    global _registered_driver
    _registered_driver = driver


def get_driver():
    global _registered_driver
    return _registered_driver


def deregister_driver():
    global _registered_driver
    _registered_driver = None
