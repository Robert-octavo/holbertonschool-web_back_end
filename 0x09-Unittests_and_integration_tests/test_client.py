#!/usr/bin/env python3
"""Parameterize a unit test	"""

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
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

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google/repos'}),
        ('abc', {'repos_url': 'https://api.github.com/orgs/abc/repos'}),
    ])
    @patch('client.get_json')
    def test_public_repos(self, test_url, test_payload, mock):
        """Parameterize a unit test	"""
        mock.return_value = test_payload
        test = GithubOrgClient(test_url)
        self.assertEqual(test._public_repos_url,
                         test_payload['repos_url'])
        self.assertEqual(test.public_repos(), mock.return_value)
        mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Parameterize a unit test	"""
        test = GithubOrgClient('google')
        self.assertEqual(test.has_license(repo, license_key), expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'))
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Parameterize a unit test	"""

    @classmethod
    def setUpClass(cls):
        """Parameterize a unit test	"""
        cls.get_patcher = patch('client.get_json')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Parameterize a unit test	"""
        cls.get_patcher.stop()
