import yaml
import os

CONFIG_PATH = os.path.expanduser("~/.genix/config.yaml")


def load_config():
    """Load user configuration."""
    default_config = {"shell": "bash", "confirmation": True, "cloud_sync": False}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)
    return default_config


def save_config(config):
    """Save user configuration."""
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
