# src/utils.py
import json

def load_config(config_path: str = 'config/db_config.json') -> dict:
    """Loads a JSON configuration file."""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {config_path}")
        return {}
