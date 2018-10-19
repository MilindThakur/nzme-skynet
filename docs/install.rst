.. meta::
    :description: Skynet documentation
    :keywords: skynet, selenium, python, web application, mobile application, api, installation

++++++++++++
Skynet Setup
++++++++++++

Pre-Install
===========

Please make sure you have following installed:
    * Python 2.7
    * git
    * pip
    * virtualenv

Install Browsers and Drivers
============================

    Follow `drivers </drivers>`_ to install necessary browsers and Selenium drivers to run the scripts locally


Install stable release from repo
================================

The Skynet artifacts are not publicly available on PyPi yet and are stored locally in the
`JFrog </https://nzme.jfrog.io/nzme/webapp/#/home>`_ repo. Grab yourself an access and obtain the API key.

To be able to use the _pip_ command to install Skynet, it is advisable to create a _pip.conf_ file with following
configuration.

.. highlight:: bash

::

    $ touch ~/.pip/pip.conf
    $ vi ~/.pip/pip.conf

    [global]
    ; Low timeout
    timeout = 20
    require-virtualenv = true

    ; Custom index
    index-url = https://<firstname.lastname>:<API_Key>@nzme.jfrog.io/nzme/api/pypi/nzme-pypi/simple

To install Skynet

.. highlight:: bash

::

    $ mkvirtualenv skynet
    (skynet)$ pip install nzme-skynet


Install in-dev source code
==========================

To install the source code from the repo, first get yourself access to Grabone bitbucket account. Its best you add your
public ssh key to the account.

.. highlight:: bash

::

    $ git clone git@bitbucket.org:grabone/skynet.git
    $ cd skynet
    $ python setup.py install



