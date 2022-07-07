import unittest
from tests import PluginTest
from plugins.cat_fact import cat_fact
from mock import patch, call
from unittest import mock
import requests

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({"fact": "test"}, 200)


class CatFactTest(PluginTest):
    """
    Tests For Cat Fact Plugin
    """

    def setUp(self):
        self.test = self.load_plugin(cat_fact)

    def test_main(self):
        with patch.object(requests, 'get') as get_mock:
            self.test(self.jarvis_api, "")
            get_mock.assert_called_with("https://catfact.ninja/fact")

    @mock.patch('plugins.cat_fact.requests.get', side_effect=mocked_requests_get)
    def test_response(self, mock_get):
        resp = self.test.run("")
        self.assertEqual(self.history_say().last_text(), "test")


if __name__ == '__main__':
    unittest.main()
