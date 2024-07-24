import os
import sys
import pytest
from unittest.mock import Mock, patch

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, project_root)

from llm_file_operations.tests.llm_interface.src.nexus_validator import NexusValidator
from llm_file_operations.src.instruction_parser import InstructionParser
from llm_file_operations.src.file_operations import FileOperator

@pytest.fixture
def mock_config():
    return {'some_key': 'some_value'}

@pytest.fixture
def nexus_validator(mock_config):
    return NexusValidator(mock_config)

def test_nexus_validator_initialization(nexus_validator):
    assert isinstance(nexus_validator.instruction_parser, InstructionParser)
    assert isinstance(nexus_validator.file_operator, FileOperator)

def test_validate_command_success(nexus_validator):
    with patch.object(InstructionParser, 'parse') as mock_parse:
        mock_parse.return_value = {'action': 'CREATE_FILE'}
        is_valid, message = nexus_validator.validate_command('some command')
        assert is_valid == True
        assert message == "Command is valid"

def test_validate_command_failure(nexus_validator):
    with patch.object(InstructionParser, 'parse') as mock_parse:
        mock_parse.return_value = {'action': 'INVALID_ACTION'}
        is_valid, message = nexus_validator.validate_command('some command')
        assert is_valid == False
        assert "Unsupported action" in message

def test_execute_command_success(nexus_validator):
    with patch.object(NexusValidator, 'validate_command') as mock_validate, \
         patch.object(FileOperator, 'execute') as mock_execute:
        mock_validate.return_value = (True, "Command is valid")
        mock_execute.return_value = "Command executed successfully"

        success, result = nexus_validator.execute_command('some command')
        assert success == True
        assert result == "Command executed successfully"

def test_execute_command_validation_failure(nexus_validator):
    with patch.object(NexusValidator, 'validate_command') as mock_validate:
        mock_validate.return_value = (False, "Invalid command")

        success, result = nexus_validator.execute_command('some command')
        assert success == False
        assert result == "Invalid command"

def test_execute_command_execution_failure(nexus_validator):
    with patch.object(NexusValidator, 'validate_command') as mock_validate, \
         patch.object(FileOperator, 'execute') as mock_execute:
        mock_validate.return_value = (True, "Command is valid")
        mock_execute.side_effect = Exception("Execution failed")

        success, result = nexus_validator.execute_command('some command')
        assert success == False
        assert "Execution failed" in result