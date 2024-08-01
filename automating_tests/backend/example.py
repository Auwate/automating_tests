"""
An example class tested through Tox
"""


class MyClass:
    """
    A basic class for testing purposes
    """

    def __init__(self) -> None:
        self._name = "Austin"

    @property
    def name(self):
        """Getter"""
        return self._name

    @name.setter
    def name(self, name):
        """Setter"""
        self._name = name

    def to_string(self) -> str:
        """A toString method"""
        return f"Hello, my name is {self.name}"
