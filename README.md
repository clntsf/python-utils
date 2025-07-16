# python-utils
Miscellaneous utility scripts in Python, designed to solve common problems in an extensible way

## Dependencies:

Each module which requires a non-stdlib dependency will have a requirements.txt file in a format suitable for immediate use with `pip install -r requirements.txt`. Where possible it is my intention to make the most of Python's extensive standard library, but where not adding a dependency would require the writing of another module or more I may at least temporarily do so.

## Contents:

- **[/filetree](./filetree/)**: Highly-extensible module for defining strategies for iterating over file trees of any type and pretty-printing their contents uniformly, with two example strategies.

- **[/repo_util](./repo_util/)**: Various utility scripts I am using inside this repository (but whose use could be helpful elsewhere) for managing dependencies etc.

    - **[/merge_dependencies](./repo_util/merge_dependencies/)**: Merge the dependencies in all requirements.txt files across a project into a central requirements.txt at root (configurable), with extensible policy-based collision handling