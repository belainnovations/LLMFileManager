import pytest
from unittest.mock import patch, mock_open
import yaml
import logging
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

@patch('main.load_config')
@patch('main.InstructionParser')
@patch('main.ContextMatcher')
@patch('main.ErrorHandler')
@patch('main.FileOperator')
@patch('main.ClipboardMonitor')
def test_main_component_initialization(mock_clipboard_monitor, mock_file_operator, 
                                       mock_error_handler, mock_context_matcher, 
                                       mock_instruction_parser, mock_load_config):
    mock_load_config.return_value = {"config_key": "config_value"}
    main()
    mock_instruction_parser.assert_called_once_with(use_yaml=True)
    mock_context_matcher.assert_called_once()
    mock_error_handler.assert_called_once()
    mock_file_operator.assert_called_once()
    mock_clipboard_monitor.assert_called_once()
    mock_clipboard_monitor.return_value.start_monitoring.assert_called_once()

@patch('main.load_config', side_effect=Exception("Config error"))
def test_main_config_loading_error(mock_load_config, caplog):
    caplog.set_level(logging.ERROR)
    main()
    assert "An error occurred: Config error" in caplog.text

@patch('main.load_config')
@patch('main.ClipboardMonitor')
def test_main_clipboard_monitor_error(mock_clipboard_monitor, mock_load_config, caplog):
    mock_load_config.return_value = {"config_key": "config_value"}
    mock_clipboard_monitor.return_value.start_monitoring.side_effect = Exception("Monitor error")
    caplog.set_level(logging.ERROR)
    main()
    assert "An error occurred: Monitor error" in caplog.text
