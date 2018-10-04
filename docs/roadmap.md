# **Skynet Features Roadmap**

## **Drivers**:
* Initialise mutiple drivers in a single test run. This will allow running same test across
local, remote and remote device browsers in parallel e.g. using tag @cross-browser
    * Restarting driver
    * Retrieve driver by session
    * Replace drivers

## **Page Objects:**
* Concept of Primary and Secondary locators. Primary locators will confirm that the
page is displayed. Create @primary decorator, which auto checks if the page is loaded
* Use decorator @component for re-usable component POs within a Page. Handle lazy
loading as part of decorator.
* Special case of multiple similar components on a page e.g. multiple deals. Should be
able to load as
 
        deal(1).name 
        deal('title').select()

## **Elements**
* Expose only relevant element types, hide Clickable() etc.
* 

## **BDD Tests**
* Test retries on failures
* Ability to run same scenario/feature on both android and ios in parallel using tag like 
@cross-device
* Ability to run same scenario/feature across browsers using tag like @cross-browser


## **Generic**
* Log browser console errors
* Increase test coverage. 
* Manage cloud capabilities in a separate file and select the platform in the testsetup.ini
config

e.g. _browserstack_devices.json_
```
    {
        "browserstack_Windows_10_Edge": {
        "deviceName": "Browserstack Windows 10 Edge", 
        "desiredCapabilities": {
                "browser": "Edge",
                "browser_version": "17.0",
                "os": "Windows",
                "os_version": "10",
                "resolution" : "1280x1024",
                "browserstack.local" : "true"
                }
            }
        },
        "browserstack_Android_S8": {
        "deviceName": "Browserstack Android S8",
        "desiredCapabilities": {
                "browser": "Chrome",
                "device" : "Samsung Galaxy S8",
                "os_version": "7.0",
                "real_mobile": "true",
                "browserstack.local" : "true",
                "browserstack.appium_version" : "1.7.2"
                }
        }
    }
```
And use it testsetup.ini
```
[ENVIRONMENT]
testurl=https://www.google.co.nz/
local=flase
selenium_grid_hub=<browserstack_hub_url>
zalenium=false
browserstack_device=browserstack_Android_S8

```
