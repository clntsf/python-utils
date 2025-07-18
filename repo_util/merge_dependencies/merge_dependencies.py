from pathlib import Path
from re import findall, MULTILINE
from collision_policy import (
    CollisionPolicy,
    CollisionPolicies
)

# matches an actual dependency listing and not random text or comments
DEPENDENCY_REGEX = r"^(.+?)((?:==|>|>=|<|<=).+)$"

# USER: configure this based on the path to the project root directory relative to this file
PROJECT_ROOT_RELPATH = "../../.."

def merge_dependencies(collision_policy: type[CollisionPolicy] = CollisionPolicies.KEEP_FIRST):
    """Merge the dependencies of all project requirements.txt files into the main requirements.txt."""

    repo_root_dir = Path(__file__, PROJECT_ROOT_RELPATH).resolve()
    main_requirements = Path(repo_root_dir, "requirements.txt")
    project_requirements = repo_root_dir.glob("*/**/requirements.txt") # ignore requirement at root
    dependency_dict: dict[str, str] = {}

    # get dependencies and handle collisions
    for requirement_path in project_requirements:
        strpath = str(requirement_path.relative_to(repo_root_dir))
        with open(requirement_path, "r") as reader:
            project_dependencies = findall(DEPENDENCY_REGEX, reader.read(), MULTILINE)

            for (dep, version) in project_dependencies:
                if dep not in dependency_dict:
                    dependency_dict[dep] = version
                else:
                    collision_policy.resolve(dependency_dict, dep, version, strpath)
        
    out = "\n".join(
        "".join(item) for item in dependency_dict.items()
        if item[1] != ""                              # items with value "" are excluded by a collision
    )

    # no valid dependencies
    if out == "":
        print("[INFO]: No dependencies found in project, will not write main requirements.txt")
        return

    with open(main_requirements, "w") as writer:
        writer.write(out)

