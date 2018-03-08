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

### **Supported Tags for use with Behave**
We use Behave as our BDD Runner, while skynet does not require you to use it, it does have some extra support built in.
We supported the following tags to specify what platform you want for the given test.
Specifying a single one of these tag's either in command line or debug params. If no platform tag is specified, then the default platform of web is used.
```
@api
@android-app
@android-browser
@ios-app
@ios-browser
   
```
