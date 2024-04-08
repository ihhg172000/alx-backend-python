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


class TestMemoize(unittest.TestCase):
    """
    TestMemoize
    """
    def test_memoize(self):
        """ test_memoize """
        class TestClass:
            """
            TestClass
            """
            def a_method(self):
                """ a_method """
                return 42

            @utils.memoize
            def a_property(self):
                """ a_property """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            mock_return_value = 10
            mock_method.return_value = mock_return_value

            test_instance = TestClass()

            self.assertEqual(test_instance.a_property, mock_return_value)
            self.assertEqual(test_instance.a_property, mock_return_value)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
