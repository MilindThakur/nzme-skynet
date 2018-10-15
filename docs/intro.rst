+++++++++++++++++++
What and Why Skynet
+++++++++++++++++++

The aim of Skynet is to provide a framework that focuses on writing "good" tests and does the heavy-lifting in terms
of test configuration, initialisation and management. It is built on top of other popular libraries like `Selenium`_ ,
`Appium`_, `Requests`_, `Locust io`_, `Behave`_ to name a few and provides simple APIs for writing maintainable
and reliable test scripts.

Skynet manages multiple browser and devices drivers through high level APIs and a configuration file that can be
overridden at CLI, hence felicitating easy CI integration. Same set of tests can either be run locally or remotely (using
custom grid or something like `Zalenium`_ ..very recommended) by setting flags in a configuration file.


Hooks in Skynet manages drivers (browser and api) internally and exposes execution using tags like @android-app,
@ios-app, @crossbrowser etc. Skynet promotes Page Object (PO) design patterns but also encourages reusing of PO modules
called components (e.g. reusable header, footer in a page) using property @components.


.. _Selenium: http://seleniumhq.org
.. _Appium: http://appium.io/
.. _Requests: http://docs.python-requests.org/en/master/
.. _Locust io: https://locust.io/
.. _Behave: https://behave.readthedocs.io/en/latest/
.. _Zalenium: https://opensource.zalando.com/zalenium/