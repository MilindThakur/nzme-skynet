
.. meta::
    :description: Skynet Tutorial
    :keywords: python, selenium, tutorial, tests

+++++++++++++++
Skynet Tutorial
+++++++++++++++

Make sure you have skynet installed as per :doc:`installation</install>` instruction


As a script
===========

Skynet APIs can be used as a python script or within a unittest framework like unittest, pytest etc.

.. highlight:: python

::

    from nzme_skynet.core.driver.driverregistry import DriverRegistry
    from nzme_skynet.core.controls.textinput import TextInput
    from nzme_skynet.core.controls.button import Button

    # Default is local Chrome driver
    DriverRegistry.register_driver()

    driver = DriverRegistry.get_driver()

    # Visit url
    driver.goto_url("https://www.google.co.nz", absolute=True)

    # Create a UI control object
    search_input = TextInput(By.NAME, 'q')
    submit_search_btn = Button(By.NAME, 'btnK')

    # UI control methods available based on type of UI object initialised
    search_input.set_value('nzme')
    submit_search_btn.click()

    # Default UI object is Element
    search_result_container = Element(By.ID, 'rso')

    # Wait API handles async nature
    search_result_container.will_be_visible()
    driver.wait_for_url_to_contain('nzme')

    # Deregister/close driver
    DriverRegistry.deregister_driver()


As a BDD tool
=============

Skynet uses `behave </https://github.com/behave/behave>`_ as a BDD tool and has in built hooks, tags for auto test
initialisation. The test configuration is driven by a testsetup.ini config file and can be overridden in CLI using behave
command line.

A typical feature file will look like as follows:

.. highlight:: bash

::


Built-in command line script
============================


