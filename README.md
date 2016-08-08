# **Skynet - Test Automation Library @ NZME**

## **Features included:**
* A python library to automate web apps and mobile apps across range of browsers and devices
* Scripts to automate visual testing
* Out of box integration with cloud testing (e.g. Sauce Labs)
* Plugins to query database, run REST api calls and load tests
* Support for BDD

## **Setup instructions**

### **Install pip, web browsers**
* [Follow these instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/requirements_installation.md) to install pip, git, virtualenv/virtualenvwrapper
* Download [Chrome browser](https://www.google.com/chrome/browser/desktop/index.html)
* Download [Firefox v.46 browser](https://ftp.mozilla.org/pub/firefox/releases/46.0.1/). Firefox > v.47 requires [Marionette](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette) driver which is in beta phase (and not currently support in this library)
* Install [PhantomJS](http://phantomjs.org/download.html) (headless browser)


### **Clone Skynet automation repo**
```bash
git clone git@bitbucket.org:grabone/skynet.git
cd skynet
```

### **Create and activate virtualenv**
[Follow instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/virtualenv_instructions.md) to create and activate a python virtualenv

### **Install the python dependencies in a virtualenv**
```bash
pip install -r requirements.txt
```

To verify drivers are working [check these instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/verify_webdriver.md)

### **Verify skynet has installed successfully**
The following commands will run all the unittests written for the library
```bash
cd tests
py.test
```

To run all the tests in parallel
```bash
py.test -n <no_of_parallel_processes>
```

To run individual tests
```bash
py.text -q <test_name.py>
```
