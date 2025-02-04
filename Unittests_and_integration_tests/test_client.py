#!/usr/bin/env python3
"""unittest for client"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_result = {"some": "data"}  # Mocked API response
        mock_get_json.return_value = expected_result
        
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)
        
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        expected_url = "https://api.github.com/orgs/test_org/repos"
        mock_payload = {"repos_url": expected_url}
        
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock, return_value=mock_payload):
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, expected_url)


if __name__ == "__main__":
    unittest.main()