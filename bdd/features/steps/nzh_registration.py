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
    homepage.register_txtlnk.is_currently_displayed()
    homepage.open_register_form()

@when("I fill the registration form")
def i_fill_the_registration_form(context):
    """
    :type context: behave.runner.Context
    """
    homepage = HomePage(context.app)
    context.user = RandomUser()
    # context.user.FIRSTNAME ="test123"
    # context.user.LASTNAME ="test123"
    # context.user.EMAIL = "qwi878979290121@qwer.com"
    # context.user.PASSWORD = "Q1w2e3r4t5"
    # context.user.BIRTHYEAR = "1982"
    # context.user.POSTCODE = "0612"
    # context.user.GENDER = "M"
    context.user.create_user()
    homepage.registration_form_page.fill_form(context.user)


@step("I click the register button")
def i_click_the_register_button(context):
    """
    :type context: behave.runner.Context
    """
    homepage = HomePage(context.app)
    homepage.registration_form_page.submit_register_form()


@then("I should be registered successfully")
def i_should_be_registered_successfully(context):
    """
    :type context: behave.runner.Context
    """
    homepage = HomePage(context.app)
    assert homepage.registration_form_page.last_page_form.will_be_displayed(time=20) is True
    homepage.registration_form_page.form_cancel_button.click()


@step("I should see the username on the homepage")
def i_should_see_the_username_on_the_homepage(context):
    """
    :type context: behave.runner.Context
    """
    homepage = HomePage(context.app)
    assert homepage.profile_lnk.will_be_displayed() is True


@when("I fill register form and submit")
def i_fill_register_form_and_submit(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(u"""
        given I open the registration form
        when I fill the registration form
        and I click the register button
    """)