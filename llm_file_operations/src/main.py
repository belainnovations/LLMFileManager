import os
import sys
import yaml
import logging
from instruction_parser import InstructionParser
from file_operations import FileOperator
from clipboard_monitor import ClipboardMonitor
from context_matcher import ContextMatcher
from error_handler import ErrorHandler

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_config_path():
    if getattr(sys, 'frozen', False):
        # If running as executable
        application_path = os.path.dirname(sys.executable)
        config_path = os.path.join(application_path, 'data', 'config.yaml')
    else:
        # If running as script
        application_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(application_path, 'config', 'config.yaml')
    
    print(f"Looking for config file at: {config_path}")  # Debug print
    return config_path

def load_config():
    config_path = get_config_path()
    try:
        with open(config_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        print(f"Config file not found at {config_path}. Using default configuration.")
        return {}  # Return default configuration or raise an error as appropriate

def main():
    logger.info("Starting LLM File Operations")
    logger.info(f"Current working directory: {os.getcwd()}")

    try:
        config = load_config()
        instruction_parser = InstructionParser(use_yaml=True)
        context_matcher = ContextMatcher()
        error_handler = ErrorHandler()
        file_operator = FileOperator(context_matcher, error_handler, config)

        monitor = ClipboardMonitor(
            instruction_parser,
            file_operator,
            error_handler,
            config
        )

        monitor.start_monitoring()
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
