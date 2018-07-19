## Installing Appium for mobile automation ##

### **Manual Install**

* Follow this [handy guide](https://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial) from android central.
* If you are running on linux you need to install some extra 32bit libraries. 
    ```
    sudo apt-get install zlib1g:i386 libc6:i386 libstdc++6:i386
    ```
* Install appium using npm, a [Guide can be found here](https://www.npmjs.com/package/appium)

### **Docker Install - Android Only**

* The [docker-android](https://github.com/butomo1989/docker-android) image is recommended and is used in the
docker-compose.yaml file. This acts as node to Zalenium grid. 

### **iOS & Android - macOS install**
iOS is a special case because Apple made it so. This can only be done on a mac.

* Install xcode (Mac only)
* Install [HomeBrew](https://brew.sh/)
* Install java
    ```
    brew cask install java
    Add JAVA_Home to your .bash_profile
        export JAVA_HOME=$(/usr/libexec/java_home)
        export PATH=${JAVA_HOME}/bin:$PATH
    ```
* Install and configure [Android studio](https://developer.android.com/studio/install.html) 
    ```
    * Add .bash_profile entries if they are not there.
        export ANDROID_HOME=$HOME/Library/Android/sdk
        export PATH=$PATH:$ANDROID_HOME/tools
        export PATH=$PATH:$ANDROID_HOME/platform-tools
    ```
* Resource your Terminal session
    ```
    source ~/.bash_profile
    ```
* Install carthage
    ```
    brew install carthage

    ```
* Install npm (used to install Appium)
    ```
    brew install node
    ```
* Install Appium Doctor
    ```
    npm install -g appium-doctor
    ```
* Run appium doctor, Everything should be green. If its not, remedy the issues before proceeding.
    ```
    appium-doctor
    ```

* Install Appium
    ```
    npm install -g appium
    ```
        
* Start a Simulator and an Emulator 

* Start Appium
    ```
    appium -p 4444 --session-override
    -p is to specify the port
    --session-override is to override the current test session with a new one, Usefull during debug if you stop your test mid run.
    ```

### **Android - Linux install**

* Install java
    ```
    sudo -i apt-get update
    sudo apt-get install default-jdk
    Add JAVA_Home to your .bashrc
        export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
        export PATH=$PATH:${JAVA_HOME}/bin/

    ```
* Install ADB dependancies
    ````    
    sudo apt-get install zlib1g:i386
    ````
* Install and configure [Android studio](https://developer.android.com/studio/install.html) 
    ```
    * Add .bashrc entries if they are not there.
        export ANDROID_HOME=$HOME/android/
        export PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/tools:$ANDROID_HOME/build-tools/26.0.1/
    ```
* Resource your Terminal session
    ```
    source ~/.bashrc
    ```
* Install [npm](https://nodejs.org/en/download/package-manager/)

* Install Appium Doctor
    ```
    npm install -g appium-doctor
    ```
* Run appium doctor, Everything should be green. If its not, remedy the issues before proceeding.
    ```
    appium-doctor
    ```

* Install Appium
    ```
    npm install -g appium
    ```
        
* Start an Emulator 

* Start Appium
    ```
    appium -p 4444 --session-override
    -p is to specify the port
    --session-override is to override the current test session with a new one, Usefull during debug if you stop your test mid run.
    ```