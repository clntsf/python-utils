from matplotlib.colors import CSS4_COLORS

from parse_config import parse_config

# https://stackoverflow.com/questions/35465557/how-to-apply-color-on-text-in-markdown

def format_output():
    config = parse_config()
    generate_links = config["settings"]["generate-links"]
    

if __name__ == "__main__":
    format_output()