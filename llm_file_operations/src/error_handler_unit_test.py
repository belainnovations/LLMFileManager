import pytest
from error_handler import ErrorHandler
from unittest.mock import patch, MagicMock

@pytest.fixture
def error_handler():
    return ErrorHandler()

def test_error_handler_initialization(error_handler):
    assert isinstance(error_handler, ErrorHandler)

@patch('error_handler.logging.error')
def test_handle_standard_exception(mock_logging, error_handler, capsys):
    exception = Exception("Test exception")
    error_handler.handle(exception)
    assert len(mock_logging.call_args_list) == 2
    assert mock_logging.call_args_list[0][0][0] == f"An error occurred: {str(exception)}"
    assert "Traceback" in mock_logging.call_args_list[1][0][0]
    captured = capsys.readouterr()
    assert "An error occurred. Check the log for details." in captured.out

@patch('error_handler.logging.error')
def test_handle_custom_exception(mock_logging, error_handler, capsys):
    class CustomException(Exception):
        pass
    exception = CustomException("Custom test exception")
    error_handler.handle(exception)
    assert len(mock_logging.call_args_list) == 2
    assert mock_logging.call_args_list[0][0][0] == f"An error occurred: {str(exception)}"
    assert "Traceback" in mock_logging.call_args_list[1][0][0]
    captured = capsys.readouterr()
    assert "An error occurred. Check the log for details." in captured.out

@patch('error_handler.logging.error')
def test_handle_system_exception(mock_logging, error_handler, capsys):
    exception = FileNotFoundError("File not found")
    error_handler.handle(exception)
    assert len(mock_logging.call_args_list) == 2
    assert mock_logging.call_args_list[0][0][0] == f"An error occurred: {str(exception)}"
    assert "Traceback" in mock_logging.call_args_list[1][0][0]
    captured = capsys.readouterr()
    assert "An error occurred. Check the log for details." in captured.out

@patch('error_handler.logging.error')
def test_handle_error_simple_message(mock_logging, error_handler):
    message = "Simple error message"
    result = error_handler.handle_error(message)
    mock_logging.assert_called_with(message)
    assert result == f"Error: {message}"

@patch('error_handler.logging.error')
def test_handle_error_multiline_message(mock_logging, error_handler):
    message = "Error line 1\nError line 2"
    result = error_handler.handle_error(message)
    mock_logging.assert_called_with(message)
    assert result == f"Error: {message}"

@patch('error_handler.logging.error')
def test_handle_error_special_characters(mock_logging, error_handler):
    message = "Error: $pecial @haracters!"
    result = error_handler.handle_error(message)
    mock_logging.assert_called_with(message)
    assert result == f"Error: {message}"

@patch('error_handler.logging')
def test_logging_level(mock_logging, error_handler):
    error_handler.handle(Exception("Test"))
    mock_logging.error.assert_called()

@patch('error_handler.logging.error')
@patch('error_handler.traceback.format_exc')
def test_exception_and_traceback_logged(mock_format_exc, mock_logging, error_handler):
    mock_format_exc.return_value = "Traceback info"
    test_exception = Exception("Test exception")
    error_handler.handle(test_exception)
    mock_logging.assert_any_call(f"An error occurred: {str(test_exception)}")
    mock_logging.assert_any_call("Traceback info")

@pytest.mark.parametrize("log_level", ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
@patch('error_handler.logging')
def test_logging_behavior_different_levels(mock_logging, error_handler, log_level):
    mock_logging.getLogger.return_value.level = getattr(mock_logging, log_level)
    error_handler.handle(Exception("Test"))
    mock_logging.error.assert_called()
