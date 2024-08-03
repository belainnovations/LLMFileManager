
def test_instruction_parser_initialization_yaml():
    parser = InstructionParser(use_yaml=True)
    assert parser.use_yaml == True

def test_instruction_parser_initialization_custom():
    parser = InstructionParser(use_yaml=False)
    assert parser.use_yaml == False


def test_parse_valid_yaml():
    parser = InstructionParser(use_yaml=True)
    yaml_content = """
    LLMOP:
      version: "1.0"
      action: CREATE_FILE
      file: test.txt
      language: text
      description: Test file
      execution_key: "EXECUTE_LLM_INSTRUCTION"
      code: |
        This is a test file.
    """
    result = parser.parse(yaml_content)
    assert result is not None
    assert result['action'] == 'CREATE_FILE'
    assert result['file'] == 'test.txt'

def test_parse_invalid_yaml():
    parser = InstructionParser(use_yaml=True)
    yaml_content = "Invalid YAML content"
    result = parser.parse(yaml_content)
    assert result is None

def test_parse_valid_custom():
    parser = InstructionParser(use_yaml=False)
    custom_content = """
    ###LLMOP_START###
    action: CREATE_FILE
    file: test.txt
    ###LLMOP_END###
    ###CODE_START###
    This is a test file.
    ###CODE_END###
    """
    result = parser.parse(custom_content)
    assert result is not None
    assert result['action'] == 'CREATE_FILE'
    assert result['file'] == 'test.txt'

def test_parse_invalid_custom():
    parser = InstructionParser(use_yaml=False)
    custom_content = "Invalid custom content"
    result = parser.parse(custom_content)
    assert result is None
def test_instruction_parser_set_parse_mode():
    parser = InstructionParser(use_yaml=False)
    parser.set_parse_mode(True)
    assert parser.use_yaml == True
    parser.set_parse_mode(False)
    assert parser.use_yaml == False
import pytest
from instruction_parser import InstructionParser

# Add your unit tests for InstructionParser here