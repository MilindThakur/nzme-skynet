from behave import *
use_step_matcher("re")


@given("I am on the test app home screen")
def I_am_on_the_test_app_home_screen(context):
    """
    :type context: behave.runner.Context
    """
    a = context
    pass


@then("The home message is displayed")
def The_home_message_is_displayed(context):
    """
    :type context: behave.runner.Context
    """
    b = context
    pass