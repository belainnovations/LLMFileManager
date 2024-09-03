import pyperclip
import time
import logging
import binascii
from tenacity import retry, stop_after_attempt, wait_fixed

logger = logging.getLogger(__name__)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(0.1))
def safe_paste():
    return pyperclip.paste()

class ClipboardMonitor:
    def __init__(self, instruction_parser, file_operator, error_handler, config):
        self.instruction_parser = instruction_parser
        self.file_operator = file_operator
        self.error_handler = error_handler
        self.config = config
        self.previous_content = ''

    def start_monitoring(self):
        logger.info("Starting clipboard monitoring...")
        check_interval = self.config.get('clipboard_check_interval', 0.5)
        self.previous_content = safe_paste()
        logger.debug(f"Initial clipboard content: {self.previous_content[:100]}")
        while True:
            try:
                clipboard_content = safe_paste()
                if clipboard_content != self.previous_content:
                    logger.debug(f"New clipboard content detected. Length: {len(clipboard_content)}")
                    logger.debug(f"First 100 chars: {clipboard_content[:100]}")
                    logger.debug(f"Hexdump of first 20 bytes: {binascii.hexlify(clipboard_content[:20].encode()).decode()}")
    
                    format_type = self.detect_format(clipboard_content)
                    if format_type:
                        logger.info(f"Detected {format_type} format instruction")
                        self.instruction_parser.set_parse_mode(format_type == "yaml")
                        instruction = self.instruction_parser.parse(clipboard_content)
                        if instruction is not None:
                            logger.debug(f"Parsed instruction: {instruction}")
                            result = self.file_operator.execute(instruction)
                            logger.info(result)
                        else:
                            logger.debug("No valid LLM operation found in clipboard content.")
                    else:
                        logger.debug("No valid LLM operation format detected in clipboard content.")
    
                    self.previous_content = clipboard_content
                time.sleep(check_interval)
            except Exception as e:
                logger.error(f"An error occurred: {str(e)}", exc_info=True)
                if "YAML" in str(e):
                    logger.error("YAML parsing error. Please check the format of your instruction.")
                print("An error occurred. Check the log for details.")
                time.sleep(1)  # Add a small delay to prevent rapid error logging

    def detect_format(self, content):
        content = content.strip()  # Remove leading/trailing whitespace
        if content.startswith("###LLMOP_START###"):
            return "custom"
        elif content.startswith("LLMOP:"):
            return "yaml"
        return None