# **Skynet Features Roadmap**

## **Drivers**:
* Initialise multiple drivers in a single test run. This will allow running same test across
local, remote and remote device browsers in parallel e.g. using tag @cross-browser
    * Restarting driver
    * Retrieve driver by session
    * Replace drivers

## **Page Objects:**
* Concept of Primary and Secondary locators. Primary locators will confirm that the
page is displayed. Create @primary decorator, which auto checks if the page is loaded
* Use decorator @component for re-usable component POs within a Page. Handle lazy
loading as part of decorator: **Done**
* Special case of multiple similar components on a page e.g. multiple deals. Should be
able to load as
 
        deal(1).name 
        deal('title').select()

## **Elements**
* Expose only relevant element types, hide Clickable() etc.

## **BDD Tests**
* Test retries on failures: **DONE:**: use tag _@auto_retry_ for unstable tests.
* Ability to run same scenario/feature on both android and ios in parallel using tag like 
@cross-device
* Ability to run same scenario/feature across browsers using tag like @cross-browser


## **Generic**
* Log browser console errors
* Increase test coverage. 
* Manage cloud capabilities in a separate file and select the platform in the testsetup.ini
config: **DONE:** use separate _testsetup.ini_ files

        $ behave -D configfile=testsetup_browserstack.ini --tags=@p1
        $ behave -D configfile=testsetup_android.ini --tags=@android-app --tags=@p1 

