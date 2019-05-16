# -*- coding: utf-8 -*-

import unittest
import requests
import httpretty
import json
from types import ModuleType

from nzme_skynet.core.api.apiclient import ApiClient


def get_serialized_result(dict_mock):
    return json.dumps({'result': dict_mock})


def get_serialized_error(dict_mock):
    return json.dumps({'error': dict_mock})


class ApiClientTest(unittest.TestCase):
    """
    Api Client unittests
    """

    def setUp(self):
        self.error_message_body = {
            'message': 'test_message',
            'detail': 'test_details'
        }
        self.create_record = {
            'id': '1',
            'title': 'foo_title',
            'author': 'bar_author'
        }
        self.updated_record = {
            'id': '1',
            'title': 'foo_title_updated',
            'author': 'bar_author_updated'
        }
        self.delete_record = {
            'status': 'record deleted'
        }
        self.record_list = [
            {
                'id': '1',
                'title': 'title_1',
                'author': 'author_1'
            },
            {
                'id': '2',
                'title': 'title_2',
                'author': 'author_2'
            }
        ]
        self.get_param = {'id': self.record_list[0]['id']}

        self.base_uri = "/api/1"
        self.uri = "/books"
        self.client_kwargs = {
            'host': 'mock_host',
            'username': 'test',
            'password': 'test'

        }
        self.resource_url = 'https://' + \
            self.client_kwargs['host'] + self.base_uri + self.uri
        self.client = ApiClient(**self.client_kwargs)

    def test_create_session_client(self):
        self.assertEqual(self.client._base_url,
                         ('https://' + self.client_kwargs['host']))
        self.assertEqual(type(self.client._req), requests.sessions.Session)

    def test_create_request_client(self):
        self.client_req = ApiClient('mock_host', persist_session=None)
        self.assertEqual(self.client_req._base_url, 'https://mock_host')
        self.assertEqual(type(self.client_req._req), ModuleType)

    def test_create_resource(self):
        r = self.client.resource(self.uri, self.base_uri)
        resource_repr = type(repr(r))
        self.assertEqual(resource_repr, str)
        self.assertEqual(r.resource_url, self.resource_url)

    @httpretty.activate
    def test_get(self):
        httpretty.register_uri(httpretty.GET,
                               self.resource_url,
                               body=get_serialized_result(self.create_record),
                               status=200,
                               content_type="application/json")
        r = self.client.resource(self.uri, self.base_uri).get(
            params=self.get_param)
        self.assertEqual(r.status_code, 200)
        r_json = json.loads(r.content)
        self.assertEqual(r_json['result']['id'], self.create_record['id'])
        self.assertEqual(r_json['result']['title'],
                         self.create_record['title'])
        self.assertEqual(r_json['result']['author'],
                         self.create_record['author'])

    @httpretty.activate
    def test_response(self):
        httpretty.register_uri(httpretty.GET,
                               self.resource_url,
                               status=200,
                               adding_headers={
                                   'test-1': 'foo', 'test-2': 'bar'},
                               content_type="application/json")
        response = self.client.resource(self.uri, self.base_uri).get()
        self.assertEqual(type(response), requests.Response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['test-1'], 'foo')
        self.assertEqual(response.headers['test-2'], 'bar')

    @httpretty.activate
    def test_http_error(self):
        httpretty.register_uri(httpretty.GET,
                               self.resource_url,
                               body=get_serialized_error(
                                   self.error_message_body),
                               status=400,
                               content_type="application/json")
        response = self.client.resource(self.uri, self.base_uri).get()
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_json['error']['message'], 'test_message')
        self.assertEqual(response_json['error']['detail'], 'test_details')

    @httpretty.activate
    def test_500_error(self):
        httpretty.register_uri(httpretty.GET,
                               self.resource_url,
                               status=500,
                               content_type="application/json")
        response = self.client.resource(self.uri, self.base_uri).get()
        self.assertEqual(response.status_code, 500)

    @httpretty.activate
    def test_post(self):
        httpretty.register_uri(httpretty.POST,
                               self.resource_url,
                               body=get_serialized_result(self.create_record),
                               status=200,
                               content_type="application/json")
        response = self.client.resource(self.uri, self.base_uri).post(
            data=json.dumps(self.create_record))
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['result']['title'], 'foo_title')
        self.assertEqual(response_json['result']['author'], 'bar_author')

    @httpretty.activate
    def test_put(self):
        httpretty.register_uri(httpretty.PUT,
                               self.resource_url + "/1",
                               body=get_serialized_result(self.updated_record),
                               status=200,
                               content_type="application/json")
        r = self.client.resource(self.uri, self.base_uri).put(
            path="/1", data=json.dumps(self.updated_record))
        self.assertEqual(r.status_code, 200)
        response_json = json.loads(r.content)
        self.assertEqual(response_json['result']
                         ['title'], self.updated_record['title'])

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(httpretty.GET,
                               self.resource_url,
                               body=get_serialized_result(self.create_record),
                               status=200,
                               content_type="application/json")

        httpretty.register_uri(httpretty.DELETE,
                               self.resource_url + "/1",
                               body=get_serialized_result(self.delete_record),
                               status=200,
                               content_type="application/json")
        resource = self.client.resource(self.uri, self.base_uri)
        response = resource.get()
        response_json = json.loads(response.content)
        new_path = "/{0}".format(response_json['result']['id'])
        response_1 = resource.delete(path=new_path)
        self.assertEqual(response_1.status_code, 200)
        response_1_json = json.loads(response_1.content)
        self.assertEqual(response_1_json['result']
                         ['status'], self.delete_record['status'])
