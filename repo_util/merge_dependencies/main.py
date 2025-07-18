from collision_policy import CollisionPolicies
from merge_dependencies import merge_dependencies
from sys import argv

if __name__ == "__main__":

    policy = CollisionPolicies.EXCLUDE_AND_WARN

    # this might be evil but it works really well
    available_policies = CollisionPolicies.__annotations__
    if len(argv) > 1:
        if (user_policy:=argv[1]) in available_policies:
            policy = available_policies[user_policy]
        else:
            print(f"[ERROR]: Unknown policy {user_policy}! Options are \n - {'\n - '.join(available_policies)}")
            print("Defaulting to policy EXCLUDE_AND_WARN\n")

    merge_dependencies(policy) 