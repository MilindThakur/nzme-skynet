
.. meta::
    :description: Installing browsers and drivers for UI tests
    :keywords: selenium, driver, webdriver, chrome, firefox, phantomjs, mobile

+++++++++++++++++++++++++
Driver Installation
+++++++++++++++++++++++++

Local Browsers and Drivers
==========================

Chrome
------

Download the latest `Chrome browser <https://www.google.com/chrome/browser/desktop/index.html>`_ and
`Chrome driver <https://sites.google.com/a/chromium.org/chromedriver/>`_

On linux, you can also use the following script to download/install Chrome driver

.. highlight:: bash

::

    sudo apt-get install unzip
    LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
    wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver
    sudo mv -f chromedriver /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

Firefox
-------

Download the latest `Firefox browser <https://www.mozilla.org/en-US/firefox/new/>`_ and
`Marionette driver <https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette>`_

On linux, you can also use the following script to download/install latest Marionette driver

.. highlight:: bash

::

    LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json' https://github.com/mozilla/geckodriver/releases/latest)
    LATEST_VERSION=$(echo $LATEST_RELEASE | sed -e 's/.*"tag_name":"\([^"]*\)".*/\1/')
    LATEST_DRIVER="geckodriver-$LATEST_VERSION-linux64.tar.gz"
    wget https://github.com/mozilla/geckodriver/releases/download/$LATEST_VERSION/$LATEST_DRIVER
    tar -xvzf $LATEST_DRIVER
    chmod +x geckodriver
    sudo mv -f geckodriver /usr/local/share/geckodriver
    sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver
    sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver
    rm $LATEST_DRIVER

PhantomJS
---------

Although PhantomJS is no longer supported, one can `install <http://phantomjs.org/download.html>`_ the headless driver.

On linux, you can also use the following script to download/install the last available phantomjs driver

.. highlight:: bash

::

    cd /usr/local/share
    sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
    sudo tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2
    sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
    sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
    sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs


Verify driver installation
--------------------------

To verify if the drivers have been installed properly.

.. highlight:: bash

::

    $ python
    >> from selenium import webdriver
    >> driver = webdriver.Chorme() # Should start Chrome browser
    >> driver = webDriver.Firefox() # Should start Firefox browser
    >> driver = webdriver.PhantomJS() # Should start headless PhantomJS browser
    >> driver.get("https://www.google.co.nz") # Should navigate to the page
    >> driver.quit() # Should close the browser

Dockerised Selenium
===================

You can also run `docker selenium <https://github.com/elgalu/docker-selenium/blob/master/README.md>`_ container to
access Chrome and Firefox browsers which are available on *http://localhost:4444/wd/hub* by default.

We highly recommend using `Zalenium <https://opensource.zalando.com/zalenium/>`_ as a fast, flexible and scalable
container based selenium grid for UI tests.

To access browsers running in a docker container

.. highlight:: python

::

    $ python
    >> from selenium import webdriver
    >> desired_caps = {}
    >> desired_caps['version'] = "ANY"
    >> desired_caps['platform'] = "ANY"
    >> desired_caps['browserName'] ="chrome"
    >> driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps) # Should start Chrome browser
    >> driver.quit() # Should close the browser

Mobile Driver
=============

Appium
------

Use the official `Appium documentation <http://appium.io/docs/en/about-appium/getting-started/?lang=en>`_ to install
the driver based on your OS.

If you are running on linux you need to install some extra 32bit libraries.

.. highlight:: bash

::

    sudo apt-get install zlib1g:i386 libc6:i386 libstdc++6:i386

You could also install `Appium Desktop <https://github.com/appium/appium-desktop>`_ if you prefer using a UI tool.

Install `Android Studio <https://developer.android.com/studio/index.html>`_ to setup an Emulator. Launch suitable emulator
for testing apps or webapps using Chrome/native Android browser.



Launch `Apple Simulators <https://help.apple.com/simulator/mac/current/#/deve44b57b2a>`_ for testing apps or webapps using
safari.

You could also use `docker-android <https://github.com/butomo1989/docker-android>`_ to launch appium server and android
emulator in the same container.