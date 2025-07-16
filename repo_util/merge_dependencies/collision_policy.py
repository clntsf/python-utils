from abc import ABC, abstractmethod

class CollisionPolicy(ABC):

    @staticmethod
    @abstractmethod
    def resolve(dependencies: dict[str, str], key: str, newval: str, reqs_path: str = "") -> None:
        """
        Resolve the collision in the dependencies dict in-place, returning None.

        Parameters
        ----------

        dependencies : dict[str, str]
            dictionary of dependencies in the form {"dependencyName": "{equalitySymbol}{version}"}
        key : str
            the dependency for which the collision occurred
        newval : str
            the value of the colliding dependency (e.g. ">=1.0.0")
        reqs_path : str, optional
            the path to the requirements file containing the collision (default "")
        """
        ...


class KeepFirstPolicy(CollisionPolicy):
    """
    This policy has a first-in strategy: the first version control seen for a dependency is kept.
    In practice this probably is not sufficient for advanced needs, but should suffice as a minimal
    example of the interface as well as adequate default behavior for merge_dependencies
    """

    @staticmethod
    def resolve(dependencies: dict[str, str], key: str, newval: str, reqs_path: str = "") -> None:
        return


class ExcludeAndWarnDependency(CollisionPolicy):
    """
    This policy opts to exclude any dependencies with collisions and print a warning for the user for each collision.
    Excluding a dependency is done by setting its value in dependencies to ""
    """

    @staticmethod
    def resolve(dependencies: dict[str, str], key: str, newval: str, reqs_path: str = "") -> None:
        # add dep name at start for friendliness with piping to sort
        print(f"@{key} [WARN]: Colliding values for dependency {key} found, new value is '{newval}' from path: {reqs_path}")
        dependencies[key] = ""


class CollisionPolicies:
    """
    this is purely for convenience. Developers can choose to import their specified strategy
    instead of having to update this with every created strategy, but this provides a clean and
    intuitive way for users to select a strategy

    Options
     * KEEP_FIRST
     * EXCLUDE_AND_WARN
    """
    KEEP_FIRST: type[CollisionPolicy] = KeepFirstPolicy
    EXCLUDE_AND_WARN: type[CollisionPolicy] = ExcludeAndWarnDependency
