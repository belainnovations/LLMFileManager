import pytest
from unittest.mock import patch, mock_open
import yaml
from main import load_config, main

@patch('yaml.safe_load')
@patch('builtins.open', new_callable=mock_open, read_data="config_data: test")
def test_load_config_success(mock_file, mock_yaml_load):
    mock_yaml_load.return_value = {"config_key": "config_value"}
    config = load_config()
    assert config == {"config_key": "config_value"}

@patch('builtins.open', side_effect=FileNotFoundError)
def test_load_config_file_not_found(mock_file):
    with pytest.raises(FileNotFoundError):
        load_config()

@patch('yaml.safe_load', side_effect=yaml.YAMLError)
@patch('builtins.open', new_callable=mock_open, read_data="invalid: yaml: content")
def test_load_config_invalid_yaml(mock_file, mock_yaml_load):
    with pytest.raises(yaml.YAMLError):
        load_config()

# Add your unit tests for the main function here
