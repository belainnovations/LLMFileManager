from llm_file_operations.src.instruction_parser import InstructionParser
from llm_file_operations.src.file_operations import FileOperator
from llm_file_operations.src.context_matcher import ContextMatcher

class NexusValidator:
    def __init__(self, config):
        self.instruction_parser = InstructionParser()
        self.file_operator = FileOperator(ContextMatcher(), None, config)

    def validate_command(self, command):
        try:
            # Parse the command
            instruction = self.instruction_parser.parse(command)
            
            # Validate file operations
            self.file_operator.validate(instruction)
            
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