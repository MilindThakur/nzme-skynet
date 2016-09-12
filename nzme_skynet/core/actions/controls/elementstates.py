# coding=utf-8
from selenium.webdriver.common.by import By

import nzme_skynet.core.utils.timeouts as timeout


def is_visible(driver, selector, by=By.CSS_SELECTOR, time=timeout.DEFAULT_TIMEOUT):
    pass


def is_ready_to_interact_with(driver, selector, by=By.CSS_SELECTOR):
    pass


def will_be_ready_to_interact(driver, selector, by=By.CSS_SELECTOR):
    pass


def will_be_ready_to_interact_in_time(driver, selector, time, by=By.CSS_SELECTOR):
    pass


def is_present(driver, selector, by=By.CSS_SELECTOR):
    pass


def will_be_present(driver, selector, by=By.CSS_SELECTOR):
    pass


def will_be_present_in_time(driver, selectr, by=By.CSS_SELECTOR):
    pass
