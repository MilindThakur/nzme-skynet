# coding=utf-8
"""
This module abstract away the BDD hooks setup from test repo.
The setup is driven through config file which needs to be
implemented in the test repo.
Ref: https://github.com/oleg-toporkov/python-bdd-selenium.git
"""

import logging
import re

from allure.common import AllureImpl
from allure.constants import AttachmentType, Label
from allure.structure import TestLabel

from log import Logger
from nzme_skynet.core.app import appbuilder
from setupparser import Config


def before_all(context):
    """
    Set context variable for entire run
    Executed one in the beginning of entire test run
    :param context: behave.runner.Context
    """
    # These context variables can be overridden from command line
    if context.config.userdata:
        Config.BROWSER_NAME = context.config.userdata.get("type", Config.BROWSER_NAME)
        Config.BROWSER_OS = context.config.userdata.get("os", Config.BROWSER_OS)
        Config.BROWSER_VERSION = context.config.userdata.get("version", Config.BROWSER_VERSION)

        Config.ENV_IS_LOCAL = context.config.userdata.get("local", Config.ENV_IS_LOCAL)
        Config.ENV_BASE_URL = context.config.userdata.get("baseurl", Config.ENV_BASE_URL)

    Logger.configure_logging()
    logger = logging.getLogger(__name__)

    allure_report_path = '{}/allure_report'.format(Config.LOG)

    # Init allure
    try:
        context.allure = AllureImpl(allure_report_path)
    except Exception:
        logger.error('Failed to init allure at: {}'.format(allure_report_path))
        raise


# noinspection PyUnusedLocal
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
    logger = logging.getLogger(__name__)
    context.app = None
    context.picture_num = 0
    context.test_group = feature.name

    # Start the feature in allure reporting
    try:
        context.allure.start_suite(feature.name, feature.description,
                                   labels=[TestLabel(name=Label.FEATURE, value=feature.name)])
    except Exception:
        logger.error('Failed to init allure suite with name {}'.format(feature.name))
        raise


def after_feature(context, feature):
    """
    Executed at the end of each feature
    :param context: behave.runner.Context
    :param feature: behave.model.Feature
    """
    logger = logging.getLogger(__name__)

    # Stop the feature in allure reporting
    try:
        context.allure.stop_suite()
    except Exception:
        logger.error('Failed to stop allure suite with name {}'.format(feature.name))
        raise


def before_scenario(context, scenario):
    """
    Open app instance form a browser
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    logger = logging.getLogger(__name__)
    Logger.create_test_folder(scenario.name)

    # Start the scenario in allure reporting
    try:
        context.allure.start_case(scenario.name,
                                  labels=[TestLabel(name=Label.FEATURE, value=scenario.feature.name)])
    except Exception:
        logger.error('Failed to start init allure test with name {}'.format(scenario.name))
        raise

    context.test_name = scenario.name

    # cleanup app state for new test
    if context.app is not None:
        try:
            context.app.quit()
        except Exception:
            logger.error('Failed to stop browser instance')
            raise
        context.app = None

    # Build capabilities
    cap = {
        "browserName": Config.BROWSER_NAME,
        "platform": Config.BROWSER_OS,
        "version": '' if 'latest' in Config.BROWSER_VERSION else Config.BROWSER_VERSION
    }

    # Build the app instance
    if 'api' not in scenario.tags:
        try:
            if Config.ENV_IS_LOCAL:
                context.app = appbuilder.build_desktop_browser(Config.BROWSER_NAME, Config.ENV_BASE_URL)
            else:
                cap['group'] = context.test_group
                cap['name'] = context.test_name
                context.app = appbuilder.build_docker_browser(Config.SEL_GRID_URL, cap, Config.ENV_BASE_URL)
        except Exception, e:
            logger.exception(e)
            raise Exception("Failed to launch a browser")

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

            # Attach screen shot to allure reporting
            try:
                with open(_screenshot, 'rb') as _file:
                    context.allure.attach('{} fail'.format(scenario.name), _file.read(), AttachmentType.PNG)
            except Exception:
                logger.error('Failed to attach screenshot to report: {}'.format(_screenshot))
                raise

    # Add stack trace to allure reporting on failure
    try:
        _status = scenario.status
        if _status == 'skipped':
            _status = 'canceled'
        context.allure.stop_case(_status,
                                 getattr(context, 'last_error_message', None),
                                 getattr(context, 'last_traceback', None))
    except Exception:
        logger.error('Failed to stop allure test with name: {}'.format(scenario.name))
        raise

    if context.app:
        try:
            context.app.quit()
        except Exception:
            logger.error('Failed to stop browser instance {}'.format(Config.BROWSER_NAME))
            raise
        context.app = None

    logger.info('End of test: {}. Status {} !!!\n\n\n'.format(scenario.name, scenario.status.upper()))


def before_step(context, step):
    """
    Before step hook
    :param context: behave.runner.Context
    :param step: behave.model.Step

    """
    logger = logging.getLogger(__name__)

    # Start allure reporting for the step
    try:
        context.allure.start_step(step.name)
    except Exception:
        logger.error('Failed to init allure step with name: {}'.format(step.name))
        raise


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

        # Add screen shot for the step to allure reporting
        # noinspection PyBroadException
        try:
            with open(_screenshot, 'rb') as _file:
                context.allure.attach('{}_{}'.format(context.test_name, step.name), _file.read(), AttachmentType.PNG)
        except Exception:
            logger.error('Failed to attach to report screenshot: {}'.format(_screenshot))

    # Stop allure reporting for the step
    try:
        context.allure.stop_step()
    except Exception:
        logger.error('Failed to stop allure step with name: {}'.format(step.name))
        raise

    # Add stacktrace to allure reporting on failure
    if step.status.lower == 'failed':
        context.last_traceback = step.error_message
        try:
            context.last_error_message = step.error_message.split('ERROR:')[1]
        except IndexError:
            context.last_error_message = step.error_message
