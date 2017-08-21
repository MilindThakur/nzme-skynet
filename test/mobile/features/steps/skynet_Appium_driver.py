from behave import *
from test.mobile.pages.homepage import Homepage

use_step_matcher("re")


@given("I am on the test app home screen")
def I_am_on_the_test_app_home_screen(context):
    page = Homepage(context.app)
    assert page.home_message.get_text() == "HomeMessage", "The Home message was not as we expected. We expected HomeMessage, but the " \
                                         "app had: " + page.home_message.get_text()



@then("The home message is displayed")
def The_home_message_is_displayed(context):
    page = Homepage(context.app)
    assert page.home_message.get_text() == "HomeMessage", "The Home message was not as we expected. We expected HomeMessage, but the " \
                                         "app had: " + page.home_message.get_text()
