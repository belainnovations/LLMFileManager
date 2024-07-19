import os
import logging
from instruction_parser import InstructionParser
from file_operations import FileOperator
from clipboard_monitor import ClipboardMonitor
from context_matcher import ContextMatcher
from error_handler import ErrorHandler

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting LLM File Operations")
    logger.info(f"Current working directory: {os.getcwd()}")

    try:
        instruction_parser = InstructionParser(use_yaml=True)
        context_matcher = ContextMatcher()
        error_handler = ErrorHandler()
        file_operator = FileOperator(context_matcher, error_handler)

        monitor = ClipboardMonitor(
            instruction_parser,
            file_operator,
            error_handler
        )

        monitor.start_monitoring()
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
