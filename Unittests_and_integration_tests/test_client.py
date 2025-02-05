#!/usr/bin/env python3
"""unittest for client"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
import requests
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        expected_url = "https://api.github.com/orgs/test_org/repos"
        mock_payload = {"repos_url": expected_url}

        with patch.object(
                GithubOrgClient,
                "org",
                new_callable=PropertyMock,
                return_value=mock_payload
                ):
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        expected_repos = ["repo1", "repo2"]

        mock_get_json.return_value = mock_repos_payload
        with patch.object(
                GithubOrgClient,
                "_public_repos_url",
                new_callable=PropertyMock,
                return_value="https://api.github.com/orgs/test_org/repos"
                ) as mock_url:
            client = GithubOrgClient("test_org")
            self.assertEqual(client.public_repos(), expected_repos)

            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
                )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        self.assertEqual(
            GithubOrgClient.has_license(
                repo,
                license_key
                ),
                expected
            )


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to start patching requests.get"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()
        
        def side_effect(url):
            if "orgs" in url:
                return unittest.mock.Mock(json=lambda: cls.org_payload)
            if "repos" in url:
                return unittest.mock.Mock(json=lambda: cls.repos_payload)
            return unittest.mock.Mock(json=lambda: {})
        
        cls.mock_get.side_effect = side_effect
    
    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
