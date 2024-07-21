import os
import sys
import logging

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from llm_file_operations.src.main import load_config

def test_logging_level():
    config = load_config()
    logging_level = config.get('logging', {}).get('level', 'INFO')

    logger = logging.getLogger('test_logger')
    logger.setLevel(logging_level)

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

    print(f"Current logging level: {logging_level}")
    print("Check the log output to verify if messages are displayed according to the configured level.")

if __name__ == "__main__":
    test_logging_level()
