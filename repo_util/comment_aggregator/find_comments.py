import argparse
from json import dumps      # TODO: remove
from os import system
from pathlib import Path
import re
from typing import Iterable
from yaml import safe_load

from parse_config import parse_config, CONFIG_FP

TAG_RE = r"^(.*#\s*({}).*)$"

# https://stackoverflow.com/questions/60979532/argparse-ignore-positional-arguments-if-a-flag-is-set
# this will interrupt program flow if the --update-config flag is present and perform the code in __call__
# and then exit the program
class UpdateConfigAction(argparse.Action):
    def __init__(self, option_strings, dest, **kwargs):
        return super().__init__(option_strings, dest, nargs=0, default=argparse.SUPPRESS, **kwargs)
    
    def __call__(self, parser: argparse.ArgumentParser, *args, **kwargs):
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
        "-s", "--min_severity", type=int, default=1,
        help="Minimum severity tag to log (severity configurable in YAML)"
    )

    parser.add_argument(
        "-u", "--update-config", action=UpdateConfigAction, required=False,
        help="if present, opens the config file for the user to update instead of running the script"
    )

    return parser

def format_re(expr: str, tagnames: list[str]):
    return expr.format("|".join(tagnames))

def process_files(files: Iterable[Path], tag_re: str):
    data = {}

    for fp in files:
        with open(fp, "r") as reader:
            lines = reader.read().splitlines()

        tags = []
        for i, line in enumerate(lines, start=1):
            match = re.match(tag_re, line)
            if match != None:
                tags.append((i, match.groups()))

        data[fp.name] = tags

    return data

def main():
    parser = make_parser()
    args = parser.parse_args()

    # get passed arguments
    base_fp = Path(args.base_path).resolve()
    subfiles = base_fp.glob("**/*.py")
    out_path: str = args.output_path

    # parse config file
    config = parse_config()

    settings = config["settings"]
    comments = config["comments"]
    tagnames = [comment["comment-tag"] for comment in comments]
    
    tag_re_formatted = format_re(TAG_RE, tagnames)
    data = process_files(subfiles, tag_re_formatted)

    data_out = dumps(data, indent=2)
    if out_path is not None:
        out_path_abs = Path(out_path).resolve()

        # add default filename if path supplied is a directory
        if out_path_abs.is_dir():
            out_path_abs = out_path_abs.joinpath("output.json")

        with open(out_path_abs, "w") as writer:
            writer.write(data_out)

        
if __name__ == "__main__":
    main()