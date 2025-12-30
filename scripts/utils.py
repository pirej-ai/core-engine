import logging
import os
import json
from typing import Dict, List, Tuple
from datetime import datetime

class Utils:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_config(self, file_path: str) -> Dict:
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            self.logger.error(f"Config file not found: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse config file: {e}")
            return {}

    def write_config(self, file_path: str, config: Dict) -> None:
        try:
            with open(file_path, 'w') as file:
                json.dump(config, file, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to write config file: {e}")

    def get_file_mod_time(self, file_path: str) -> float:
        try:
            return os.path.getmtime(file_path)
        except OSError as e:
            self.logger.error(f"Failed to get file mod time: {e}")
            return 0.0

    def get_current_time(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    utils = Utils()
    config = utils.load_config('config.json')
    print(config)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()