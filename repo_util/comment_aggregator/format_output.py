from pathlib import Path
from textwrap import dedent

from parse_config import parse_config

# https://stackoverflow.com/questions/35465557/how-to-apply-color-on-text-in-markdown
def format_output(root: str|Path, data: dict[Path, list]):
    config = parse_config()

    # make a stylesheet for custom tag colors
    tags: list[dict] = config["tags"]
    tag_colors = {
        tag["tag-name"]: tag.get("color", "black")
        for tag in tags
    }
    styles = "<style>\n" + "\n".join(
        tagname + " {" + f"color: {color}; font-weight: bold" + "}"
        for tagname, color in tag_colors.items()
    ) + "\n</style>"

    out = styles + dedent(f"""

    # Aggregated Comments from {root}

    Below are a list of comments by file. Files with no comments are not listed here
    """)

    for filepath, refs in data.items():
        if refs == []: continue

        relpath = filepath.relative_to(root)
        header = f"\n## [{filepath.name}]({relpath})\n\n"

        # format the tags for the file
        file_tags = []
        for (line_number, (line, tagname)) in refs:
            formatted_tag = f"<{tagname}>[ {tagname} ]</{tagname}>"
            line_ref = f"[line {line_number}]({relpath}#L{line_number})"
            file_tags.append(f" - {formatted_tag} @ {line_ref}: {line}")

        out += header + "\n".join(file_tags)
        
    with open(f"{root}/repo_comments.md", "w") as writer:
        writer.write(out)