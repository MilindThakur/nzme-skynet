from behave import *

from bdd.pages.homepage.homepage import HomePage
from nzme_skynet.core.utils.randomuser import RandomUser

use_step_matcher("re")

@given("I open the registration form")
def i_open_the_registration_from(context):
    """
    :type context: behave.runner.Context
    """
    homepage = HomePage(context.app)
    homepage.register_txtlnk.is_visible()
    homepage.open_register_form()

@when("I fill the registration form")
def i_fill_the_registration_form(context):
    """
    :type context: behave.runner.Context
    """
    homepage = HomePage(context.app)
    context.user = RandomUser()
    context.user.create_user()
    homepage.get_registration_form().fill_form(context.user)


@step("I click the register button")
def i_click_the_register_button(context):
    """
    :type context: behave.runner.Context
    """
    context.homepage.get_registration_form().submit_register_form()


@then("I should be registered successfully")
def i_should_be_registered_successfully(context):
    """
    :type context: behave.runner.Context
    """
    assert context.homepage.get_registration_form().last_page_form.will_be_displayed() is True
    context.homepage.get_registration_form().form_cancel_button.click()


@step("I should see the username on the homepage")
def i_should_see_the_username_on_the_homepage(context):
    """
    :type context: behave.runner.Contextx
    """
    assert context.homepage.profile_lnk.will_be_ready_to_interact() is True