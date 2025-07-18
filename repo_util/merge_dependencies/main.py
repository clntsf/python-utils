from collision_policy import CollisionPolicies
from merge_dependencies import merge_dependencies
from sys import argv

if __name__ == "__main__":

    policy = CollisionPolicies.EXCLUDE_AND_WARN

    # choose user-defined policy if supplied on command-line if present and valid
    if len(argv) > 1:
        user_policy = CollisionPolicies[argv[1]]
        if user_policy is None:
            print(f"[ERROR]: Unknown policy {user_policy}!")
            print(f"Options are:\n - {'\n - '.join(CollisionPolicies.__annotations__)}")
            print("Defaulting to policy EXCLUDE_AND_WARN")
        else:
            policy = user_policy

    merge_dependencies(policy) 