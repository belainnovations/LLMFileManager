import pytest
from unittest.mock import Mock, patch
from clipboard_monitor import ClipboardMonitor

@pytest.fixture
def mock_dependencies():
    return {
        'instruction_parser': Mock(),
        'file_operator': Mock(),
        'error_handler': Mock(),
        'config': {'clipboard_check_interval': 0.1}
    }

def test_clipboard_monitor_initialization(mock_dependencies):
    """
    Test if ClipboardMonitor is correctly initialized with all required dependencies.
    """
    monitor = ClipboardMonitor(**mock_dependencies)
    assert isinstance(monitor, ClipboardMonitor)
    assert monitor.instruction_parser == mock_dependencies['instruction_parser']
    assert monitor.file_operator == mock_dependencies['file_operator']
    assert monitor.error_handler == mock_dependencies['error_handler']
    assert monitor.config == mock_dependencies['config']

@pytest.mark.parametrize("content,expected_format", [
    ("LLMOP:\n  version: '1.0'", "yaml"),
    ("###LLMOP_START###\nSome content", "custom"),
    ("Invalid content", None)
])
def test_detect_format(mock_dependencies, content, expected_format):
    """
    Test the detect_format method with various input formats.
    """
    monitor = ClipboardMonitor(**mock_dependencies)
    assert monitor.detect_format(content) == expected_format

@patch('clipboard_monitor.pyperclip.paste')
def test_start_monitoring_new_content(mock_paste, mock_dependencies):
    """
    Test the start_monitoring method when new content is detected.
    """
    mock_paste.side_effect = ["LLMOP:\n  version: '1.0'", KeyboardInterrupt]
    monitor = ClipboardMonitor(**mock_dependencies)

    with pytest.raises(KeyboardInterrupt):
        monitor.start_monitoring()

    mock_dependencies['instruction_parser'].set_parse_mode.assert_called_once_with(True)
    mock_dependencies['instruction_parser'].parse.assert_called_once()
    mock_dependencies['file_operator'].execute.assert_called_once()

@pytest.mark.usefixtures("capsys")
@patch('clipboard_monitor.pyperclip.paste')
@patch('clipboard_monitor.logger')
def test_start_monitoring_error_handling(mock_logger, mock_paste, mock_dependencies, capsys):
    """
    Test error handling in the start_monitoring method.
    """
    mock_paste.side_effect = [Exception("Test error"), KeyboardInterrupt]
    monitor = ClipboardMonitor(**mock_dependencies)

    with pytest.raises(KeyboardInterrupt):
        monitor.start_monitoring()

    # Check if the error was logged
    mock_logger.error.assert_called_with("An error occurred: Test error", exc_info=True)

    # Check if the error message was printed to console
    captured = capsys.readouterr()
    assert "An error occurred. Check the log for details." in captured.out

# Remove the custom capsys fixture as it's no longer needed

# Add more test cases as needed
