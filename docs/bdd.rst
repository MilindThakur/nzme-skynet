
.. meta::
    :description: Writing BDD style tests
    :keywords: selenium, bdd, gherkin, cucumber, webdriver

+++++++++++++++++++++++
Writing BDD style tests
+++++++++++++++++++++++

Skynet has some built-in features to help write BDD style automated tests. Steps to create tests are:

    1. Create a feature file
    2. Add static one-time environment control file *environment.py*
    3. Create step implementation
    4. Create page object file
    5. Run the test using *behave* CLI

A typical directory structure might look like::

    features/
    features/tutorial.feature
    features/environment.py
    features/steps/
    features/steps/tutorial.py
    pages/
    pages/googlepage.py


Feature File
============

Create a directory called *features* in the root directory of the project, this will host all the feature files.
Create a feature file within the directory with a *tutorial.feature* extension with following format.

.. code-block:: gherkin

 Feature: As a X I want Y So that Z

   Scenario: Should be able to search on google search
      Given I navigate to google search page
       When I search for term "NZME"
       Then I can see the url "www.nzme.co.nz/" in the result

The framework exposes certain built-in tags that can be used for test execution

    * **@api** Tagged scenarios will use the HTTP methods made available by the framework for testing APIs.
    * **@android-app** Tagged scenarios tagged allows testing an android app. This tag parses the section *ANDROID* within the config file *testconfig.ini*, available at the root of the project, for script startup.
    * **@ios-app** Tagged scenarios allows testing an ios app. This tag parses the section *IOS* within the config file *testconfig.ini*, available at the root of the project, for script startup.
    * **@android-browser**  Tagged scenarios allows testing android web apps. This tag parses the section *ANDROID* within the config file *testconfig.ini*, available at the root of the project, for script startup.
    * **@ios-browser** Tagged scenarios allows testing ios web apps. This tag parses the section *IOS* within the config file *testconfig.ini*, available at the root of the project, for script startup.
    * **@crossbrowser** TBD

.. note::

    The framework defaults to running UI tests on a browser, hence does not have any special tag for that.
    i.e. Any scenario *not* tagged is assumed to be a browser based test.

Please refer to `behave docs </https://behave.readthedocs.io/en/latest/tutorial.html>`_ for writing different styles of
scenarios.


Environment Control File
========================

In the *features* directory create an *environment.py* module that initialises the features
and scenarios before every run and then cleans up after. This module internally calls hooks implemented in the framework
for initialisation and cleanup.

.. code-block:: python

    from nzme_skynet.core.bdd import basetest

    def before_all(context):
        basetest.before_all(context)

    def after_all(context):
        basetest.after_all(context)

    def before_feature(context, feature):
        basetest.before_feature(context, feature)

    def after_feature(context, feature):
        basetest.after_feature(context, feature)

    def before_scenario(context, scenario):
        basetest.before_scenario(context, scenario)

    def after_scenario(context, scenario):
        basetest.after_scenario(context, scenario)

    def before_step(context, step):
        basetest.before_step(context, step)

    def after_step(context, step):
        basetest.after_step(context, step)

Step Implementation
===================

Create a new directory *features/steps*. In that directory create a step file *tutorial.py*.

.. code-block:: python

    from behave import *

    @given('I navigate to google search page')
    def step_impl(context):
        context.ghomepage = GoogleHomePage()
        context.ghomepage.goto(absolute=True)

    @when('I search for term "(?P<search_term>.+)"')
    def step_impl(context, search_term):
        context.ghomepage.search('nzme')

    @then('I can see the url "(?P<url>.+)" in the result')
    def step_impl(context, url):
        gresultpage = GoogleSearchResultPage()
        gresultpage.search_result_container.will_be_visible()
        first_result_url = gresultpage.get_result_url(1)
        assert url in first_result_url, "Unexpected {0} found in first result".format(first_result_url)



Page Object Pattern
===================

The framework encourage using well known Page Object pattern to model automation code. For the above scenario, create a
folder *pages* in the root of the project and create a page object file as following:

.. code-block:: python

    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys

    from nzme_skynet.core.controls.textinput import TextInput
    from nzme_skynet.core.controls.button import Button
    from nzme_skynet.core.controls.element import Element
    from nzme_skynet.core.driver.driverregistry import DriverRegistry
    from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
    from nzme_skynet.core.driver.enums.drivertypes import DriverTypes

    class GoogleHomePage(BaseWebPage):
        page_url = "https://www.google.co.nz/"
        search_input = TextInput(By.NAME, 'q')
        submit_search_btn = Button(By.NAME, 'btnK')

        def search(self, string):
            self.search_input.set_value(string)
            # To get around suggestions option hiding the search button
            ActionChains(DriverRegistry.get_webdriver()).send_keys(Keys.ESCAPE).perform()
            self.submit_search_btn.click()

    class GoogleSearchResultPage(BaseWebPage):
        search_result_container = Element(By.ID, 'rso')

        def get_result_url(self, index):
            return self.search_result_container.find_sub_elements(By.TAG_NAME, "cite")[index-1].text

Test Execution
==============

To execute the above feature locally (on chrome by default):

.. code-block:: bash

    behave feature/tutorial.feature -D local=true

To execute the above feature on firefox locally:

.. code-block:: bash

    behave feature/tutorial.feature -D local=true -D browserName=firefox

To execute the above feature on a selenium grid:

.. code-block:: bash

    behave feature/tutorial.feature -D local=false -D browserName=firefox -D selenium_grid_url=http://localhost:4444/wd/hub

To execute the above feature on Zalenium container grid:

.. code-block:: bash

    behave feature/tutorial.feature -D local=false -D browserName=firefox -D selenium_grid_url=http://localhost:4444/wd/hub -D zalenium=true


.. note::

    Please refer to :doc:`some tips </best_practice>` on writing better feature files, scenarios, step
    files, page objects, tagging etc.

