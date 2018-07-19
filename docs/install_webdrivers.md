## Installing Chromedriver (chrome), Geckodriver (firefox) drivers

**Ubuntu**:

Chromedriver (Chrome):

    sudo apt-get install unzip
    LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
    wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver
    sudo mv -f chromedriver /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    rm chromedriver_linux64.zip
    
Geckodriver (Firefox):

    LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json' https://github.com/mozilla/geckodriver/releases/latest)
    LATEST_VERSION=$(echo $LATEST_RELEASE | sed -e 's/.*"tag_name":"\([^"]*\)".*/\1/')
    LATEST_DRIVER="geckodriver-$LATEST_VERSION-linux64.tar.gz"
    wget https://github.com/mozilla/geckodriver/releases/download/$LATEST_VERSION/$LATEST_DRIVER
    tar -xvzf $LATEST_DRIVER
    chmod +x geckodriver
    sudo mv -f geckodriver /usr/local/share/geckodriver
    sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver
    sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver
    rm $LATEST_DRIVER


**Mac**:

    brew install chromedriver
    brew upgrade chomedriver
    
    brew install geckodriver
    brew upgrade geckodriver
    
**Verify drivers**:

Verify chromedriver: Should open, goto url and close chrome browser

    python
    >>> from selenium import webdriver
    >>> browser = webdriver.Chrome()
    >>> browser.get("https://www.google.co.nz") 
    >>> browser.close()
    >>> exit()
    
Verify geckodriver: Should open, goto url and close firefox browser

    python
    >>> from selenium import webdriver
    >>> browser = webdriver.Firefox()
    >>> browser.get("https://www.google.co.nz")
    >>> browser.close()
    >>> exit()