import os
import sys
import pytest
from unittest.mock import patch

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, project_root)

from llm_file_operations.tests.llm_interface.src.api_providers import AnthropicProvider
from llm_file_operations.tests.llm_interface.src.nexus_validator import NexusValidator
from llm_file_operations.tests.llm_interface.src.config import NexusConfig

@pytest.fixture
def mock_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'test_config.yaml')
    return NexusConfig(config_path)

@pytest.fixture
def anthropic_provider(mock_config):
    return AnthropicProvider(mock_config.get_api_key())

@pytest.fixture
def nexus_validator(mock_config):
    return NexusValidator(mock_config)

def test_command_generation_to_execution(anthropic_provider, nexus_validator):
    # Mock the API response
    with patch.object(AnthropicProvider, 'generate_response') as mock_generate:
        mock_generate.return_value = "LLMOP:\n  version: '1.0'\n  action: CREATE_FILE\n  file: test.txt\n  content: 'Hello, World!'"

        # Generate command
        command = anthropic_provider.generate_response([{"role": "user", "content": "Create a file named test.txt with content 'Hello, World!'"}])

        # Validate command
        is_valid, message = nexus_validator.validate_command(command)
        assert is_valid, f"Command validation failed: {message}"

        # Execute command (mocked)
        with patch.object(NexusValidator, 'execute_command') as mock_execute:
            mock_execute.return_value = (True, "File created successfully")
            success, result = nexus_validator.execute_command(command)
            assert success, f"Command execution failed: {result}"

def test_configuration_handling(mock_config, anthropic_provider, nexus_validator):
    assert anthropic_provider.client.api_key == mock_config.get_api_key()
    assert nexus_validator.file_operator.config == mock_config._config

# Add more integration tests here
