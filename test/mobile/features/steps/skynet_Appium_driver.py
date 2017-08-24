from behave import *
from selenium.webdriver.common.by import By

from test.mobile.pages.pageobject.mobile.homepage import HomePage

use_step_matcher("re")


@given("I am on the test app home screen")
def I_am_on_the_test_app_home_screen(context):
    assert HomePage(context.app).home_message.get_text() == "HomeMessage"


@when("I navigate to the dashboard")
def I_navigate_to_the_dashboard(context):
    HomePage(context.app).navigation_bar.bar.find_sub_elements(By.ID, "navigation_dashboard")[0].click()


@then("The (?P<message>.+) message is displayed")
def The_home_message_is_displayed(context, message):
    assert HomePage(context.app).home_message.get_text() == message

