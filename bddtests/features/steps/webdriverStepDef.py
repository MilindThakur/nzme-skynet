from behave import given, when, then


@given('I initialise webbrowser "{browser}"')
def I_initialise_browser(context, browser):
    """
    :type context: behave.runner.Context
    :type browserType: str
    """
    pass


@when('I navigate to url "{url}"')
def I_navigate_to_url(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    pass


@then("I can access the page")
def I_can_access_the_page(context):
    """
    :type context: behave.runner.Context
    """
    pass
