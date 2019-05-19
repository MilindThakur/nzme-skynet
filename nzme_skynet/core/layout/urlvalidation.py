# coding=utf-8
import itertools
import requests

from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes


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
    DriverRegistry.register_driver(DriverTypes.CHROMEHEADLESS, local=False)
    broken_images_list = _validate_images_on_url(
        url, DriverRegistry.get_webdriver())
    DriverRegistry.deregister_driver()
    return broken_images_list


def validate_links(url):
    DriverRegistry.register_driver(DriverTypes.CHROMEHEADLESS, local=False)
    broken_links_list = _validate_links_on_url(
        url,  DriverRegistry.get_webdriver())
    DriverRegistry.deregister_driver()
    return broken_links_list


def validate_js_error(url):
    DriverRegistry.register_driver(DriverTypes.CHROMEHEADLESS, local=False)
    js_errors = _validate_js_error_on_url(url, DriverRegistry.get_webdriver())
    DriverRegistry.deregister_driver()
    return js_errors


def validate_all(urls):
    DriverRegistry.register_driver(DriverTypes.CHROMEHEADLESS, local=False)
    errors = []
    list_urls = urls.split(',')
    for url in list_urls:
        DriverRegistry.get_webdriver().get(url)
        errors.append(_validate_images_on_url(
            url, DriverRegistry.get_webdriver(), open_url=False))
        errors.append(_validate_links_on_url(
            url, DriverRegistry.get_webdriver(), open_url=False))
        errors.append(_validate_js_error_on_url(
            url, DriverRegistry.get_webdriver(), open_url=False))
    DriverRegistry.deregister_driver()
    return list(itertools.chain.from_iterable(errors))
