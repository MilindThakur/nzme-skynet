# coding=utf-8

from nzme_skynet.core.app import appbuilder

def before_all(context):
    local_browser_type = context.config.userdata.get("browserlocal")
    base_url = context.config.userdata.get("baseurl")
    context.app = appbuilder.build_desktop_browser(local_browser_type, base_url)

def after_all(context):
    context.app.quit()