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

## **Scripts**
The package includes scripts to be able to run from commandline

### **Screenshot utility**
Allows taking screenshots of the webpages across multiple devices
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
  urls                  url or comma separated list of urls

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        folder name to save results to
  --checkimages         validate images on url(s)
  --checklinks          validate links on url(s)
  --checkjs             validate js on url(s)
  --checkall            validate all on url(s)



$ nzme-pagevalidation --checkimages --checklinks https://www.nzherald.co.nz,http://www.zmonline.com -f /home/Documents
```

# Change Log
```bash
0.1.10  Update README with pagevalidation utility 
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