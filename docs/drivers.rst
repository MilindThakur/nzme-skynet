
.. meta::
    :description: Installing browsers and drivers for UI tests
    :keywords: selenium, driver, webdriver, chrome, firefox, phantomjs, mobile

++++++
Chrome
++++++

Download the latest `Chrome browser</https://www.google.com/chrome/browser/desktop/index.html>`_ and
`Chrome driver</https://sites.google.com/a/chromium.org/chromedriver/>`_

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

+++++++
Firefox
+++++++

Download the latest `Firefox browser</https://www.mozilla.org/en-US/firefox/new/>`_ and
`Marionette driver</https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette>`_

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

+++++++++
PhantomJS
+++++++++

Although PhantomJS is no longer supported, one can `install</http://phantomjs.org/download.html>`_ the headless driver.

On linux, you can also use the following script to download/install latest Marionette driver

.. highlight:: bash

::

    cd /usr/local/share
    sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
    sudo tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2
    sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
    sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
    sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs


Verify driver installation
==========================

To verify if the drivers have been installed properly.

.. highlight:: bash

::

    $ python
    >> from selenium import webdriver
    >> driver = webdriver.Chorme() # Should start Chrome browser
    >> driver = webDriver.Firefox() # Should start Firefox browser
    >> driver = webdriver.PhantomJS()
