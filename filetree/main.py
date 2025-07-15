from navigators.json_navigator import JSONNavigator
from navigators.filesystem_navigator import FilesystemNavigator
from pprint_filetree import pprint_filetree

from pathlib import Path

obj = {
    "root": {
        "alice": {
            "charlie": {
                "dog": None,
                "cat": None,
                "monkey": None
            },
            "bob.txt": None,
        },
        "foo.txt": None,
        "bar": {
            "baz.txt": None
        },
        "emptydir": {}
    }
}
    
nav = JSONNavigator("root", obj["root"])
pprint_filetree(nav)

parent_dir = Path("..").resolve()
filenav = FilesystemNavigator(parent_dir)
# pprint_filetree(filenav)