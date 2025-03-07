#!/usr/bin/env python3
"""unitest"""
import unittest
from unittest import mock
from parameterized import parameterized
import utils
from unittest.mock import patch, Mock
from functools import wraps


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
    """mock https test"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """mock https test"""
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


def memoize(fn):
    """Memoizes the result of the function to avoid re-execution."""
    cache_name = f"_{fn.__name__}_cache"

    @wraps(fn)
    def wrapper(self):
        if not hasattr(self, cache_name):
            result = fn(self)
            setattr(self, cache_name, result)
        return getattr(self, cache_name)
    return wrapper


class TestMemoize(unittest.TestCase):
    """Test class to verify the memoize decorator functionality."""
    def test_memoize(self):
        """Test the memoization behavior of the decorator."""
        class TestClass:
            def a_method(self):
                """Returns 42."""
                return 42

            @memoize
            def a_property(self):
                """Returns a_method."""
                return self.a_method()
        test_instance = TestClass()
        with mock.patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42
            result1 = test_instance.a_property()
            self.assertEqual(result1, 42)
            mock_method.assert_called_once()
            result2 = test_instance.a_property()
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
