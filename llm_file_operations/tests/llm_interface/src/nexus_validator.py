from llm_file_operations.src.instruction_parser import InstructionParser
from llm_file_operations.src.file_operations import FileOperator
from llm_file_operations.src.context_matcher import ContextMatcher

class NexusValidator:
    ALLOWED_ACTIONS = ['CREATE_FILE', 'REPLACE', 'APPEND', 'DELETE']

    def __init__(self, config):
        self.instruction_parser = InstructionParser()
        self.file_operator = FileOperator(ContextMatcher(), None, config)

    def validate_command(self, command):
        try:
            # Parse the command
            instruction = self.instruction_parser.parse(command)

            # Perform basic validation checks
            if not instruction or 'action' not in instruction:
                return False, "Invalid command structure"

            # Check if the action is supported
            if instruction['action'] not in self.ALLOWED_ACTIONS:
                return False, f"Unsupported action: {instruction['action']}"

            # Additional validation can be added here based on the specific requirements

            return True, "Command is valid"
        except Exception as e:
            return False, str(e)

    def execute_command(self, command):
        is_valid, message = self.validate_command(command)
        if not is_valid:
            return False, message
        
        try:
            result = self.file_operator.execute(self.instruction_parser.parse(command))
            return True, result
        except Exception as e:
            return False, str(e)