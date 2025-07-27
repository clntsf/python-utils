import argparse
from json import dumps      # TODO: remove
from os import system
from pathlib import Path
import re
from yaml import safe_load

# https://stackoverflow.com/questions/60979532/argparse-ignore-positional-arguments-if-a-flag-is-set
# this will interrupt program flow if the --update-config flag is present and perform the code in __call__
# and then exit the program
class UpdateConfigAction(argparse.Action):
    def __init__(self, option_strings, dest, **kwargs):
        return super().__init__(option_strings, dest, nargs=0, default=argparse.SUPPRESS, **kwargs)
    
    def __call__(self, parser: argparse.ArgumentParser, namespace, values, option_string=None, **kwargs):
        system(f"open {CONFIG_FP}")
        parser.exit()

# TODO: add any extra arguments needed
def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find comments in a repository and render with markdown, configurable with YAML",
        fromfile_prefix_chars="@"
    )

    parser.add_argument("base_path", help="path from which to find tags")

    parser.add_argument(
        "-o", "--output_path", required=False,
        help="path to which to write markdown report (report not saved if left empty)"
    )

    parser.add_argument(
        "-u", "--update-config", action=UpdateConfigAction, required=False,
        help="if present, opens the config file for the user to update instead of running the script"
    )

    return parser

CONFIG_FP = f"{Path(__file__).parent}/comments.yml"
TAG_RE = r"^(.*#\s*({}).*)$"

def format_re(expr: str, tagnames: list[str]):
    return expr.format("|".join(tagnames))

def process_file(fp: str|Path, tag_re: str):
    with open(fp, "r") as reader:
        lines = reader.read().splitlines()

    tags = []
    for i, line in enumerate(lines, start=1):
        match = re.match(tag_re, line)
        if match != None:
            tags.append((i, match.groups()))

    return tags

def main():
    parser = make_parser()
    args = parser.parse_args()

    # get passed arguments
    base_fp = Path(args.base_path).resolve()
    subfiles = base_fp.glob("**/*.py")
    out_path: str = args.output_path

    # parse config file
    with open(CONFIG_FP, "r") as reader:
        config = safe_load(reader)

    settings = config["settings"]
    comments = config["comments"]
    tagnames = [comment["comment-tag"] for comment in comments]
    
    data = {}

    tag_re_formatted = format_re(TAG_RE, tagnames)
    for file_path in subfiles:
        data[file_path.name] = process_file(file_path, tag_re_formatted)

    print(dumps(data, indent=2))
        
if __name__ == "__main__":
    main()