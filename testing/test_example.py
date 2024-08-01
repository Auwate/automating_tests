import unittest
from ..automating_tests.backend.example import MyClass


class TestSuite(unittest.TestCase):

    def test_setter(self) -> None:
        testing = MyClass()
        testing.name = "Tyler"
        self.assertEqual(testing.name, "Tyler")

    def test_getter(self) -> None:
        testing = MyClass()
        self.assertEqual(testing.name, "Austin")
