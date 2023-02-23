#!/usr/bin/env python3
"""Parameterize a unit test	"""

from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
import unittest
from unittest.mock import patch


class estGithubOrgClient(unittest.TestCase):
    """Parameterize a unit test	"""

    @parameterized.expand([
        ('google', {'payload': True}),
        ('abc', {'payload': False})
    ])
    @patch('requests.get')
    def test_org(self, test_url, test_payload, mock):
        """Parameterize a unit test	"""
        mock.json.return_value = test_payload
        mock.return_value = mock
        self.assertEqual(get_json(test_url), test_payload)
