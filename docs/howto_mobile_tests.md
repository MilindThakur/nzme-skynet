## **Mobile Tests Features included:**
* Android/iOS mobile app
* Android/iOS web (chrome/safari)

### **Installation**

The framework uses appium to run the tests on Android/iOS. Please follow [installation instructions](./install_appium.md) for appium 

### How to run tests on Android and iOS devices

Start the appium server or launch the docker setup using [docker script](../docker_compose.sh)

The configuration for mobile tests are set in the testsetup.ini file, available at the root of the project

    #------- Mobile Platforms -------#
    [ANDROID]
    platformVersion=8.1
    version=8.1
    deviceName=Android Emulator
    browserName=chrome
    app=<path_to_apk>
    appPackage=<package_name>
    appActivity=<activity_name>
    fullReset=true

    [IOS]
    platformName=iOS
    platformVersion=11.2
    deviceName=iPhone 6
    app=<path_to_zip>
    bundleId=<bundle_id>
    browserName=Safari
    fullReset=false
    
The capabilities can be directly added to the setup based on needed configuration. These capabilities are passed on to 
the appium server by the framework.

    [IOS]
    platformName=iOS
    platformVersion=11.2
    deviceName=iPhone 6
    app=<path_to_zip>
    bundleId=<bundle_id>
    iosBrowserName=Safari
    fullReset=false
    locationServicesEnabled=false
    locationServicesAuthorized=false
    autoDismissAlerts=true

Set the appium server url in the section ENVIRONMENT

    #------- Environmental -------#
    [ENVIRONMENT]   
    testurl=<url_to_test_for_web>
    local=false
    zalenium=true
    selenium_grid_hub=http://localhost:4444/wd/hub
       
Tag the BDD scenarios with:

     @android-app
     @android-browser
     @ios-app
     @ios-browser
