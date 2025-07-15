from .filetree_navigator import FileTreeNavigator
from pathlib import Path

class FilesystemNavigator(FileTreeNavigator):
    path: Path

    def __init__(self, root_path: Path):
        self.path = root_path

    @property
    def value(self):
        return self.path.name
    
    def get_children(self) -> list[FileTreeNavigator]:
        if self.path.is_file(): return []
        return [FilesystemNavigator(child_path) for child_path in self.path.glob("*")]