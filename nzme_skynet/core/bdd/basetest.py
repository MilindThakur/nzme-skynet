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
    # Setup the context variables from the config file
    if context.config.userdata:
        Config.BROWSER = context.config.userdata.get("browser", Config.BROWSER)
        Config.URL = context.config.userdata.get("url", Config.URL)
        Config.REUSE = context.config.userdata.get("reuse", Config.REUSE)
        Config.CLOUD = context.config.userdata.get("cloud", Config.CLOUD)

    Logger.configure_logging()
    logger = logging.getLogger(__name__)

    allure_report_path = '{}/allure_report'.format(Config.LOG)

    # Init allure
    try:
        context.allure = AllureImpl(allure_report_path)
    except Exception:
        logger.error('Failed to init allure at: {}'.format(allure_report_path))
        raise

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

    # Build the app instance
    if context.app is None:
        try:
            if not Config.CLOUD and not Config.API:
                context.app = appbuilder.build_desktop_browser(Config.BROWSER, Config.URL)
            if Config.API:
                context.baseuri = Config.BASEURI
        except Exception:
            logger.error('Failed to start browser instance: {}'.format(Config.BROWSER))
            raise
    logger.info('Start of Scenario: {}'.format(scenario.name))

def after_scenario(context, scenario):
    """
    Close app instance if not reused
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    logger = logging.getLogger(__name__)

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

    if not Config.REUSE:
        try:
            context.app.quit()
        except Exception:
            logger.error('Failed to stop browser instance {}'.format(Config.BROWSER))
            raise
        context.app = None

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
    try:
        if context.app is not None:
            context.app.take_screenshot_current_window(_screenshot)
            context.picture_num += 1
    except Exception:
        logger.error('Failed to take screenshot to: {}'.format(Config.LOG))
        logger.error('Screenshot name: {}'.format(step_name))
        raise

    # Add screen shot for the step to allure reporting
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
