# coding=utf-8
"""
This module abstract away the BDD hooks setup from test repo.
The setup is driven through config file which needs to be
implemented in the test repo.
Ref: https://github.com/oleg-toporkov/python-bdd-selenium.git
"""

import logging
import re
from log import Logger
from setupparser import Config

from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes


def before_all(context):
    """
    Set context variable for entire run
    Executed one in the beginning of entire test run
    :param context: behave.runner.Context
    """
    Logger.configure_logging()


def after_all(context):
    """
    Executed at the end of the test run
    :param context: behave.runner.Context
    """
    pass


def before_feature(context, feature):
    """
    Executed at the beginning of every feature file
    :param context: behave.runner.Context
    :param feature: behave.model.Feature
    """
    context.driver = None
    context.picture_num = 0
    context.test_group = feature.name


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
    logger = logging.getLogger(__name__)
    Logger.create_test_folder(scenario.name)

    context.test_name = scenario.name

    # cleanup app state for new test
    if DriverRegistry.get_driver() is not None:
        try:
            DriverRegistry.deregister_driver()
        except Exception:
            logger.error('Failed to stop browser instance')
            raise

    tags = str(context.scenario.tags)
    try:
        if 'api' not in tags:
            if 'android' in tags or 'ios' in tags:
                # Mobile tests
                if 'android-browser' in tags:
                    DriverRegistry.register_driver(
                        DriverTypes.ANDROIDWEB,
                        driver_options=Config.ANDROID_BROWSER_CAPABILITIES,
                        mbrowsername=context.config.userdata.get('androidBrowserName',
                                                                 Config.ANDROID_BROWSER_CAPABILITIES['browserName']))
                elif 'ios-browser' in tags:
                    DriverRegistry.register_driver(
                        DriverTypes.IOSWEB,
                        driver_options=Config.IOS_BROWSER_CAPABILITIES,
                        mbrowsername=context.config.userdata.get('iosBrowserName',
                                                                 Config.IOS_BROWSER_CAPABILITIES['browserName']))
                elif 'android-app' in tags:
                    DriverRegistry.register_driver(
                        DriverTypes.ANDROID,
                        driver_options=Config.ANDROID_APP_CAPABILITIES)
                elif 'ios-app' in tags:
                    DriverRegistry.register_driver(
                        DriverTypes.IOS,
                        driver_options=Config.IOS_APP_CAPABILITIES)
            else:
                # Desktop browser tests
                DriverRegistry.register_driver(
                    driver_type=context.config.userdata.get("type", Config.DESKTOP_BROWSER_CAPABILITIES['browserName']),
                    driver_options=Config.DESKTOP_BROWSER_CAPABILITIES,
                    local=context.config.userdata.getbool("local", Config.ENV_OPTIONS['local']))
                DriverRegistry.get_driver().baseurl = context.config.userdata.get("testurl", Config.ENV_OPTIONS['testurl'])
                DriverRegistry.get_driver().goto_url(DriverRegistry.get_driver().baseurl, absolute=True)
        context.driver = DriverRegistry.get_driver()
    except Exception as e:
        logger.exception(e)
        raise

    logger.info('Start of Scenario: {}'.format(scenario.name))


def after_scenario(context, scenario):
    """
    Close app instance if not reused
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    logger = logging.getLogger(__name__)

    if DriverRegistry.get_driver() is not None:

        if scenario.status.lower == 'failed':
            _screenshot = '{}/{}_fail.png'.format(Config.LOG, scenario.name.replace(' ', '_'))
            # Take screen shot on a failure
            try:
                DriverRegistry.get_driver().take_screenshot_current_window(_screenshot)
            except Exception:
                logger.error('Failed to take screenshot to: {}'.format(Config.LOG))
                raise

    if DriverRegistry.get_driver():
        try:
            DriverRegistry.deregister_driver()
        except Exception:
            logger.error('Failed to stop driver instance')
            raise
        context.driver = None

    logger.info('End of test: {}. Status {} !!!\n\n\n'.format(scenario.name, scenario.status.upper()))


def before_step(context, step):
    """
    Before step hook
    :param context: behave.runner.Context
    :param step: behave.model.Step

    """
    pass


def after_step(context, step):
    """
    After step hook
    :param context: behave.runner.Context
    :param step: behave.model.Step
    """
    logger = logging.getLogger(__name__)
    step_name = re.sub('[^A-Za-z0-9]+', '_', step.name)

    # TODO: Create screenshot filename
    _screenshot = '{}/{}/{}__{}__.png'.format(Config.LOG,
                                              context.test_name.replace(' ', '_'),
                                              context.picture_num,
                                              step_name)

    # Take screen shot
    # if step.status.lower == 'failed' or step.status.lower == 'skipped':
    if DriverRegistry.get_driver() is not None:
        try:
            DriverRegistry.get_driver().take_screenshot_current_window(_screenshot)
            context.picture_num += 1
        except Exception:
            logger.error('Failed to take screenshot to: {}'.format(Config.LOG))
            logger.error('Screenshot name: {}'.format(step_name))
            raise

    # Add stacktrace to allure reporting on failure
    if step.status.lower == 'failed':
        context.last_traceback = step.error_message
        try:
            context.last_error_message = step.error_message.split('ERROR:')[1]
        except IndexError:
            context.last_error_message = step.error_message
