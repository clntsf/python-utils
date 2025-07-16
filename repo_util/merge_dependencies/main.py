from collision_policy import CollisionPolicies
from merge_dependencies import merge_dependencies

if __name__ == "__main__":
    merge_dependencies(CollisionPolicies.EXCLUDE_AND_WARN)