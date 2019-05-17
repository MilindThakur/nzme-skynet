## **Mobile Tests Features included:**
* Android/iOS mobile app
* Android/iOS web (chrome/safari)

### **Installation**

The framework uses Appium to run the tests on Android/iOS. Please follow [installation instructions](./install_appium.md)
for Appium 

### How to run tests on Android and iOS devices

Start the Appium server or launch [docker-android](https://github.com/budtmo/docker-android) or 
[Selenoid Appium](https://aerokube.com/selenoid/latest/#_android)

The configuration for mobile tests are set in the _testsetup.ini_ file, available at the root of the project

    #------- Mobile Platforms -------#
    [ANDROID]
    capabilities = {
                    }

    [IOS]
    capabilities = {
                    }
    
The capabilities can be directly added to the setup based on needed configuration. These capabilities are used to launch
an appropriate device driver by the framework and relayed over Appium.

    [ANDROID]
    capabilities = {
                    "platformName": "Android",
                    "platformVersion": "9",
                    "deviceName": "Android Emulator 01",
                    "appPackage": "<app_package_name>",
                    "automationName":"UiAutomator2",
                    "app": "<apk_location>",
                    "appActivity": "<activity_name>",
                    "fullReset":True,
                    "clearSystemFiles":True,
                    "newCommandTimeout":3000
                    }

Set the Appium server url in the section ENVIRONMENT

    #------- Environmental -------#
    [ENVIRONMENT]   
    testurl=<url_to_test_for_web>
    local=false
    zalenium=true
    selenium_grid_hub=<appium_url>
       
Tag the BDD scenarios with:

     @android-app
     @android-browser
     @ios-app
     @ios-browser
     
Run the tests (use tags based on platform to run)

    $ behave --tags=@p1 --tags=@android-app
