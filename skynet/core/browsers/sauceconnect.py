# coding=utf-8
import os

selenium_host = "ondemand.saucelabs.com"
selenium_port = "80"


def get_sauce_username():
    return os.environ['SAUCE_USERNAME']


def get_sauce_accesskey():
    return os.environ['SAUCE_ACCESS_KEY']


def construct_remote_commandexecutor():
    print get_sauce_username()
    return "http://%s:%s@%s:%s/wd/hub" % \
           (get_sauce_username(),
            get_sauce_accesskey(),
            selenium_host,
            selenium_port)
