# **Skynet - Test Automation Library @ NZME - Mobile**

## **Features included:**
* Android mobile app
* Android web (chrome)
* ios
* ios web (safari)(Coming soon)

## **Setup instructions**
This is a supplimentry to guide the the [Skynet Readme](../README.md)


### **Local install (non docker)** 
* If you plan to run mobile tests within docker (Android only support), the containers will spawn with the docker_compose.sh start command.
  The containers are defined in the docker-compose.yml found within the project directory.

# **Manual install**
* Follow this [handy guide](https://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial) from android central.
* If you are running on linux you need to install some extra 32bit libraries. 
    ```
    sudo apt-get install zlib1g:i386 libc6:i386 libstdc++6:i386
    ```
* Install appium using npm, a [Guide can be found here](https://www.npmjs.com/package/appium)

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
        
* Start an Emulator 

* Start Appium
    ```
    appium -p 4444 --session-override
    -p is to specify the port
    --session-override is to override the current test session with a new one, Usefull during debug if you stop your test mid run.
    ```
    
### How to run tests on Android and iOS devices

Start the appium server as per the command above.
Edit the testsetup.ini file, present at the root of the project, such that the selenium server is (set by default)
       
       selenium_grid_hub=http://localhost:4444/wd/hub
       
Tag the tests with:

        @android-app
        @android-browser
        @ios-app


### **Install scripts (Deprecated but can be used at your own risk. Original made for a fresh machine with nothing pre installed)**
* If you are on linux you can use this script instead.
  Save it as a .sh and run bash <filename>.sh
      
    ```
    #!/bin/bash
    # Updating package index
    sudo -i apt-get update
    
    #installing java jdk
    printf "Installing jdk"
    sudo apt-get install default-jdk
                                        
    #Used to pull appium
    printf "Installing npm."
    sudo apt install nodejs-legacy
    
    # install all android sdk ect
    printf "Installing android-sdk."
    printf "Checking ~/Android exists"
    test -d ~/Android && echo "~/Android exists" ||mkdir ~/Android && cd ~/Android
    
    # download android sdk if needed
    test -e ./android-sdk_r24.2-linux.tgz && echo "Android sdk.tgz exists." || wget http://dl.google.com/android/android-sdk_r24.2-linux.tgz
    tar -xvf android-sdk_r24.2-linux.tgz
    
    #Change dir to update android sdk
    cd android-sdk-linux/tools
    sdkmanager "platform-tools"
    sdkmanager "platforms;android-26"
    
    #Add paths to $path
    bashrc=$(< ~/.bashrc);
    #setting java home in PATH
    javaH=$(readlink -f $(which java) | awk '{ print substr($1, 0, length($1)-4)}')
    if [[ "$bashrc" == *$javaH* ]];
        then
            printf "Java home already set.\n"
        else
            printf "Adding Java home.\n"
            echo "export JAVA_HOME=$javaH" >>~/.bashrc
            echo "export PATH=\$PATH:\${JAVA_HOME}bin/" >>~/.bashrc
    fi
    
    if [[ "$bashrc" == *"android-sdk"* ]];then
        echo "Android env var exist in PATH";
    else
        echo "Adding android env vars to PATH"
        echo "export ANDROID_HOME=\$HOME/Android/android-sdk-linux/" >>~/.bashrc
        echo "export PATH=\$PATH:\$ANDROID_HOME/platform-tools:\$ANDROID_HOME/tools:\$ANDROID_HOME/build-tools/22.0.1/" >>~/.bashrc
    fi
    
    # install adb dependancies
    sudo apt-get install libc6:i386 libstdc++6:i386
    # install aapt dependancies
    sudo apt-get install zlib1g:i386
    
    
    # Installing Appium doctor to check dependancies
    printf "\n>>>>>>>>>>>>>>          Installing Appium doctor to check dependancies\n"
    sudo npm install -g appium-doctor 
    
    source ~/.bashrc
    
    # Checking dependancies with Appium doctor
    #We cannot get the output from appium doctor, this will only appear in console for the user executing the script.
    appium-doctor
    
    # Installing Appium via npm
    read -r -p "Did appium doctor come back clean? [y/n] " response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]];
        then
            printf "\n>>>>>>>>>>>>>>          Installing Appium via npm\n"
            sudo npm install -g appium 
        else
            printf "Manually resolve appium dependancies and install appium using npm install -g appium.\n" && exit 1    
    fi
    
    #End / Fin
    ```
* If you are on macOS you can use this script after installing xcode. 
  Save it as a .sh and run bash <filename>.sh
      
    ```
   #!/bin/bash
    #
    # Check if Homebrew is installed
    #
    which -s brew
    if [[ $? != 0 ]] ; then
        # Install Homebrew
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        BREW_VERSION=$(brew -v | grep "Homebrew " | awk '{ print substr($2,  0, length($2))}');
        if [[ "$BREW_VERSION" != 1.* ]];
            then  printf "Check brew installed correctly, Exiting script." && exit 1;
        fi
    else
        printf "Updating Brew/Brew cask before proceeding."
        brew update  && brew cleanup && brew cask cleanup
    fi
    
    #
    #Installing java
    #
    brew cask install java
    
    #
    # Attempting carthage install, this has a dependancie on xcode 8.2 which cannot be installed via brew
    #
    printf "Installing Carthage."
    brew install carthage
    
    #
    # Installing appium dependancies
    #
    printf "\n>>>>>>>>>>>>>>          Installing grid dependancies"
    printf "Installing Node.\n"
    brew install node
    
    printf "Installing android-sdk."
    brew cask install android-sdk
    
    yes | sdkmanager --licenses
    sdkmanager "platform-tools"
    sdkmanager "platforms;android-25"
    sdkmanager "build-tools;26.0.1"
    sdkmanager "system-images;android-25;google_apis;x86"
    
    #
    # Configuring path in bash_profile
    #
    printf "\n>>>>>>>>>>>>>>          Configuring path in bash_profile"
    javaH="JAVA_HOME=\$(/usr/libexec/java_home)";
    androidH=$(brew cask info android-sdk | grep "android-sdk/" | awk 'NR==1{print $1}')
    printf "Adding entries into bash_profile."
    bashp=$(< ~/.bash_profile);
    if [[ "$bashp" == *$javaH* ]];
        then
            printf "Java home already set.\n"
        else
            printf "Adding Java home.\n"
            echo -e export "$javaH" >> ~/.bash_profile
    fi
    
    if [[ "$bashp" == *$androidH* ]];
        then
            printf "Android home already set."
        else
            printf "Adding android home."
            echo export "ANDROID_HOME=$androidH" >> ~/.bash_profile
    fi
    if [[ "$bashp" == *"$androidH/platform-tools"* ]];
        then
            printf "adb path already set.\n"
        else
            printf "Adding adb path.\n"
            echo export PATH="$androidH/platform-tools/":$PATH >> ~/.bash_profile
    fi
    sleep 2
    source ~/.bash_profile
    
    if [[ "$bashp" == *"${JAVA_HOME}/bin"* ]];
        then
            printf "Java_home/bin is already set in PATH."
        else
            printf "Adding Java_home/bin to PATH."
            echo export PATH=${JAVA_HOME}/bin:$PATH >> ~/.bash_profile
    fi
    
    sleep 2
    source ~/.bash_profile
    
    #
    # Testing paths added to bash_profile
    #
    printf "\n>>>>>>>>>>>>>>          Testing bash_profile for paths added"
    echo test "$JAVA_HOME" -d  && echo "Java_Home is set.\n" || echo "Java_Home was not set.";
    echo test [["$androidH" == "*$ANDROID_HOME*"]] && echo "Andoid_Home is Set.\n" || echo "Android_Home was not set.";
    
    #
    # Installing Appium doctor to check dependancies
    #
    printf "\n>>>>>>>>>>>>>>          Installing Appium doctor to check dependancies\n"
    npm install -g appium-doctor
    
    #
    # Checking dependancies with Appium doctor
    #We cannot get the output from appium doctor, this will only appear in console for the user executing the script.
    appium-doctor
    
    #
    # Installing Appium via npm
    #
    read -r -p "Did appium doctor come back clean? [y/n] " response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]];
        then
            printf "\n>>>>>>>>>>>>>>          Installing Appium via npm\n"
            npm install -g appium
        else
            printf "Manually resolve appium dependancies and install appium using npm install -g appium." && exit 1
    fi
    
    ```



        
        
