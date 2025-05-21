from pathlib import Path
import os
import re
import yaml
from dotenv import load_dotenv

load_dotenv()

def greet(name):
    return f"Hello, {name}!" 


def _substitute_env_vars(obj):
    pattern = re.compile(r'\$\{([A-Za-z0-9_]+)\}')
    if isinstance(obj, dict):
        return {k: _substitute_env_vars(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_substitute_env_vars(i) for i in obj]
    elif isinstance(obj, str):
        def replacer(match):
            var_name = match.group(1)
            return os.environ.get(var_name, match.group(0))
        return pattern.sub(replacer, obj)
    else:
        return obj

def read_config(config_path: Path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return _substitute_env_vars(config)

def get_config():
    config_path = Path(__file__).parent.parent / "config.yml"
    return read_config(config_path)

def get_remotes():
    config = get_config()
    return config["remotes"]

def get_workflows():
    config = get_config()
    return config["workflows"]