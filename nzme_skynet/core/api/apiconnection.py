# coding=utf-8
import requests


class RestError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


# noinspection PyMethodMayBeStatic
class ApiConnection(object):
    def __init__(self, host_url, http=True):
        self.use_http = http
        self.host = host_url

    def _create_connection_url(self):
        if self.use_http:
            return "http://" + self.host
        else:
            return "https://" + self.host

    def _build_header(self, content_type):
        header = {"Accept": "application/json"}
        if content_type != "":
            header["Content-type"] = content_type
        return header

    def get(self, uri, params=None):
        if params is None:
            params = {}
        return self._request(uri, "GET", params=params)

    def post(self, uri, json=None):
        if json is not None:
            return self._request(uri, "POST", json=json)
        else:
            return self._request(uri, "POST")

    def put(self, uri, json):
        return self._request(uri, "PUT", json=json)

    def patch(self, uri, json):
        return self._request(uri, "PATCH", json=json)

    def delete(self, uri):
        return self._request(uri, "DELETE")

    def _request(self, uri, method, params=None, json=None, content_type="application/json"):
        h = self._create_connection_url()
        r = requests.request(method=method, url=h + uri, params=params, body=json,
                             headers=self._build_header(content_type))
        return r
