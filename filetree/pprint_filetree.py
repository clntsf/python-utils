from navigators.filetree_navigator import FileTreeNavigator

_EMPTY_PREFIX           = "    "
_EMPTY_NOTLAST_PREFIX   = "│   "
_MIDDLE_CHILD_CONNECTOR = "├── "
_LAST_CHILD_CONNECTOR   = "└── "

def pprint_filetree(root: FileTreeNavigator, _prefix: str = "", _is_last: bool = True, _is_root: bool = True) -> None:
    """
    Pretty-print a filetree specified by a FileTreeNavigator pointing to its root. This function runs recursively
    and supports any arbitrary strategy implementing the FileTreeNavigator interface, so it can be used cleanly with
    JSON filetree representations (see json_navigator.py) or children of a specified path in the user's filesystem (see
    filesystem_navigator.py)

    @param root: a FileTreeNavigator pointing to the root of the filetree to parse
    """
    if _is_root:
        print(f"/{root.value}")
    else:
        connector = _LAST_CHILD_CONNECTOR if _is_last else _MIDDLE_CHILD_CONNECTOR
        print(_prefix + connector + root.value)
    
    if not _is_root:
        _prefix += _EMPTY_PREFIX if _is_last else _EMPTY_NOTLAST_PREFIX

    children: list[FileTreeNavigator] = root.get_children()
    if len(children) == 0:
        return

    for not_last_child in children[:-1]:
        pprint_filetree(not_last_child, _prefix, False, False)

    pprint_filetree(children[-1], _prefix, True, False)