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
from nzme_skynet.core.app import appbuilder
from setupparser import Config


def before_all(context):
    """
    Set context variable for entire run
    Executed one in the beginning of entire test run
    :param context: behave.runner.Context
    """
    Logger.configure_logging()

    # These context variables can be overridden from command line
    if context.config.userdata:
        Config.BROWSER_OPTIONS['type'] = context.config.userdata.get("type", Config.BROWSER_OPTIONS['type'])
        Config.BROWSER_OPTIONS['os'] = context.config.userdata.get("os", Config.BROWSER_OPTIONS['os'])
        Config.BROWSER_OPTIONS['version'] = context.config.userdata.get("version", Config.BROWSER_OPTIONS['version'])

        Config.ENV_IS_LOCAL = context.config.userdata.getbool("local", Config.ENV_IS_LOCAL)
        Config.ENV_BASE_URL = context.config.userdata.get("baseurl", Config.ENV_BASE_URL)


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
    context.app = None
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
    if context.app is not None:
        try:
            context.app.quit()
        except Exception:
            logger.error('Failed to stop browser instance')
            raise
        context.app = None


    # Build the app instancetry:
    tags = str(context.config.tags)
    try:
        if 'api' not in tags:
            if 'mobile-android' in tags:
                context.app = appbuilder.build_appium_driver(Config.MOBILE_ANDROID_OPTIONS)
            elif 'mobile-ios' in tags:
                context.app = appbuilder.build_appium_driver(Config.MOBILE_IOS_OPTIONS)
            else:
                # this falls back into a generic browser as a default.
                # todo - expand for browser types chrome, firefox, safari ect
                if Config.ENV_IS_LOCAL:
                    context.app = appbuilder.build_desktop_browser(Config.BROWSER_OPTIONS, Config.ENV_BASE_URL)
                else:
                    # TODO - grab capabilities from a config
                    # TODO - push this down into the docker_browser builder
                    # Build capabilities
                    cap = {
                        "browserName": Config.BROWSER_OPTIONS['type'],
                        "platform": Config.BROWSER_OPTIONS['os'],
                        "version": '' if 'latest' in Config.BROWSER_OPTIONS['version'] else Config.BROWSER_OPTIONS[
                            'version']
                    }
                    cap['group'] = context.test_group
                    cap['name'] = context.test_name
                    context.app = appbuilder.build_docker_browser(Config.SEL_GRID_URL, cap, Config.ENV_BASE_URL)
    except Exception, e:
        logger.exception(e)
        raise Exception("Something broke creating a driver:" + e)

    logger.info('Start of Scenario: {}'.format(scenario.name))


def after_scenario(context, scenario):
    """
    Close app instance if not reused
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    logger = logging.getLogger(__name__)

    if context.app is not None:

        if scenario.status.lower == 'failed':
            _screenshot = '{}/{}_fail.png'.format(Config.LOG, scenario.name.replace(' ', '_'))

            # Take screen shot on a failure
            try:
                context.app.take_screenshot_current_window(_screenshot)
            except Exception:
                logger.error('Failed to take screenshot to: {}'.format(Config.LOG))
                raise

    if context.app:
        try:
            context.app.quit()
        except Exception:
            logger.error('Failed to stop browser instance {}'.format(Config.BROWSER_OPTIONS['type']))
            raise
        context.app = None

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
    if context.app is not None:
        try:
            context.app.take_screenshot_current_window(_screenshot)
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

