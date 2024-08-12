import pytest
from unittest.mock import patch, MagicMock
from src.clipboard_monitor import ClipboardMonitor
from src.instruction_parser import InstructionParser
from src.file_operations import FileOperator
from src.error_handler import ErrorHandler
import logging

@pytest.fixture
def mock_components():
    return {
        'instruction_parser': MagicMock(spec=InstructionParser),
        'file_operator': MagicMock(spec=FileOperator),
        'error_handler': MagicMock(spec=ErrorHandler),
        'config': {'clipboard_check_interval': 0.1}
    }

def test_error_propagation(mock_components, caplog):
    caplog.set_level(logging.ERROR)

    # Simulate an error in instruction parsing
    mock_components['instruction_parser'].parse.side_effect = ValueError("Invalid instruction format")

    clipboard_content = "Invalid LLMOP instruction"

    def clipboard_side_effect():
        yield clipboard_content
        raise KeyboardInterrupt

    with patch('pyperclip.paste', side_effect=clipboard_side_effect()):
        monitor = ClipboardMonitor(**mock_components)
        try:
            monitor.start_monitoring()
        except KeyboardInterrupt:
            pass

    # Check if error was logged
    assert "An error occurred" in caplog.text
    assert "Invalid instruction format" in caplog.text

def test_error_logging(mock_components, caplog):
    caplog.set_level(logging.ERROR)

    # Simulate an error in file operation
    mock_components['file_operator'].execute.side_effect = IOError("File not found")

    clipboard_content = """
    LLMOP:
      version: "1.0"
      action: CREATE_FILE
      file: non_existent/test.txt
      language: text
      description: Create a new text file
      execution_key: "EXECUTE_LLM_INSTRUCTION"
      code: |-
        Test content
    """

    def clipboard_side_effect():
        yield clipboard_content
        raise KeyboardInterrupt

    with patch('pyperclip.paste', side_effect=clipboard_side_effect()):
        monitor = ClipboardMonitor(**mock_components)
        try:
            monitor.start_monitoring()
        except KeyboardInterrupt:
            pass

    # Check if error was logged
    assert "An error occurred" in caplog.text
    assert "File not found" in caplog.text
