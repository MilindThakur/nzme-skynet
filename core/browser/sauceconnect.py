import os

selenium_host = "ondemand.saucelabs.com"
selenium_port = "80"


def getSauceUsername():
    return os.environ['SAUCE_USERNAME']


def getSauceAccessKey():
    return os.environ['SAUCE_ACCESS_KEY']


def constructRemoteCommandExecutor():
    print getSauceUsername()
    return "http://%s:%s@%s:%s/wd/hub" % \
           (getSauceUsername(),
            getSauceAccessKey(),
            selenium_host,
            selenium_port)
