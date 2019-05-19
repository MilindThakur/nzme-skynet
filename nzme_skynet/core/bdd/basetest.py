# coding=utf-8
"""
This module abstract away the BDD hooks setup from test repo.
The setup is driven through config file which needs to be
implemented in the test repo.
Ref: https://github.com/oleg-toporkov/python-bdd-selenium.git
"""

import logging
import re
import ast
import os
try:
    import configparser
except:
    import ConfigParser as configparser
from nzme_skynet.core.utils.log import Logger
from behave.model_core import Status
import allure
from allure_commons.types import AttachmentType
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.controls import set_highlight

logger = logging.getLogger(__name__)


def before_all(context):
    """
    Set context variable for entire run
    Executed one in the beginning of entire test run
    :param context: behave.runner.Context
    """
    Logger.configure_logging()
    userdata = context.config.userdata
    configfile = userdata.get("configfile", "testsetup.ini")
    parser = configparser.SafeConfigParser(allow_no_value=True)
    parser.read(configfile)

    if parser.has_section("BROWSER"):
        context.options = {}
        context.browser_capabilities = ast.literal_eval(
            parser.get("BROWSER", 'capabilities'))
        # Update user specified browser capabilities from CLI
        for key in userdata:
            if key in context.browser_capabilities:
                context.browser_capabilities[key] = userdata[key]
        # Parse framework specific configuration options
        # Set global highlight state
        set_highlight(userdata.getbool(
            "highlight", parser.getboolean("BROWSER", "highlight")))
        context.options["resolution"] = userdata.get(
            "resolution", parser.get('BROWSER', 'resolution'))
        context.options["headless"] = userdata.getbool(
            "headless", parser.getboolean("BROWSER", "headless"))
        context.options["mobileEmulation"] = userdata.get(
            "mobileEmulation", parser.get("BROWSER", "mobileEmulation"))
        logger.debug("Created browser capability {0}".format(
            context.browser_capabilities))
    if parser.has_section("ANDROID"):
        context.android_capabilities = ast.literal_eval(
            parser.get("ANDROID", "capabilities"))
        logger.debug("Created android capability {0}".format(
            context.android_capabilities))
    if parser.has_section("IOS"):
        context.ios_capabilities = ast.literal_eval(
            parser.get("IOS", "capabilities"))
        logger.debug("Created ios capability {0}".format(
            context.ios_capabilities))
    if parser.has_section("ENVIRONMENT"):
        context.testurl = userdata.get(
            "testurl", parser.get("ENVIRONMENT", "testurl"))
        context.local = userdata.getbool(
            "local", parser.getboolean("ENVIRONMENT", "local"))
        context.selenium_grid_hub = userdata.get(
            "selenium_grid_hub", parser.get("ENVIRONMENT", "selenium_grid_hub"))
        context.zalenium = userdata.getbool(
            "zalenium", parser.getboolean("ENVIRONMENT", "zalenium"))
    context.log = os.path.abspath('logs')


def after_all(context):
    """
    Executed at the end of the test run
    :param context: behave.runner.Context
    """
    set_highlight(False)


def before_feature(context, feature):
    """
    Executed at the beginning of every feature file
    :param context: behave.runner.Context
    :param feature: behave.model.Feature
    """
    context.driver = None
    context.picture_num = 0
    context.test_group = feature.name
    # Retry scenarios tagged with @autoretry
    for scenario in feature.scenarios:
        if "autoretry" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=2)


def after_feature(context, feature):
    """
    Executed at the end of each feature
    :param context: behave.runner.Context
    :param feature: behave.model.Feature
    """
    pass


def before_scenario(context, scenario):
    """
    Open app instance form a browser
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    Logger.create_test_folder(scenario.name)
    context.test_name = scenario.name
    # cleanup app state for new test
    if context.driver is not None:
        try:
            DriverRegistry.deregister_driver()
            context.driver = None
        except Exception:
            logger.exception('Failed to stop browser instance')
            raise

    tags = str(context.config.tags)
    try:
        logger.debug("Building driver..")
        if 'api' not in tags:
            if 'android' in tags or 'ios' in tags:
                # Mobile tests
                if 'android-browser' in tags:
                    context.driver = DriverRegistry.register_driver(
                        DriverTypes.ANDROIDWEB,
                        capabilities=context.android_capabilities,
                        grid_url=context.selenium_grid_hub)
                elif 'ios-browser' in tags:
                    context.driver = DriverRegistry.register_driver(
                        DriverTypes.IOSWEB,
                        capabilities=context.ios_capabilities,
                        grid_url=context.selenium_grid_hub)
                elif 'android-app' in tags:
                    context.driver = DriverRegistry.register_driver(
                        DriverTypes.ANDROID,
                        capabilities=context.android_capabilities,
                        grid_url=context.selenium_grid_hub)
                elif 'ios-app' in tags:
                    context.driver = DriverRegistry.register_driver(
                        DriverTypes.IOS,
                        capabilities=context.ios_capabilities,
                        grid_url=context.selenium_grid_hub)
                else:
                    logger.exception(
                        "Only supports tags @android-app, @android-browser, @ios-app, @ios-browser")
                    raise Exception(
                        "Only supports tags @android-app, @android-browser, @ios-app, @ios-browser")
            else:
                # Desktop browser tests
                # Add Feature and Scenario name for grouping Zalenium Test
                # https://github.com/zalando/zalenium/blob/master/docs/usage_examples.md#test-name
                if not context.local and context.zalenium:
                    context.browser_capabilities['name'] = context.test_name
                DriverRegistry.register_driver(
                    driver_type=context.browser_capabilities['browserName'],
                    capabilities=context.browser_capabilities,
                    local=context.local,
                    grid_url=context.selenium_grid_hub, options=context.options)
            context.driver = DriverRegistry.get_driver()
            context.driver.baseurl = context.testurl
    except Exception:
        logger.exception("Failed building the driver")
        raise

    logger.info('Start of Scenario: {}'.format(scenario.name))


def after_scenario(context, scenario):
    """
    Close app instance if not reused
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    if context.driver is not None:

        if scenario.status == Status.failed:
            _screenshot = '{}/{}_fail.png'.format(
                context.log, scenario.name.replace(' ', '_'))
            # Take screen shot on a failure
            try:
                context.driver.take_screenshot_current_window(_screenshot)
            except Exception:
                logger.debug(
                    'Failed to take screenshot to: {}'.format(context.log))
                pass
            # https://github.com/zalando/zalenium/blob/master/docs/usage_examples.md#marking-the-test-as-passed-or-failed
            if context.zalenium:
                try:
                    context.driver.add_cookie({
                        'name': 'zaleniumTestPassed',
                        'value': 'false'
                    })
                except Exception:
                    logger.debug(
                        'Failed to set failed cookie for scenario in Zalenium')
                    pass

        # https://github.com/zalando/zalenium/blob/master/docs/usage_examples.md#marking-the-test-as-passed-or-failed
        if scenario.status == Status.passed and context.zalenium:
            try:
                context.driver.add_cookie({
                    'name': 'zaleniumTestPassed',
                    'value': 'true'
                })
            except Exception:
                logger.debug(
                    'Failed to set passed cookie for scenario in Zalenium')
                pass

    if context.driver:
        try:
            DriverRegistry.deregister_driver()
            context.driver = None
        except Exception:
            logger.exception('Failed to stop driver instance')
            raise

    logger.info('End of test: {}. Status {} !!!\n\n\n'.format(
        scenario.name, scenario.status.name.upper()))


def before_step(context, step):
    """
    Before step hook
    :param context: behave.runner.Context
    :param step: behave.model.Step

    """
    if context.driver is not None and context.zalenium:
        try:
            context.driver.add_cookie({
                'name': 'zaleniumMessage',
                'value': step.name.replace(' ', '_')
            })
        except Exception:
            logger.debug('Failed to set cookie for test step in Zalenium')
            pass


def after_step(context, step):
    """
    After step hook
    :param context: behave.runner.Context
    :param step: behave.model.Step
    """
    step_name = re.sub('[^A-Za-z0-9]+', '_', step.name)

    # TODO: Create screenshot filename
    _screenshot = '{}/{}/{}__{}__.png'.format(context.log,
                                              context.test_name.replace(
                                                  ' ', '_'),
                                              context.picture_num,
                                              step_name)

    # Take screen shot
    # if step.status == Status.failed or step.status == Status.skipped:
    if context.driver is not None:
        try:
            context.driver.take_screenshot_current_window(_screenshot)
            context.picture_num += 1
        except Exception:
            logger.debug(
                'Failed to take screenshot to: {}'.format(context.log))
            pass
    try:
        with open(_screenshot, 'rb') as _file:
            allure.attach(_file.read(), name='{}_{}'.format(context.test_name, step.name),
                          attachment_type=AttachmentType.PNG)
    except Exception:
        logger.error(
            'Failed to attach to report screenshot: {}'.format(_screenshot))
