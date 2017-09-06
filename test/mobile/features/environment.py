from nzme_skynet.core.bdd import basetest


def before_all(context):
    basetest.before_all(context)


def after_all(context):
    basetest.after_all(context)


def before_feature(context, feature):
    basetest.before_feature(context, feature)


def after_feature(context, feature):
    basetest.after_feature(context, feature)


def before_scenario(context, scenario):
    basetest.before_scenario(context, scenario)


def after_scenario(context, scenario):
    basetest.after_scenario(context, scenario)


def before_step(context, step):
    basetest.before_step(context, step)


def after_step(context, step):
    basetest.after_step(context, step)
