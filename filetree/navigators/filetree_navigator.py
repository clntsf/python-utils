from abc import ABC, abstractmethod

class FileTreeNavigator(ABC):

    @property
    @abstractmethod
    def value(self) -> str:
        """
        Get filetree root value.
        """
        ...

    @abstractmethod
    def get_children(self) -> "list[FileTreeNavigator]":
        """
        Get list of root children as filetree navigators
        """
        ...