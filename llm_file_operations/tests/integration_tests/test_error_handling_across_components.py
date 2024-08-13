import pytest
from unittest.mock import patch, MagicMock
from src.clipboard_monitor import ClipboardMonitor
from src.instruction_parser import InstructionParser
from src.file_operations import FileOperator
from src.error_handler import ErrorHandler
import logging
import threading
import time

@pytest.fixture
def mock_components():
    return {
        'instruction_parser': MagicMock(spec=InstructionParser),
        'file_operator': MagicMock(spec=FileOperator),
        'error_handler': MagicMock(spec=ErrorHandler),
        'config': {'clipboard_check_interval': 0.1}
    }

@pytest.fixture
def capture_output(capsys):
    yield capsys.readouterr

def test_error_propagation(mock_components, caplog):
    caplog.set_level(logging.ERROR, logger="src.clipboard_monitor")

    # Simulate an error in instruction parsing
    mock_components['instruction_parser'].parse.side_effect = ValueError("Invalid instruction format")

    clipboard_content = "Invalid LLMOP instruction"

    stop_flag = threading.Event()

    def mock_paste():
        if not stop_flag.is_set():
            return clipboard_content
        raise KeyboardInterrupt

    with patch('pyperclip.paste', side_effect=mock_paste):
        monitor = ClipboardMonitor(**mock_components)

        def run_monitor():
            try:
                monitor.start_monitoring()
            except KeyboardInterrupt:
                pass

        thread = threading.Thread(target=run_monitor)
        thread.start()
        time.sleep(0.5)  # Allow time for error to occur and be logged
        stop_flag.set()
        thread.join(timeout=1)

    # Check if error was logged
    assert "An error occurred" in caplog.text
    assert "Invalid instruction format" in caplog.text

def test_error_logging(mock_components, caplog):
    caplog.set_level(logging.ERROR, logger="src.clipboard_monitor")

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

    stop_flag = threading.Event()

    def mock_paste():
        if not stop_flag.is_set():
            return clipboard_content
        raise KeyboardInterrupt

    with patch('pyperclip.paste', side_effect=mock_paste):
        monitor = ClipboardMonitor(**mock_components)

        def run_monitor():
            try:
                monitor.start_monitoring()
            except KeyboardInterrupt:
                pass

        thread = threading.Thread(target=run_monitor)
        thread.start()
        time.sleep(0.5)  # Allow time for error to occur and be logged
        stop_flag.set()
        thread.join(timeout=1)

    # Check if error was logged
    assert "An error occurred" in caplog.text
    assert "File not found" in caplog.text
