#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json

class TestAccessNestedMap(unittest.TestCase):
    """ test for access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test that result is as expected """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ test access nested map with exception """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected)

class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        # Create mock response object
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
       
        # Patch requests.get to return our mock response
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value = mock_response
           
            # Call the function being tested
            result = utils.get_json(test_url)
           
            # Verify get was called exactly once with correct URL
            mock_get.assert_called_once_with(test_url)
           
            # Verify returned payload matches expected
            self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()

