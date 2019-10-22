# **Skynet - Test Automation Library @ NZME - Changelog**

```bash
0.5.0   Migrate to python 3.6+
0.4.4   Add travis CI for build on github, last build supporting python2.7
0.4.3   Add ability to find element/s within the parent container, refactor browser proxy, fix chrome mobileEmulation 
        rendering
0.4.2   Fix unittests
0.4.1   Update docs, pep8 styling
0.4.0   ** BREAKING CHANGE **: new testsetup.ini config to support "free-form" capabilities  
0.3.28  Add step screenshots to allure report
0.3.27  Fix API request initialization
0.3.26  Upgrade to Selenium 3.141.0, introduce declarative pipeline and code cov
0.3.25  Improve click method, add methods to wait_for_url, wait_for_url_to_contain, include typing,
        remove dependency on zalenium version for running integration tests
0.3.24  Re-introduce opening testurl before every scenario, needed for setting cookie in zalenium
0.3.23  Add cloud testing capability, upgrade to selenium 3.14.0
0.3.22  Fix chrome headless in remote mode
0.3.21  Update to selenium 3.13.0, add debug logs, update docs
0.3.20  Refactor mobile driver creation to accept capabilities from ini 
0.3.19  Add additional params for delete request
0.3.18  Add default capability of fullReset to android driver
0.3.17  Upgrade to selenium 3.11.0
0.3.16  Fix behave parallel issue. Now handles any tag at any scenario/feature level
0.3.15  Remove redundant allure error logging
0.3.14  Implement behave v1.2.6 API change, update selenium to 3.10.0
0.3.13  iOS mobile app driver - Corrected bad import path for default timouts 
0.3.12  iOS mobile app driver - Exposing timeout for accepting location services.
0.3.11  Add support iOS and Android mobile app testing
0.3.10  Better logging for behave tests
0.3.9   Upgrade selenium to 3.8.1
0.3.8   Turn element highlighting using a config flag
0.3.7   Run one thread per feature when running tests in parallel, better reporting
0.3.6   Ability to include build no for debugging in CI using zalenium
0.3.5   Ability to reference test steps in zalenium video logs through pop ups
0.3.4   Fix parsing a custom selenium grid url
0.3.3   Fixes for parallel tests, maximise window and expose driver exception
0.3.2   Upgrade selenium to 3.7.0
0.3.1   Revert importing elements from controls package
0.3.0   Refactored framework - BREAKING CHANGE !!
0.2.22  Add support for runnig UI tests through a proxy
0.2.21  Upgrade to selenium 3.5.0
0.2.20  Add support for running Android app and browser tests using appium
0.2.19  Fix running BDD scearios parallel with multiple tags and defines
0.2.18  Fix running BDD scearios parallel with multiple tags 
0.2.17  Add support for running BDD tests in parallel
0.2.16  Add support for Selenium Grid - BREAKING CHANGE - need update to testconfig.ini
0.2.15  Fix selenium driver taking too long to load
0.2.14  Update dependencies
0.2.13  Make API Wrapper generic
0.2.12  Update selenium to 3.0.1
0.2.11  Remove API flag from testconfig. Run api tests using @api
0.2.10  Add default content-type as json to API requests
0.2.9   Fix API post argumen to json
0.2.8   Fix API post, handle API tests in bdd
0.2.7   Add api wrappers to framework
0.2.6   Handle elemets stated internally in click method 
0.2.5   Fix pytest-allure version dependency
0.2.4   Set default timeout to 1sec for short explicit waits
0.2.3   Add explicit wait for elem to be present (In DOM), visible (has height & width), interactable
0.2.2   Add handling lazy loaded images
0.2.1   Add faker and alluer dep to setup.py
0.2.0   Add bdd and browser (chrome) test capability
0.1.10  Add pagevalidation utility 
0.1.9   Update README with screenshot utility
0.1.8   Add screenshot script as console script to the repo
0.1.7   Handle installing package through constraints
0.1.6   Fix: when no device are specified
0.1.5   Manage list of devices internally
0.1.3   Update screenshots to specify custom folder options
0.1.2   Add Jenkinsfile
0.1.1   Update MANIFEST.in
0.1.0   Inital version
```