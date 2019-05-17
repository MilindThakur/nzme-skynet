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
        capabilities =  {
                        'os' : 'Windows',
                        'os_version' : '10',
                        'browser' : 'Chrome',
                        'browser_version' : '73.0',
                        'resolution' : '1920x1080',
                        'project' : 'test_project',
                        'build' : 'test_build',
                        'name' : 'test_name',
                        'browserstack.local' : 'true',
                        'browserstack.debug' : 'true',
                        'browserstack.selenium_version' : '3.14.0'
                        }
      
* Set the environment _local_ variable to _false_  and specify the remote url to test

    
        #------- Environmental -------#
        [ENVIRONMENT]
        testurl=https://www.google.co.nz/
        local=false
        selenium_grid_hub=<cloud_service_command_executor_url>
        zalenium=false

* Start the local tunnel if testing internal sites


        $ ./BrowserStackLocal --key <user_key>
    
* Run the tests


        $ behave --tag=@p1 --browserName=chrome     

    
### **Browser based tests on devices**

To run test scenarios on multiple browsers across devices (ios/android),
* Tag the scenarios with _@android-browser_ or _@ios-browser_ tags
* Update the appropriate _[ANDROID]_ or _[IOS]_ sections of the 
_testsetup.ini_ config file with appropriate capabilities as specified by the 
provider documentation

e.g. IOS (Browserstack)

        [IOS]
        capabilities = {
                        'os_version' : '12',
                        'device' : 'iPhone XS Max',
                        'real_mobile' : 'true',
                        'project' : 'test',
                        'build' : 'test_123',
                        'name' : 'loginTest',
                        'browserstack.local' : 'true',
                        'browserstack.debug' : 'true',
                        'browserstack.networkProfile' : '4g-lte-high-latency',
                        'browserstack.video' : 'false'
                        }
         
* Set the environment _local_ variable to _false_  and specify the remote url to test


    #------- Environmental -------#
    [ENVIRONMENT]
    testurl=https://www.google.co.nz/
    local=false
    selenium_grid_hub=<cloud_service_command_executor_url>
    zalenium=false

* Run the tests


        $ behave --tag=@p1 --tags=@ios-browser

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
