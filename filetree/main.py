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

def demo_json_pprint():
    nav = JSONNavigator("root", obj["root"])
    pprint_filetree(nav)

def demo_filesystem_pprint():
    parent_dir = Path("..").resolve()
    filenav = FilesystemNavigator(parent_dir)
    pprint_filetree(filenav)

def main():   
    # demo_json_pprint()
    demo_filesystem_pprint()
    
if __name__ == "__main__":
    main()