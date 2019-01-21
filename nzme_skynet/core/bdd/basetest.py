# coding=utf-8
"""
This module abstract away the BDD hooks setup from test repo.
The setup is driven through config file which needs to be
implemented in the test repo.
Ref: https://github.com/oleg-toporkov/python-bdd-selenium.git
"""

import logging
import re
from nzme_skynet.core.utils.log import Logger
from setupparser import Config
from behave.model_core import Status
import allure
from allure_commons.types import AttachmentType

from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
logger = logging.getLogger(__name__)


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
    Logger.create_test_folder(scenario.name)

    context.test_name = scenario.name

    # Accommodate for overriding config settings in CLI
    context.browser_name = context.config.userdata.get('browserName', Config.BROWSER_CAPABILITIES['browserName'])
    context.test_url = context.config.userdata.get('testurl', Config.ENV_OPTIONS['testurl'])
    context.is_local = context.config.userdata.getbool("local", Config.ENV_OPTIONS['local'])
    context.grid_url = context.config.userdata.get('selenium_grid_hub', Config.ENV_OPTIONS['selenium_grid_hub'])
    context.is_zalenium = context.config.userdata.getbool('zalenium', Config.ENV_OPTIONS['zalenium'])
    if 'build' in context.config.userdata.keys():
        Config.BROWSER_CAPABILITIES['build'] = context.config.userdata['build']

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
                        capabilities=Config.ANDROID_CAPABILITIES,
                        grid_url=Config.ENV_OPTIONS['selenium_grid_hub'])
                elif 'ios-browser' in tags:
                    context.driver = DriverRegistry.register_driver(
                        DriverTypes.IOSWEB,
                        capabilities=Config.IOS_CAPABILITIES,
                        grid_url=Config.ENV_OPTIONS['selenium_grid_hub'])
                elif 'android-app' in tags:
                    context.driver = DriverRegistry.register_driver(
                        DriverTypes.ANDROID,
                        capabilities=Config.ANDROID_CAPABILITIES,
                        grid_url=Config.ENV_OPTIONS['selenium_grid_hub'])
                elif 'ios-app' in tags:
                    context.driver = DriverRegistry.register_driver(
                        DriverTypes.IOS,
                        capabilities=Config.IOS_CAPABILITIES,
                        grid_url=Config.ENV_OPTIONS['selenium_grid_hub'])
                else:
                    logger.exception("Only supports tags android-app, android-browser, ios-app, ios-browser")
                    raise Exception("Only supports tags android-app, android-browser, ios-app, ios-browser")
            else:
                # Desktop browser tests
                # Add Feature and Scenario name for grouping Zalenium Test
                # https://github.com/zalando/zalenium/blob/master/docs/usage_examples.md#test-name
                if not context.is_local and context.is_zalenium:
                    Config.BROWSER_CAPABILITIES['name'] = context.test_name
                context.driver = DriverRegistry.register_driver(
                    driver_type=context.browser_name,
                    capabilities=Config.BROWSER_CAPABILITIES,
                    local=context.is_local,
                    grid_url=context.grid_url)
            context.driver.baseurl = context.test_url
    except Exception as e:
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
            _screenshot = '{}/{}_fail.png'.format(Config.LOG, scenario.name.replace(' ', '_'))
            # Take screen shot on a failure
            try:
                context.driver.take_screenshot_current_window(_screenshot)
            except Exception:
                logger.debug('Failed to take screenshot to: {}'.format(Config.LOG))
                pass
            # https://github.com/zalando/zalenium/blob/master/docs/usage_examples.md#marking-the-test-as-passed-or-failed
            if context.is_zalenium:
                try:
                    context.driver.add_cookie({
                        'name': 'zaleniumTestPassed',
                        'value': 'false'
                    })
                except Exception:
                    logger.debug('Failed to set failed cookie for scenario in Zalenium')
                    pass

        # https://github.com/zalando/zalenium/blob/master/docs/usage_examples.md#marking-the-test-as-passed-or-failed
        if scenario.status == Status.passed and context.is_zalenium:
            try:
                context.driver.add_cookie({
                    'name': 'zaleniumTestPassed',
                    'value': 'true'
                })
            except Exception:
                logger.debug('Failed to set passed cookie for scenario in Zalenium')
                pass

    if context.driver:
        try:
            DriverRegistry.deregister_driver()
            context.driver = None
        except Exception:
            logger.exception('Failed to stop driver instance')
            raise

    logger.info('End of test: {}. Status {} !!!\n\n\n'.format(scenario.name, scenario.status.name.upper()))


def before_step(context, step):
    """
    Before step hook
    :param context: behave.runner.Context
    :param step: behave.model.Step

    """
    if context.driver is not None and context.is_zalenium:
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
    _screenshot = '{}/{}/{}__{}__.png'.format(Config.LOG,
                                              context.test_name.replace(' ', '_'),
                                              context.picture_num,
                                              step_name)

    # Take screen shot
    # if step.status == Status.failed or step.status == Status.skipped:
    if context.driver is not None:
        try:
            context.driver.take_screenshot_current_window(_screenshot)
            context.picture_num += 1
        except Exception:
            logger.debug('Failed to take screenshot to: {}'.format(Config.LOG))
            pass
    try:
        with open(_screenshot, 'rb') as _file:
            allure.attach(_file.read(), name='{}_{}'.format(context.test_name, step.name), attachment_type=AttachmentType.PNG)
    except Exception:
        logger.error('Failed to attach to report screenshot: {}'.format(_screenshot))