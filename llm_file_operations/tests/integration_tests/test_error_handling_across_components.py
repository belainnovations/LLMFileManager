import pytest
from unittest.mock import patch, MagicMock, call
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
    caplog.set_level(logging.DEBUG)

    # Simulate an error in instruction parsing
    mock_components['instruction_parser'].parse.side_effect = ValueError("Invalid instruction format")

    clipboard_contents = [
        "Initial content",
        "Invalid LLMOP instruction",
        "LLMOP:\n  version: '1.0'\n  action: CREATE_FILE\n  file: test.txt\n  code: Test content",
        "Another invalid instruction"
    ]

    stop_flag = threading.Event()
    paste_call_count = 0

    def mock_paste():
        nonlocal paste_call_count
        content = clipboard_contents[paste_call_count % len(clipboard_contents)]
        paste_call_count += 1
        print(f"mock_paste called {paste_call_count} times, returning: {content[:20]}...")
        if paste_call_count >= 10:
            stop_flag.set()
        return content

    with patch('pyperclip.paste', side_effect=mock_paste):
        monitor = ClipboardMonitor(**mock_components)

        def run_monitor():
            print("Starting monitor")
            try:
                monitor.start_monitoring()
            except Exception as e:
                print(f"Monitor stopped due to: {str(e)}")

        thread = threading.Thread(target=run_monitor)
        thread.start()

        stop_flag.wait(timeout=3)  # Wait for up to 3 seconds

        thread.join(timeout=1)

    print(f"Captured logs: {caplog.text}")
    print(f"Instruction parser called: {mock_components['instruction_parser'].parse.called}")
    print(f"Instruction parser call count: {mock_components['instruction_parser'].parse.call_count}")
    print(f"Instruction parser call args: {mock_components['instruction_parser'].parse.call_args_list}")

    assert "An error occurred: Invalid instruction format" in caplog.text
    assert mock_components['instruction_parser'].parse.called
    assert mock_components['instruction_parser'].parse.call_count > 0

def test_error_logging(mock_components, caplog):
    caplog.set_level(logging.DEBUG)

    # Simulate successful parsing but error in file operation
    mock_components['instruction_parser'].parse.return_value = MagicMock()
    mock_components['file_operator'].execute.side_effect = IOError("File not found")

    clipboard_contents = [
        "Initial content",
        """
        LLMOP:
          version: "1.0"
          action: CREATE_FILE
          file: non_existent/test.txt
          language: text
          description: Create a new text file
          execution_key: "EXECUTE_LLM_INSTRUCTION"
          code: |-
            Test content
        """,
        "Another content"
    ]

    stop_flag = threading.Event()
    paste_call_count = 0

    def mock_paste():
        nonlocal paste_call_count
        content = clipboard_contents[paste_call_count % len(clipboard_contents)]
        paste_call_count += 1
        print(f"mock_paste called {paste_call_count} times, returning: {content[:20]}...")
        if paste_call_count >= 10:
            stop_flag.set()
        return content

    with patch('pyperclip.paste', side_effect=mock_paste):
        monitor = ClipboardMonitor(**mock_components)

        def run_monitor():
            print("Starting monitor")
            try:
                monitor.start_monitoring()
            except Exception as e:
                print(f"Monitor stopped due to: {str(e)}")

        thread = threading.Thread(target=run_monitor)
        thread.start()

        stop_flag.wait(timeout=3)  # Wait for up to 3 seconds

        thread.join(timeout=1)

    print(f"Captured logs: {caplog.text}")
    print(f"File operator called: {mock_components['file_operator'].execute.called}")
    print(f"File operator call count: {mock_components['file_operator'].execute.call_count}")
    print(f"File operator call args: {mock_components['file_operator'].execute.call_args_list}")

    assert "An error occurred: File not found" in caplog.text
    assert mock_components['instruction_parser'].parse.called
    assert mock_components['file_operator'].execute.called
    assert mock_components['file_operator'].execute.call_count > 0
    assert mock_components['file_operator'].execute.call_count > 0
