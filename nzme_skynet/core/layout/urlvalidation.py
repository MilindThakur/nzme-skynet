# coding=utf-8
import itertools
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder


def create_webdriver_instance():
    capabilities = DesiredCapabilities.PHANTOMJS
    capabilities['loggingPrefs'] = {'browser': 'ALL'}
    lb = LocalBrowserBuilder("phantomJS", desCap=capabilities)
    browser = lb.build()
    return browser.driver

def validate_url(url, driver):
    result = driver.current_url
    if url in result:
        return True
    else:
        return False

def _validate_images_on_url(url, driver, open_url=True):
    broken_images_list = []
    if open_url:
        driver.get(url)
    if validate_url(url, driver):
        images = driver.find_elements_by_tag_name("img")
        for image in images:
            b = driver.execute_script("return arguments[0].complete && "
                                      "typeof arguments[0].naturalWidth != \"undefined\" && "
                                      "arguments[0].naturalWidth > 0", image)
            if not b:
                broken_images_list.append(image.get_attribute("src"))
        return broken_images_list
    else:
        return Exception("Invalid URL used - please try again")

def _validate_links_on_url(url, driver, open_url=True):
    broken_links_list = []
    if open_url:
        driver.get(url)
    if validate_url(url, driver):
        links = driver.find_elements_by_xpath("//a[@href]")
        for link in links:
            if link.is_displayed() and ("http" in link.get_attribute("href")):
                if not (requests.get(link.get_attribute("href")).status_code == 200):
                    broken_links_list.append(link.text)
        return broken_links_list
    else:
        return Exception("Invalid URL used - please try again")

def _validate_js_error_on_url(url, driver, open_url=True):
    js_error = []
    log_level = ['WARNING', 'SEVERE', 'FATAL', 'ERROR']
    if open_url:
        driver.get(url)
    if validate_url(url, driver):
        errors = driver.get_log('browser')
        for entry in errors:
            if entry['level'] in log_level:
                js_error.append(str(entry['level'] + ": " + entry['message']))
        return js_error
    else:
        return Exception("Invalid URL used - please try again")

def validate_images(url):
    driver = create_webdriver_instance()
    return _validate_images_on_url(url, driver)

def validate_links(url):
    driver = create_webdriver_instance()
    return _validate_links_on_url(url, driver)

def validate_js_error(url):
    driver = create_webdriver_instance()
    return _validate_js_error_on_url(url, driver)

def validate_all(url):
    driver = create_webdriver_instance()
    errors = []
    driver.get(url)
    errors.append(_validate_images_on_url(url, driver, open_url=False))
    errors.append(_validate_links_on_url(url, driver, open_url=False))
    errors.append(_validate_js_error_on_url(url, driver, open_url=False))
    return list(itertools.chain.from_iterable(errors))

# def validate_all(url):
#     driver = create_webdriver_instance()
#     errors = []
#     driver.get(url)
#     errors.append(_validate_images_on_url(url, driver, open_url=False))
#     errors.append(_validate_links_on_url(url, driver, open_url=False))
#     errors.append(_validate_js_error_on_url(url, driver, open_url=False))
#     return list(itertools.chain.from_iterable(errors))