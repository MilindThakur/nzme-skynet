# -*- coding: utf-8 -*-


def create_base_url(host, use_ssl):
    """
    Concatenates host url with ssl use
    :return: (string) Base url
    """
    if use_ssl:
        return "https://%s" % host
    return "http://%s" % host


def create_resource_url(base_url, uri, base_uri):
    return "%(base_url)s%(full_path)s" % (
        {
            'base_url': base_url,
            'full_path': base_uri + uri
        }
    )
