import re
from argparse import ArgumentParser
from yaml import safe_load

def make_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Find comments in a repository and render with markdown, configurable with YAML",
        fromfile_prefix_chars="@"
    )

    parser.add_argument("base_path", help="path from which to find tags")

    parser.add_argument(
        "-o", "--output_path", required = False,
        help="path to which to write markdown report (report not saved if left empty)"
    )

    parser.add_argument(
        "-u", "--update-config", action="store_true", required=False,
        help = "if present, opens the config file for the user to update instead of running the script"
    )
    return parser

def load_config():
    with open("comments.yml", "r") as reader:
        print(safe_load(reader))

def main():
    parser = make_parser()
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()