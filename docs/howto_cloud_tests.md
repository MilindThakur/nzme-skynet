## **Multiplatform Browser/App Testing using cloud services**

The framework supports executing tests on remote browsers and devices using the
services provided by the could providers like Browserstack, Saucelabs etc.

### **Desktop browser based tests**

To run test scenarios on multiple browser platforms:
* Update the _testsetup.ini_ config 
file with appropriate capabilities as specified by the provider documentation e.g. [Browserstack](https://www.browserstack.com/automate/capabilities),
[Saucelabs](https://wiki.saucelabs.com/display/DOCS/Platform+Configurator#/) etc

e.g. (Browserstack)

    #------- Desktop Platforms -------#
    [BROWSER]
    browserName=internet explorer
    browserVersion=11.0
    platformName=WINDOWS
    platformVersion=any
    browserstack.local=true
    highlight=true 
  
* Set the environment _local_ variable to _false_  and specify the remote url to test

    
    #------- Environmental -------#
    [ENVIRONMENT]
    testurl=https://www.google.co.nz/
    local=false
    selenium_grid_hub=<cloud_service_command_executor_url>
    zalenium=false
* Start the local tunnel if testing internal sites


    $ ./BrowserStackLocal --key <user_key>
    
Above setup can be overridden in CLI as

    behave <feature_file> --tags=@p1 -D browserName=safari -D browserVersion=11.0
    -D platformName=MAC -D browserstack.local=true -D testurl=https://www.google.co.nz/
    -D local=false -D selenium_grid_hub=<cloud_service_command_executor_url>
    
### **Browser based tests on devices**

To run test scenarios on multiple browsers across devices (ios/android),
* Tag the scenarios with _@android-web_ or _@ios-web_ tags
* Update the appropriate _[ANDROID]_ or _[IOS]_ sections of the 
_testsetup.ini_ config file with appropriate capabilities as specified by the 
provider documentation

e.g. IOS browser (Browserstack)

    [IOS]
    browserName=safari
    platformName=iOS
    platformVersion=11.0
    deviceName=iPhone X
    browserstack.local=true
    real_mobile=true
    
e.g. ANDROID browser (Browserstack)

    [ANDROID]
    browserName=chrome
    platformName=Android
    platformVersion=8.0
    deviceName=Samsung Galaxy S9 Plus
    browserstack.local=true
    real_mobile=true

* Set the environment _local_ variable to _false_  and specify the remote url to test


    #------- Environmental -------#
    [ENVIRONMENT]
    testurl=https://www.google.co.nz/
    local=false
    selenium_grid_hub=<cloud_service_command_executor_url>
    zalenium=false

### **Using Zalenium**

Start Zalenium enabled with Browserstack/Saucelabs/TestingBot 
(including tunnel if required) as per [doc](https://opensource.zalando.com/zalenium/)

Set the environment as below:

     #------- Environmental -------#
    [ENVIRONMENT]
    testurl=https://www.google.co.nz/
    local=false
    selenium_grid_hub=<zalenium_grid_url>
    zalenium=true
