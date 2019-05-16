# coding=utf-8
import requests
from requests.auth import HTTPBasicAuth
import logging

logger = logging.getLogger('ApiConnection')


class InvalidUsage(Exception):
    pass


class ApiConnection(object):
    """
    Wrapper class for requests library which manages requests session
    """

    def __init__(self, host_url, http=True, persist_session=True, username=None, password=None):
        """
        Request Client object
        :param host_url: Host url to send requests to
        :param http: optional, sets the http in url if not specified, default http
        :param persist_session: If session id to be maintained between requests, default True
        :param username: optional, username for basic auth
        :param password: optional, password for basic auth
        """
        if host_url is None:
            raise InvalidUsage(
                "Must specify the 'host' url to send requests to")
        if not 'http' in host_url or 'https' in host_url:
            if http:
                self._url = "http://" + host_url
            else:
                self._url = "https://" + host_url
        self._req = self._create_session(persist_session, username, password)

    def _create_session(self, persist_session, username, password):
        """
        Creates session based request object if required
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

    def reset_session(self):
        """
        Reset the active session to a new one
        :return: None
        """
        if isinstance(self._req, requests.Session):
            self._req = requests.Session()

    def get(self, uri, **kwargs):
        """
        Get request
        :param uri: relative url
        :param kwargs: optional parameters for request
        :return: class:`Response <Response>` object
        """
        return self._req.get(url=self._url+uri, **kwargs)

    def post(self, uri, **kwargs):
        """"
        Post request
        :param uri: relative url
        :param kwargs: optional parameters for request
        :return: class:`Response <Response>` object
        """
        return self._req.post(url=self._url+uri, **kwargs)

    def put(self, uri, **kwargs):
        """
        Put request
        :param uri: relative url
        :param kwargs: optional parameters for request
        :return: class:`Response <Response>` object
        """
        return self._req.put(url=self._url+uri, **kwargs)

    def patch(self, uri, **kwargs):
        """
        Patch request
        :param uri: relative url
        :param kwargs: optional parameters for request
        :return: class:`Response <Response>` object
        """
        return self._req.patch(url=self._url+uri, **kwargs)

    def delete(self, uri, **kwargs):
        """
        Delete request
        :param uri: relative url
        :param kwargs: optional parameters for request
        :return: class:`Response <Response>` object
        """
        return self._req.delete(url=self._url+uri, **kwargs)
