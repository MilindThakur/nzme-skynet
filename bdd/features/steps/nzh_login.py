from behave import *

use_step_matcher("re")


@given("I open the login form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I fill the login form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I click the login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I should be logged in to the NZH website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass