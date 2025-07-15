from navigators.json_navigator import JSONNavigator, SAMPLE_JSON_TREE
from navigators.filesystem_navigator import FilesystemNavigator
from pprint_filetree import pprint_filetree

from pathlib import Path

def demo_json_pprint():
    nav = JSONNavigator("root", SAMPLE_JSON_TREE)
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