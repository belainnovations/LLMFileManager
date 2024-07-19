import pyperclip
import time
import logging
import binascii

logger = logging.getLogger(__name__)

class ClipboardMonitor:
    def __init__(self, instruction_parser, file_operator, error_handler):
        self.instruction_parser = instruction_parser
        self.file_operator = file_operator
        self.error_handler = error_handler
        self.previous_content = ''

    def start_monitoring(self):
        logger.info("Starting clipboard monitoring...")
        while True:
            try:
                clipboard_content = pyperclip.paste()
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
                time.sleep(0.5)
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
