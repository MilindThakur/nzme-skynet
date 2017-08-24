from behave import *
from test.mobile.pages.pageobject.web.googlehomepage import GoogleHomePage

use_step_matcher("re")


@given("I have a device with chrome open")
def I_have__a_device_with_chrome_open(context):
    # Nothing happens here. the launching of chrome is part of the driver initialize
    pass


@when("I navigate to (?P<url>.+)")
def I_navigate_to_a_url(context, url):
    context.app.goto_url(url)


@then("The google homepage is displayed")
def The_google_homepage_is_displayed(context):
    assert GoogleHomePage(context.app).logo.is_currently_visible()
    assert GoogleHomePage(context.app).searchbox.is_currently_visible()
