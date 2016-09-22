# coding=utf-8

from nzme_skynet.core.app import appbuilder

def before_all(context):
    """
    Set context variable for entire run
    Override userdata on CLI e.g. -D browserlocal=firefox
    Executed one in the beginning of entire test run
    TODO: Set logging
    TODO: Set allure reporting
    :param context: behave.runner.Context
    """
    context.local_browser_type = context.config.userdata.get("browserlocal", "chrome")
    context.base_url = context.config.userdata.get("baseurl", "http://live-nzherald.uatlbcf.apnnz.co.nz/")
    context.reuse = context.config.userdata.get("reusebrowser", False)


def after_all(context):
    """
    Executed at the end of the test run
    :param context: behave.runner.Context
    :return:
    """
    pass

def before_feature(context, feature):
    """
    Executed at the beginning of every feature file
    :param context: behave.runner.Context
    :param feature: behave.model.Feature
    """
    context.app = None

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
    TODO: Set log/screenshot folder
    TODO: Set allure test case
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    if context.app is None:
        try:
            context.app = appbuilder.build_desktop_browser(context.local_browser_type, context.base_url)
        except Exception:
            raise

def after_scenario(context, scenario):
    """
    Close app instance if not reused
    TODO: Take screen shot when test result is fail
    TODO: Stop allure test case
    :param context: behave.runner.Context
    :param scenario: behave.model.Scenario
    """
    if not context.reuse:
        try:
            context.app.quit()
        except Exception:
            raise
        context.app = None

def before_step(context, step):
    """
    TODO: Call allure reporting for every step
    :param context: behave.runner.Context
    :param step: behave.model.Step
    """
    pass

def after_step(context, step):
    """
    TODO: Perform screenshot with step name
    TODO: Stop allure step reporting
    :param context:
    :param step:
    :return:
    """
    pass
