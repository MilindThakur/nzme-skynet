
.. meta::
    :description: Best Practices for writing and managing tests
    :keywords: selenium, bdd, gherkin, cucumber, webdriver, best practice, automated tests

++++++++++++++++++++++++++++++++++++++++++++++++
Best practices for writing and maintaining tests
++++++++++++++++++++++++++++++++++++++++++++++++

While there are many different ways of writing and managing tests, following are some of my experiences in writing
better test scenarios.


Writing Scenarios
=================

Following are recommended steps when creating a feature file:

1. Create a feature file
    * Identify which feature file (if existing) will the scenarios for a user story belong to and then add more scenarios to the feature file.
    * If none, create a new feature file.
    * **Avoid**: Creating feature file per user story e.g. *US_606_login_error.feature*.
2. Always add feature description at the top of the feature file:
    As a <user> I want <task> So that <advantage>
3. Write all possible scenario headlines first. Note: Do not write *GWT* statements yet.
    * The idea is to flesh out all the user scenarios before getting to defining them further.
    * Use *Should be able to* statements e.g. "*Should be able to successfully subscribe to any newsletter*".
4. Tag the scenarios with appropriate tags
    * e.g. @p1, @p2, @p3, @smoke, @e2e, @crossbrowser, @android-app etc.
5. Identify scenarios that will remain as manual and tag them as @manual. For the rest of the scenarios
(which will be automated), tag them as @wip.
    * @wip tag avoids running the *in-progress* scenarios as part of build pipeline.
6. Pick @p1 scenarios first and start defining the *GWT* statements. Subsequently move to defining @p2 and @p3 scenarios.
    * It is very likely that while defining *GWT* statements you may come up with more scenarios. List them, tag them and expand on them later.
7. When all scenarios in a feature file have been defined well, create a pull request for the team members
(dev, qa, ba, ux etc) to review.
    * The aim is for the entire team to be on the same page in terms of scenarios that the application/feature is expected to support.
8. While the review is in process, pick @p1 scenarios and start writing the supporting code for execution.
9. When the scenario is executable, remove the @wip tag and move on to the next @p1 scenario.
10. When all @p1 scenarios are done, move on to @p2 scenarios.
    * Depending on the team's *Definition of Done*, you may or may not necessarily decide to automate @p2 or @p3 scenarios.

**Tips**

* Feel free to add any comments to the scenarios e.g. any special mention from the user story
* **No leaky scenarios**. Each scenario is independent and has no dependency on any other scenario in terms of data or execution. Every scenario should be able to run independently when run in parallel.
* Write **Declarative** scenarios than *Imperative* scenarios

.. code-block:: gherkin

    # Imperative: Boring, brittle tests, rigid step names (hard to reuse)
    Scenario: Redirect user to originally requested page after logging in
        Given a User "dave" exists with password "secret"
        And I am not logged in
        When I navigate to the home page
        Then I am redirected to the login form
        When I fill in "Username" with "dave"
        And I fill in "Password" with "secret"
        And I press "Login"
        Then I should be on the home page

.. code-block:: gherkin

    # Declarative: Easy to read, re-usable (desktop, mobile)
    Scenario: Redirect user to originally requested page after logging in
        Given I am an unauthenticated User
        When I attempt to view some restricted content
        Then I am shown a login form
        When I authenticate with valid credentials
        Then I should be shown the restricted content
* Scenarios should be user focussed. Preferably a user workflow.
* Avoid automating scenarios for navigation e.g. click link and assert navigation to a page
    * It is time consuming with less changes of regression unless the href links are changed.
    * Rather use an easy to use a simple unit test framework (e.g. unittest) for automation, its fast and less code.
* User explicit step names
    * e.g. *And I click next* should be "*And I click next on registration page*"
* Avoid changing step names/string once coded. Some other steps may be re-using them. Instead add aliases.

.. code-block:: python

    @step("I login")
    @step("I enter my email and password and click login")

* Move common steps across all scenarios in a feature file to a background scenarios e.g. any special setup.
    * Note: Background scenario is executed for very scenario in a feature file. So use wisely.
* All messages e.g. error/success should be explicitly checked as string parameters to the step.
* All test data should be randomised. Unless the test data is available  as a restorable snapshot or is setup previous to running tests.
* Re-use steps wherever possible.

.. code-block:: python

    @step("I login")
    def step_impl(context):
        context.execute_steps(u"""
            given I enter username and password
            and I click login
        """)

Tagging
=======

While behave allows developer to create any custom tags as a mechanism to manage scnearios as suites, following are some
of the tags that I have been using to manage scenarios/features.

============= ==========================================================================================
Tag           Fixture-Cleanup Point
============= ==========================================================================================
@p1           Absolute necessary tests, < 4-5 mins to run (from entire collection), last mile tests.
@p2           Part of regression tests, overnight tests.
@p3           Not necessary automated, page/form validations, cosmetic checks, error msgs, click navigation. Last priority to automate.
@manual       Only manual tests.
@smoke        @p1 and some @p2 tests. Post-production or pre-deployment tests.
@crossbrowser Potential cross browser tests e.g. all @p1 tests.Each team maintains a list of browsers/version/os that constitutes crossbrowser.
@api          Absolutely necessary for api tests. Skynet by default assumes browser based tests. Skynet currently does not support api and browser test in the same scenario.
@featurename  Named tags to be used at feature level.
============= ===========================================================================================

**Tips**

* Configure build runs based on tags and *not* feature files. e.g. build for regression tests will include all @p1 and @p2 tests.
* Tag scenarios appropriately before writing test code. Tag all scenarios as @wip and remove the tag as and when automated.
* Tag scenario outlines as @p2. Remember its tests * examples, adds time to total execution runs.
* To list all scenarios matching tag/s:

.. code-block:: bash

    $ behave --dry-run --no-snippets --no-summary --no-source --tags=@p1 -o filename.txt


Writing Step Definitions
========================

**Tips**

* One step definition file per feature file. *Behave* figures out where the step is as long as all the feature files are present in the "*features*" folder.
* *Avoid* including any conditional logic in step definitions. The code in the step def should be declarative and easy to read.
    * *Avoid* ifs, fors conditional loops
    * Not more than 3-4 lines
    * The logic should reside in the page object
* Always use error string in the assert statements. It is easy to debug failures.

.. code-block:: python

    assert context.profilepage.dob.is_displayed(), "Error: DOB is not visible"
    assert context.profilepage.page_url in context.driver.current_url,  "Error: expected {0}, found {1}".format(context.profilepage.page_url, context.driver.current_url)

* Always check if the page has loaded when moving between pages. Use one/few anchor elements to confirm page load

.. code-block:: python

    context.newsletterpage = NewsLetterPage()
    context.newsletterpage.next.click()
    context.mydetailspage = MyDetailsPage()
    context.driver.wait_for_url_to_contain(MyDetailsPage().page_url)
    context.mydetailspage.firstname.will_be_visible()

* Avoid using time.sleep() anywhere in the code. Instead use explicit waits

.. code-block:: python

    context.page.element_1.will_be_visible()
    context.page.element_2.will_be_ready_to_interact()
    context.driver.wait_for_url_to_contains(url)

* Move page interaction/actions away from step defs to page objects.

.. code-block:: python

    # Avoid interactions in step defs
    context.newsletter.morning_headlines.click()
    context.newsletter.sports_headline.click()
    context.newsletter.business_news.click()

    # Instead manage them in page objects. Step defs are lot cleaner and easy to read
    context.newsletter.select_all_newspapers()
    context.newsletter.select_newspaper("Morning Headlines")
    context.newsletter.select_newspaper(newspaper.morning_headline)

* *Avoid* using absolute goto urls in step defs (unless really required). Instead use *page.page_url* defined in the page object.

.. code-block:: python

    # Avoid using url strings
    assert "/my-account/register/newsletters-setup/" in context.driver.current_url

    # Use page urls from page object
    assert context.newsletter_setup_page.page_url in context.driver.current_url

* *Avoid* using asserts in *Given* and *When* steps.
    * Asserts (test assertions) should always be used only in *Then* steps (unless steps are being re-used).
    * *Avoid* any assertions in page objects.
* When passing a lot of information to the page object action method, construct an object from arguments first and then pass the object.

.. code-block:: python

    # Do not pass many arguments to the method
    context.register.fill_form(firstname, lastname, dob, gender, city, country)

    # Create an object and then pass the object
    from nzme_skynet.core.utils.randomuser import RandomUser
    context.user = RandomUser()
    context.register.fill_form(context.user)

* *Behave* provides access to object "*context*" to which one can pass other objects/variables that require access between steps.

.. code-block:: python

    @step("I create a user")
    def step_impl(context):
        context.user = RandomUser()

    @step("I login")
    def step_impl(context):
        Login().login(context.user)


Writing Page Objects
====================

Page object pattern is a very classic way of writing maintainable test code. The aim is to create an object model of a page
with its own set of elements and actionable methods.

**Tips**

* One unique class for every page
    * Derives from *BasePage* available in the framework
    * Has locators as class attributes
    * Has actions/interactions on the page modelled as methods
    * Has relative page url, unique to the page, as class attribute *page_url*.
    * Has reusable page objects called *components* e.g. page header, footer, ad-unit etc

.. code-block:: python

    class NewsletterSignupPage(BasePage):

        page_url = '/signup/'

        firstname = TextInput(By.ID, 'first_name')
        lastname = TextInput(By.ID, 'last_name')
        email = TextInput(By.ID, 'email_address')
        signupbutton = Button(By.ID, 'signup')

        @Component
        def header_widget(self):
            self._header = HeaderWidget()

        def signup(self, firstname='TEST', lastname='TESTING', email='test@testing.com'):
            self.firstname.set_value(firstname)
            self.lastname.set_value(lastname)
            self.email.set_value(email)
            self.signupbutton.click()

* The folder structure to use

.. code-block:: bash

    pages/
    pages/newbasepage.py # Possible new base page for website derived from *BasePage*
    pages/pageobject/
    pages/pageobject/signup_page.py
    pages/pageobject/login_page.py
    pages/component/
    pages/component/header.py
    pages/component/footer.py


Writing Helper Functions
========================

CI Execution
============

Test Infrastructure
===================

Selecting Elements
==================


