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

    def get(self, uri, params=None):
        if params is None:
            params = {}
        return self._request(uri, "GET", params=params)

    def post(self, uri, json=None):
        if json is not None:
            return self._request(uri, "POST", body=json)
        else:
            return self._request(uri, "POST")

    def put(self, uri, json):
        return self._request(uri, "PUT", body=json)

    def patch(self, uri, json):
        return self._request(uri, "PATCH", body=json)

    def delete(self, uri):
        return self._request(uri, "DELETE")

    def _request(self, uri, method, params=None, body=None, content_type="application/json"):
        h = self._create_connection_url()
        r = requests.request(method=method, url=h + uri, params=params, body=body,
                             headers=self._build_header(content_type))
        if r.status_code == requests.codes.NO_CONTENT:
            return {}
        r_json_body = r.json()
        return r_json_body
