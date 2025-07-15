from abc import ABC, abstractmethod

class FileTreeNavigator(ABC):
    """
    Interface for defining a strategy for traversing a file tree.
    Constructor is not defined here to allow for flexibility.
    Conforming objects need only expose the value of the root node,
    and a list of the root's children as other FileTreeNavigators

    Interface Contract:
    ```
    # Filetree root value
    @property
    def value(self) -> str:
        ...

    # Get list of root children as filetree navigators.
    def get_children(self) -> list[FileTreeNavigator]:
        ...
    ```
    """
    @property
    @abstractmethod
    def value(self) -> str:
        "Filetree root value."
        ...

    @abstractmethod
    def get_children(self) -> "list[FileTreeNavigator]":
        "Get list of root children as filetree navigators."
        ...