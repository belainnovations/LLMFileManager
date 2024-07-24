import pytest
from unittest.mock import mock_open, patch
from config import NexusConfig
import os

@pytest.fixture
def mock_config_data():
    return """
    anthropic_api_key: test_api_key
    model: claude-3-5-sonnet-20240620
    max_tokens: 2048
    """

@pytest.fixture
def mock_config(mock_config_data):
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=mock_config_data)):
            yield NexusConfig()

def test_nexus_config_initialization(mock_config):
    assert isinstance(mock_config, NexusConfig)

def test_get_api_key(mock_config):
    assert mock_config.get_api_key() == "test_api_key"

def test_get_model(mock_config):
    assert mock_config.get_model() == "claude-3-5-sonnet-20240620"

def test_get_max_tokens(mock_config):
    assert mock_config.get_max_tokens() == 2048

def test_config_file_not_found():
    with patch('os.path.exists', return_value=False):
        with pytest.raises(FileNotFoundError):
            NexusConfig("nonexistent_config.yaml")

def test_custom_config_path(mock_config_data):
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=mock_config_data)):
            config = NexusConfig("custom_config.yaml")
            assert config.config_path == "custom_config.yaml"
