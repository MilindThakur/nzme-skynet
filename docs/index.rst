.. Skynet documentation master file, created by
   sphinx-quickstart on Fri Oct 12 16:40:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. meta::
   :description: Documentation for Skynet, tool for testing web, mobile appliations and APIs with in-build BDD support
   :keywords: selenium, python, bdd, behave, web, testing, regression

Welcome to Skynet's documentation!
==================================

Skynet is a Python based tool to automate testing of web applications and services, mobile apps across range of browsers and mobile
devices. Skynet has built-in support for writing acceptance tests using Gherkin syntax.

Features
--------

* A python library to automate web apps and mobile apps across range of browsers and devices
* Out of box integration with cloud testing (e.g. Sauce Labs)
* Plugins to query database, run REST api calls and load tests
* Support for BDD style acceptance tests
* Support for Mobile app/browser testing
* CLI scripts for basic browser validations e.g. link, images, js errors etc

Sample Code
-----------

.. highlight:: python

::

   from nzme_skynet.core.driver.driverregistry import DriverRegistry
   from nzme_skynet.core.controls.textinput import TextInput
   from nzme_skynet.core.controls.button import Button

   DriverRegistry.register_driver() # Default is local Chrome driver
   driver = DriverRegistry.get_driver()
   driver.goto_url("https://www.google.co.nz")
   search_input = TextInput(By.NAME, 'q')
   submit_search_btn = Button(By.NAME, 'btnK')
   search_input.set_value('nzme')
   submit_search_btn.click()
   search_result_container = Element(By.ID, 'rso')
   search_result_container.will_be_visible()
   driver.wait_for_url_to_contain('nzme')
   DriverRegistry.deregister_driver()


Getting Started
---------------
* :doc:`Intro </intro>`
* :doc:`Installation </install>`
* :doc:`Quick Tutorial </tutorial>`
* :doc:`Project Setup </setup>`

Contribute
==========

* :doc:`Setting dev environment</contribute>`

