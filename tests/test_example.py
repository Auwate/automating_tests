"""
Testing suite
"""

import unittest
from automating_tests.backend.example import MyClass


class TestSuite(unittest.TestCase):
    """
    This test class checks the code of backend/example.py
    """

    def setUp(self) -> None:
        self.testing = MyClass()

    def test_setter(self) -> None:
        """
        Test that the setter works
        """
        self.testing.name = "Tyler"
        self.assertEqual(self.testing.name, "Tyler")

    def test_getter(self) -> None:
        """
        Test that the getter works
        """
        self.assertEqual(self.testing.name, "Austin")

    def test_to_string(self) -> None:
        """
        Test that the toString method works
        """
        self.assertEqual(self.testing.to_string(), "Hello, my name is Austin")
