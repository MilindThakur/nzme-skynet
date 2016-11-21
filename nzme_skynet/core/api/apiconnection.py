# coding=utf-8
import requests


class RestError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


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

    def get(self, uri, params=None, content_type="application/json"):
        if params is None:
            params = {}
        return self._request(uri, "GET", params=params, content_type=content_type)

    def post(self, uri, json=None, data=None, content_type="application/json"):
        return self._request(uri, "POST", json=json, data=data, content_type=content_type)

    def put(self, uri, json, content_type="application/json"):
        return self._request(uri, "PUT", json=json, content_type=content_type)

    def patch(self, uri, json, content_type="application/json"):
        return self._request(uri, "PATCH", json=json, content_type=content_type)

    def delete(self, uri):
        return self._request(uri, "DELETE")

    def _request(self, uri, method, params=None, json=None, data=None, content_type=None):
        h = self._create_connection_url()
        r = requests.request(method=method, url=h + uri, params=params, json=json, data=data,
                             headers=self._build_header(content_type))
        return r
