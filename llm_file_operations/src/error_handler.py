import logging
import traceback

logger = logging.getLogger(__name__)

class ErrorHandler:
    def handle(self, exception):
        logging.error(f"An error occurred: {str(exception)}")
        logging.error(traceback.format_exc())
        print("An error occurred. Check the log for details.")

    def handle_error(self, message):
        logging.error(message)
        return f"Error: {message}"