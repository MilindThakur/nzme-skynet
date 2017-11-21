# **Skynet - Test Automation Library @ NZME**

## **Features included:**
* A python library to automate web apps and mobile apps across range of browsers and devices
* Scripts to automate visual testing
* Out of box integration with cloud testing (e.g. Sauce Labs)
* Plugins to query database, run REST api calls and load tests
* Support for BDD
* Support for Mobile app testing, see [Mobile app readme](docs/MOBILEREADME.md)

## **Setup instructions**

### **Local install (non docker)** 
### **Install pip, web browsers, Emulators**
* [Follow these instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/requirements_installation.md) to install pip, git, virtualenv/virtualenvwrapper
* Download [Chrome browser](https://www.google.com/chrome/browser/desktop/index.html) and [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/)
* Download Firefox. Firefox > v.47 requires [Marionette](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette) driver
* Install [PhantomJS](http://phantomjs.org/download.html) (headless browser)
* Install [mobile dependencies] 

### **Clone Skynet automation repo**
```bash
git clone git@bitbucket.org:grabone/skynet.git
cd skynet
```

### **Create and activate virtualenv**
[Follow instructions](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/virtualenv_instructions.md) to create and activate a python virtualenv

### **Install the python dependencies in a virtualenv**
```bash
pip install -r requirements.txt -c requirements/constraints.txt
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

## **Install on-demand test infrastructure**
We use a docker based on-demand Selenium Grid Infrastructure called [Zalenium](https://github.com/zalando/zalenium)
### **Prerequisites**
* Docker and docker-compose is installed

### **Run it**
* To start the hub
```bash
./docker_compose.sh start
```
* You can see the DockerSeleniumStarter node in the [grid](http://localhost:4444/grid/console)
* You can live preview your running tests on [live]( http://localhost:4444/grid/admin/live)
* You can view the recorded video, selenium and driver longs on the [dashboard](http://localhost:5555/)
* To stop the hub
```bash
./docker_compose.sh stop
```
### **Docker configuration**
The test infrastructure configurations are managed in the _**docker-compose.yaml_** file. To test any browser on any cloud provider
 * Add appropriate cloud provider environment variables (username, access-key)
 * Set the flag _--sauceLabsEnabled_ (or other provider) to true
 * Set flag _--startTunnel_ to true
 * Start the hub

To enable video recording on the tests
 * Set the flag _--videoRecordingEnabled_ to true (the videos will be available in the _/tmp/videos_ folder and dashboard)
 
## **Test Setup**
Test setup is managed in a configuration file _testsetup.ini_ which can be overridden on commandline
To run the tests in cloud (grid):
* Set the flag _local_ to false
* Set the BROWSER details
* Start the grid

## **Scripts**
The package includes scripts to be able to run from commandline

### **Screenshot utility**
Allows taking screenshots of the webpages across multiple devices (uses phandtom.js)
```bash
$ pip install nzme-skynet
$ nzme-screenshots -h
usage: nzme-screenshots [-h] [--devices DEVICES] [--folder FOLDER] urls

positional arguments:
  urls               json file with list of urls

optional arguments:
  -h, --help         show this help message and exit
  --devices DEVICES  comma separated device names, by default takes snapshot
                     on all devices
  --folder FOLDER    path to save screenshots, by default saved to a folder
                     SCREENSHOT in same directory

$ nzme-screenshots --devices iPhone_5,iPhone_6_Plus,Nexus_7,Surface_Pro,Macbook_Pro_15 --folder ../results urls.json
```

List of urls to generate snapshots should be a file of a json format:
```bash
urls.json
{
  "urls": [
    {
      "name": "Google HomePage",
      "url": "https://www.google.co.nz/?gws_rd=ssl"
    }
  ]
}
```

List of devices available to test:
```bash
iPhone_4, iPhone_5, iPhone_6, iPhone_6_Plus, Samsung_S3, Samsung_S4, Nexus_4, iPad_Mini, iPad_2, iPad_4, Nexus_7, Surface_RT, Surface_Pro,
Nexus_10, Macbook_Air_11, Macbook_Air_13, Macbook_Pro_15, Macbook_Pro_Retina, iMac_27
```

### **Page Validation utility**
Checks validity of images, links and javascript on url(s) passed in.  If a folder path is specified
then results are output to a json file in that folder, else results are printed to the console.

```bash
$ pip install nzme-skynet
$ nzme-pagevalidation -h
usage: nzme-pagevalidation [-h] [-f FOLDER] [--checkimages] [--checklinks]
                           [--checkjs] [--checkall]
                           urls

positional arguments:
  urls                  "url or comma separated list of urls, encased in single or double quotes"

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        folder name to save results to
  --checkimages         validate images on url(s)
  --checklinks          validate links on url(s)
  --checkjs             validate js on url(s)
  --checkall            validate all on url(s)


$ nzme-pagevalidation --checkimages --checklinks 'https://www.nzherald.co.nz','http://www.zmonline.com' -f /home/Documents
```

### **BDD Parallel Tests Run utility**
Allows running BDD tests in parallel, hence saving on execution time.
```bash
$ pip install nzme-skynet
$ nzme-behave-parallel -h
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
$ nzme-behave-parallel -p 4 -t prod -D local=false -D type=firefox
```


# Change Log
```bash
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