#!/usr/bin/env python3
"""Parameterize a unit test	"""

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

    def test_public_repos_url(self):
        """Parameterize a unit test	"""
        test = GithubOrgClient('google')
        self.assertEqual(test._public_repos_url,
                         'https://api.github.com/orgs/google/repos')
