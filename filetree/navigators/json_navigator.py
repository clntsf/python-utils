from .filetree_navigator import FileTreeNavigator

SAMPLE_JSON_TREE = {
    "alice": {
        "charlie": {
            "dog": None,    # NoneType value for files
            "cat": None,
            "monkey": None
        },
        "bob.txt": None,
    },
    "foo.txt": None,
    "bar": {
        "baz.txt": None
    },
    "emptydir": {}          # empty dict value for empty directories
}

class JSONNavigator(FileTreeNavigator):

    _value: str
    children: dict

    @property
    def value(self):
        return self._value

    def __init__(self, value: str, children: dict):
        self._value = value + ("/" if children is not None else "")
        self.children = children

    def get_children(self) -> "list[FileTreeNavigator]":
        if self.children is None:
            return []
        return [JSONNavigator(k, v) for k, v in self.children.items()]
    
