from pathlib import Path
from re import findall
from enum import Enum

class DependencyCollisionPolicy(Enum):
    """
    class for dependency collision policies for fix addressed below, to be used 
    in merge_dependencies to determine behavior upon collision.
    
    NB: If we really wanted to (we might) we could break this policy off into an
    interface and have an instance of it passed to merge_dependencies for maximal
    extensibility
    """
    CHOOSE_FIRST = 0
    EXCLUDE_BOTH_AND_WARN = 1
    PROMPT_AND_WARN = 2

# matches an actual dependency listing and not random text or comments
DEPENDENCY_REGEX = r"\b(.+?(?:==|>|>=|<|<=).+)\b"

# USER: configure this based on the path to the project root directory relative to this file
PROJECT_ROOT_RELPATH = "../.."

def merge_dependencies():
    """Merge the dependencies of all project requirements.txt files into the main requirements.txt."""

    repo_root_dir = Path(__file__, PROJECT_ROOT_RELPATH).resolve()
    main_requirements = Path(repo_root_dir, "requirements.txt")
    project_requirements = repo_root_dir.glob("**/requirements.txt")
    dependency_set = set()

    # TODO: FIX. this naively assumes no dependencies overlap and have conflicting versions.
    # This should at some point be left to the user of this script, but detection for these and
    # a simple solution like prompting for choice or writing to stdout on a dependency collision
    # should be implemented and controllable with a parameter to this function, on by default
    for requirement_path in project_requirements:
        with open(requirement_path, "r") as reader:
            project_dependencies = findall(DEPENDENCY_REGEX, reader.read())
            dependency_set.update(project_dependencies)

    if len(dependency_set) == 0:
        print("[INFO]: No dependencies found in project, will not write main requirements.txt")
        return

    with open(main_requirements, "w") as writer:
        writer.write("\n".join(dependency_set))

merge_dependencies()