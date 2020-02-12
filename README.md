# **Skynet - Test Automation Library @ [NZME](https://www.nzme.co.nz/)**

[![Build Status](https://travis-ci.org/MilindThakur/nzme-skynet.svg?branch=master)](https://travis-ci.org/MilindThakur/nzme-skynet)
[![codecov](https://codecov.io/gh/MilindThakur/nzme-skynet/branch/master/graph/badge.svg)](https://codecov.io/gh/MilindThakur/nzme-skynet)

## **Features included:**
* A python3.6+ library to automate web apps and mobile apps across range of browsers and devices
* Scripts to automate visual testing
* Out of box integration with cloud testing (e.g. Sauce Labs)
* Plugin to run REST api calls
* Support for BDD scenarios and parallel execution run
* Support for Mobile app testing, see [Mobile app readme](docs/howto_mobile_tests.md)
* Capture and manipulate HTTP traffic using browsermob-proxy 

## **Install Skynet package:**
 Install from source.
 
        $ git clone <repo>
        $ cd skynet
        $ python setup.py install 

## **Setup instructions**

### **Install pip, web browsers, Emulators**
* Python 3.6+
* Download [Chrome browser](https://www.google.com/chrome/browser/desktop/index.html) and [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/)
* Download Firefox. Firefox > v.47 requires [Marionette](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette) driver
* To verify drivers are working [check these instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/verify_webdriver.md)
* Install [mobile dependencies](docs/howto_mobile_tests.md) or docker solution e.g. [Selenoid Android](https://aerokube.com/selenoid/latest/#_android),
[docker-android](https://github.com/budtmo/docker-android)
* (optional) Install Selenium Grid of choice e.g. [Zalenium](https://github.com/zalando/zalenium),
[Selenoid](https://github.com/aerokube/selenoid), [docker-selenium](https://github.com/SeleniumHQ/docker-selenium) etc


        $ git clone <repo>
        $ cd skynet
        $ python3 -m venv skynet3-env
        $ source skynet3-env/bin/activate
        (skynet3-env) $ pip install -U pip
        (skynet3-env) $ pip install pipenv
        (skynet3-env) $ pipenv sync --dev
     
## **Run Tests**

You can run all of the tests via `tox` in your local

        (skynet3-env) $ deactivate
        $ sudo apt install python-tox
        $ tox

For detailed run:

Setup test env

        $ source skynet3-env/bin/activate
        (skynet3-env) $ ./docker_compose.sh start
        (skynet3-env) $ curl -sSL http://localhost:4444/wd/hub/status | jq .value.ready | grep true
        
Run tests (with coverage)

        (skynet3-env) $ py.test -vvv --cov=nzme_skynet test     
        
To run all the tests in parallel

        (skynet3-env) $ py.test -n <no_of_parallel_processes> test

To run individual tests

        (skynet3-env) $ py.text -q test/<test_name.py>
        
Teardown test env

        (skynet3-env) $ ./docker_compose.sh stop

## **BDD Test Setup**

Test setup is managed in a default configuration file _testsetup.ini_ which can be overridden on commandline.

```
#------- Desktop Platforms -------#
[BROWSER]
#- Generic Selenium/Cloud capabilities -#
capabilities =  {
                "browserName": "chrome",
                "version": "ANY",
                "platform": "ANY",
                "goog:chromeOptions" : {
                    "args": ["--disable-gpu"],
                    "extensions": [],
                    "prefs": {}
                    }
                }
#- Framework specific capabilities -#
highlight = true
resolution = maximum # e.g. maximum, 1126x830
headless = false
mobileEmulation = # e.g. iPhone X, Galaxy S5 etc

#------- Mobile Platforms -------#
#- Generic Appium capabilities -#
[ANDROID]
capabilities = {
                "platformName": "Android",
                "platformVersion": "8.1",
                "deviceName": "Device 01"
                "udid": "emulator-5554",
                "appPackage": "appPackage",
                "appActivity": "appActivity",
                "app": "/path/to/my.app"
                }

[IOS]
capabilities = {
                "platformName": "iOS",
                "platformVersion": "11.0",
                "deviceName": "iPhone 7",
                "automationName": "XCUITest",
                "app": "/path/to/my.app"
                }

#------- Environmental -------#
#- Framework specific capabilities -#
[ENVIRONMENT]
testurl=https://www.google.co.nz/
local=true
selenium_grid_hub=http://127.0.0.1:4444/wd/hub
zalenium=false
```
The capabilities key is "free-form" selenium/appium/cloud capabilities key-value pair that is passed on to the
framework. 

For desktop tests, one can remove the sections [Android] and [IOS], similarly for mobile tests
one can remove the section [BROWSER]. The section [ENVIRONMENT] is however mandatory.

One can also have separate "_testsetup.ini_" files for different runs e.g. _testsetup_browserstack.ini_ with browserstack
specific capabilities only, or _testsetup_android.ini_ for android tests. This custom .ini can be passed as a 
command line parameter for behave tests.

    (skynet3-env) $ behave -D configfile=testsetup_browserstack.ini --tags=@p1
    (skynet3-env) $ behave -D configfile=testsetup_android.ini --tags=@android-app --tags=@p1
    
The capabilities and environment key value options can also be updated on the commandline.

    (skynet3-env) $ behave -D browserName=firefox -D version=65.0 -D local=true -D headless=true --tags=@p1


### **BDD Parallel Tests Run utility**
Allows running BDD tests in parallel, hence saving on execution time.
```bash
(skynet3-env) $ nzme-behave-parallel -h
usage: Run behave in parallel mode for scenarios [-h] [--processes PROCESSES]
                                                 [--tags TAGS]
                                                 [--define DEFINE]

optional arguments:
  -h, --help            show this help message and exit
  --processes PROCESSES, -p PROCESSES
                        Maximum number of processes. Default = 5
  --tags TAGS, -t TAGS  specify behave tags to run
  --define DEFINE, -D DEFINE
                        Define user-specific data for the config.userdata
                        dictionary. Example: -D foo=bar to store it in
                        config.userdata["foo"].
```
E.g. to run 4 scenarios in parallel based on tags and override test configuration
```bash
(skynet3-env) $ nzme-behave-parallel -p 4 -t prod -D local=false -D browserName=firefox
```

### **Supported Tags for use with Behave**
We use Behave as our BDD Runner, while skynet does not require you to use it, it does have some extra support built in.
You can tag the scenarios/feature files with the following platform tags to initialise appropriate driver.  

If no platform tag is specified, then the default platform of web/browser is used.
```
@api
@android-app
@android-browser
@ios-app
@ios-browser
   
```
