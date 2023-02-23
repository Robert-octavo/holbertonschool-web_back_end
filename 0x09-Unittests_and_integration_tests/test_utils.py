#!/usr/bin/env python3
"""Parameterize a unit test 
"""
from utils import access_nested_map, get_json
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Parameterize a unit test """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Parameterize a unit test """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Parameterize a unit test """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload):
        """Parameterize a unit test """
        mock.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)


if __name__ == '__main__':
    unittest.main()
