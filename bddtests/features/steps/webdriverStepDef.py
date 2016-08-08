# coding=utf-8
from behave import *


@given('I initialise webbrowser "{browsers}"')
def i_initialise_browser(context, browser):
    """
    :type context: behave.runner.Context
    :type browserType: str
    """
    pass


@when('I navigate to url "{url}"')
def i_navigate_to_url(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    pass


@then("I can access the page")
def i_can_access_the_page(context):
    """
    :type context: behave.runner.Context
    """
    pass
