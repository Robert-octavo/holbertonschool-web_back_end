#!/usr/bin/env python3
"""Parameterize a unit test 
"""
from utils import access_nested_map, get_json, memoize
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
    def test_get_json(self, test_url, test_payload, mock):
        """Parameterize a unit test """
        mock.json.return_value = test_payload
        mock.return_value = mock
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Parameterize a unit test """

    def test_memoize(self):
        """Parameterize a unit test """
        class TestClass:
            """Parameterize a unit test """

            def a_method(self):
                """Parameterize a unit test """
                return 42

            @memoize
            def a_property(self):
                """Parameterize a unit test """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            obj = TestClass()
            obj.a_property
            obj.a_property
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
