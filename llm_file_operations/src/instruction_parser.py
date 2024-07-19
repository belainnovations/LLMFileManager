import logging
import yaml
import re

logger = logging.getLogger(__name__)

class InstructionParser:
    def __init__(self, use_yaml=False):
        self.version = "1.0"
        self.use_yaml = use_yaml

    def set_parse_mode(self, use_yaml):
        self.use_yaml = use_yaml

    def parse(self, content):
        if self.use_yaml:
            return self.parse_yaml(content)
        else:
            return self.parse_custom(content)

    def parse_custom(self, content):
        llm_op = self.extract_llm_op_segment(content)
        if not llm_op:
            logger.debug("No valid LLM operation found in content.")
            return None

        instruction = {'instruction': llm_op}

        instruction['start_context'] = self.extract_context(content, '###CONTEXT_START###', '###CONTEXT_END###')
        instruction['end_context'] = self.extract_context(content, '###END_CONTEXT_START###', '###END_CONTEXT_END###')
        instruction['code'] = self.extract_context(content, '###CODE_START###', '###CODE_END###', preserve_indentation=True)

        for line in llm_op.splitlines():
            if ':' in line:
                key, value = line.split(':', 1)
                instruction[key.strip().lower()] = value.strip()

        logger.debug(f"Parsed custom instruction: {instruction}")
        return instruction

    def parse_yaml(self, content):
        try:
            parsed_yaml = yaml.safe_load(content)
            logger.debug(f"Raw parsed YAML content: {parsed_yaml}")
            if isinstance(parsed_yaml, dict) and 'LLMOP' in parsed_yaml:
                if self.validate_yaml_structure(parsed_yaml):
                    instruction = self.convert_yaml_to_instruction(parsed_yaml)
                    logger.debug(f"Parsed YAML instruction: {instruction}")
                    return instruction
        except yaml.YAMLError as e:
            logger.error(f"YAML parsing error: {str(e)}")

        logger.error("Failed to parse YAML content")
        return None

    def validate_yaml_structure(self, parsed_yaml):
        logger.debug(f"Validating YAML structure: {parsed_yaml}")
        if 'LLMOP' not in parsed_yaml:
            logger.error("Missing LLMOP key in YAML")
            return False
        
        required_fields = ['version', 'action', 'file', 'description', 'execution_key']
        llmop_content = parsed_yaml['LLMOP']
        
        for field in required_fields:
            if field.lower() not in llmop_content:
                logger.error(f"Missing required field in YAML: {field}")
                return False
        
        action = llmop_content['action'].upper()
        valid_actions = ['CREATE_FILE', 'CREATE_FOLDER', 'REPLACE', 'INSERT', 'DELETE', 'DELETE_FILE', 'DELETE_FOLDER']
        if action not in valid_actions:
            logger.error(f"Invalid action in YAML: {action}")
            return False

        # Check for 'language' field only for actions that require it
        if action not in ['CREATE_FOLDER', 'DELETE_FILE', 'DELETE_FOLDER'] and 'language' not in llmop_content:
            logger.error("Missing 'language' field in YAML for action that requires it")
            return False

        logger.debug("YAML structure validation successful")
        return True
    def convert_yaml_to_instruction(self, parsed_yaml):
        if 'LLMOP' not in parsed_yaml:
            logger.error("Missing LLMOP key in parsed YAML")
            return None
        instruction = parsed_yaml['LLMOP']
        instruction = {k.lower(): v for k, v in instruction.items()}
        instruction['instruction'] = yaml.dump(parsed_yaml, default_flow_style=False)
        return instruction

    def extract_llm_op_segment(self, clipboard_text):
        pattern = r'###LLMOP_START###\s*(.*?)\s*###LLMOP_END###'
        match = re.search(pattern, clipboard_text, re.DOTALL)

        if match:
            content = match.group(1)
            return content.strip()
        else:
            return None

    def extract_context(self, clipboard_text, start_marker, end_marker, preserve_indentation=False):
        pattern = f'{re.escape(start_marker)}(.*?){re.escape(end_marker)}'
        match = re.search(pattern, clipboard_text, re.DOTALL)
        
        if match:
            content = match.group(1)
            if preserve_indentation:
                # Remove only the first empty line if it exists
                return content.lstrip('\n').rstrip()
            else:
                return content.strip()
        else:
            return None