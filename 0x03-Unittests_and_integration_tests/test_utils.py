#!/usr/bin/env python3
"""
test_utils.py
"""
import unittest
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


if __name__ == "__main__":
    unittest.main()
