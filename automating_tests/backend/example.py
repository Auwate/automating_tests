class MyClass:

    def __init__(self) -> None:
        self._name = "Austin"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
