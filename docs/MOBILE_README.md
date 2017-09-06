# **Skynet - Test Automation Library @ NZME - Mobile**

## **Features included:**
* Android mobile app
* Android web (chrome)
* ios(Coming soon)
* ios web (safari)(Coming soon)

## **Setup instructions**
This is a supplimentry to guide the the [Skynet Readme](../README.md)

### **Local install (non docker)** 
* If you plan to run mobile tests within docker (Android only support), the containers will spawn with the docker_compose.sh start command.
  The containers are defined in the docker-compose.yml found within the project directory.

### **Manual install**
* Follow this [handy guide](https://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial) from android central.
* If you are running on linux you need to install some extra 32bit libraries. 
    ```bash
    sudo apt-get install zlib1g:i386 libc6:i386 libstdc++6:i386
    ```
* Install appium using npm, a [Guide can be found here](https://www.npmjs.com/package/appium)

### **Install script**
* If you are on linux you can use this scripts instead.
  Save it as a .sh and run bash <filename>.sh
      
    ```bash
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
