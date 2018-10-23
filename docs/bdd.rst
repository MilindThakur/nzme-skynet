
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

Feature File
============

Create a directory called *features* in the root directory of the project, this will host all the feature files.
Create a feature file within the directory with a *tutorial.feature* extension with following format.

.. code-block:: gherkin

 Feature: As a X I want Y So that Z

   Scenario: Should be able to search on google search
      Given I navigate to google search page
       When I search for term "NZME"
       Then I can see the url "https://www.nzme.co.nz" in the result

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

Create a new directory *features/steps*. In that directory create an *environment.py* module that initialises the features
and scenarios before every run and then cleans up after.



Step Implementation
===================

Create a new directory *features/steps*. In that directory create a step file *tutorial.py*.

.. code-block:: python

    from behave import *

    @given('I navigate to google search page')
    def step_impl(context):
        pass

    @when('we implement a test')
    def step_impl(context):
        assert True is not False

    @then('behave will test it for us!')
    def step_impl(context):
        assert context.failed is False