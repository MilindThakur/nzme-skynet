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

    def get(self, uri, params=None, headers=None, auth=None):
        return self._request(uri, "GET", params=params, headers=headers, auth=auth)

    def post(self, uri, params=None, json=None, data=None, headers=None):
        return self._request(uri, "POST", params=params, json=json, data=data, headers=headers)

    def put(self, uri, json, headers=None):
        return self._request(uri, "PUT", json=json, headers=headers)

    def patch(self, uri, json, headers=None):
        return self._request(uri, "PATCH", json=json, headers=headers)

    def delete(self, uri, json=None, headers=None):
        return self._request(uri, "DELETE", json=json, headers=headers)

    def _request(self, uri, method, params=None, json=None, data=None, headers=None, auth=None):
        h = self._create_connection_url()
        return requests.request(method=method, url=h + uri, params=params, json=json, data=data, headers=headers, auth=auth)
