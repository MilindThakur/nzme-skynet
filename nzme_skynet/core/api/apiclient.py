# -*- coding: utf-8 -*-

import logging
import requests
from nzme_skynet.core.api import helper
from nzme_skynet.core.api.resource import Resource
from requests.auth import HTTPBasicAuth

logger = logging.getLogger('ApiClient')


class InvalidUsage(Exception):
    pass


class ApiClient(object):
    """
    Wrapper class for requests library

    Example Usage:

        client = ApiClient(host="api.example.com")
        order = client.resource("/order")
        items = client.resource("/items")

        order.get(params={"type":"temp"})
        items.get()

        order.delete(path="/123")
        items.delete()


    :param host: Host url to send requests to
    :param http: optional, sets the http in url if not specified, default http
    :param persist_session: If session id to be maintained between requests, default True
    :param username: optional, username for basic auth
    :param password: optional, password for basic auth
    """

    def __init__(self,
                 host,
                 persist_session=True,
                 username=None,
                 password=None,
                 ssl=True):

        if host is None:
            raise InvalidUsage(
                "Must specify the 'host' url to send requests to")
        self._req = self._create_session(persist_session, username, password)
        self._base_url = helper.create_base_url(host, ssl)

    def _create_session(self, persist_session, username, password):
        """Creates session based request object if required
        :param persist_session: bool, if requests need to be persisted through a session
        :param username: username
        :param password: password
        :return: class: `Request <Request>` object
        """
        req = requests
        if persist_session:
            logger.debug('(CREATE SESSION)')
            req = requests.Session()
            req.auth = HTTPBasicAuth(username, password)
        return req

    def resource(self, uri, base_uri=None):
        """
        Create a new :class:`Resource' object

        :param uri: path to the uri
        :param base_uri: (optional), base uri
        :return: :class:`Resource` object
        """
        return Resource(
            uri=uri,
            base_uri=base_uri,
            base_url=self._base_url,
            req=self._req
        )
