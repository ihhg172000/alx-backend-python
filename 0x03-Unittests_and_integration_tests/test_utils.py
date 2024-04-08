#!/usr/bin/env python3
"""
test_utils.py
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test_access_nested_map """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", ), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        """ test_access_nested_map_exception """
        with self.assertRaisesRegex(KeyError, expected_msg):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_pyload, mock_get):
        """ test_get_json """
        mock_get.return_value.json.return_value = test_pyload

        response_json = utils.get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response_json, test_pyload)


if __name__ == "__main__":
    unittest.main()
