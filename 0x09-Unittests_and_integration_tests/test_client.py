#!/usr/bin/env python3
"""Parameterize a unit test	"""

from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize a unit test	"""

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, test_url, test_payload, mock):
        """Parameterize a unit test	"""
        mock.return_value = test_payload
        test = GithubOrgClient(test_url)
        self.assertEqual(test.org, test_payload)
        mock.assert_called_once()
