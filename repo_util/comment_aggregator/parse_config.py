from pathlib import Path
from yaml import safe_load

CONFIG_FP = f"{Path(__file__).parent}/resources/config.yml"

def parse_config():
    with open(CONFIG_FP, "r") as reader:
        return safe_load(reader)