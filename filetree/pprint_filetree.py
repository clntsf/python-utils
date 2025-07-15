from navigators.filetree_navigator import FileTreeNavigator

EMPTY_PREFIX           = "    "
EMPTY_NOTLAST_PREFIX   = "│   "
MIDDLE_CHILD_CONNECTOR = "├── "
LAST_CHILD_CONNECTOR   = "└── "

def pprint_filetree(root: FileTreeNavigator, prefix: str = "", is_last: bool = True, is_root: bool = True):
    if is_root:
        print(f"/{root.value}")
    else:
        connector = LAST_CHILD_CONNECTOR if is_last else MIDDLE_CHILD_CONNECTOR
        print(prefix + connector + root.value)
    
    prefix += EMPTY_PREFIX if is_last else EMPTY_NOTLAST_PREFIX
    if is_root:
        prefix = ""

    children: list[FileTreeNavigator] = root.get_children()
    if len(children) == 0:
        return

    for not_last_child in children[:-1]:
        pprint_filetree(not_last_child, prefix, False, False)

    pprint_filetree(children[-1], prefix, True, False)