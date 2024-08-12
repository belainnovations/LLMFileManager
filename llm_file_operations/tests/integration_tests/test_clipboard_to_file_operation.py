import pytest
from unittest.mock import patch, MagicMock
from src.clipboard_monitor import ClipboardMonitor
from src.file_operations import FileOperator
from src.instruction_parser import InstructionParser
from src.error_handler import ErrorHandler
import os
import logging

@pytest.fixture
def mock_components():
    return {
        'instruction_parser': MagicMock(spec=InstructionParser),
        'file_operator': MagicMock(spec=FileOperator),
        'error_handler': MagicMock(spec=ErrorHandler),
        'config': {'clipboard_check_interval': 0.1}
    }

def test_clipboard_to_file_creation(mock_components, tmp_path, caplog):
    caplog.set_level(logging.DEBUG)

    initial_content = "Initial clipboard content"
    clipboard_content = """
    LLMOP:
      version: "1.0"
      action: CREATE_FILE
      file: test_file.txt
      language: text
      description: Create a new text file
      execution_key: "EXECUTE_LLM_INSTRUCTION"
      code: |-
        This is a test file content.
    """
    mock_components['instruction_parser'].parse.return_value = {
        'action': 'CREATE_FILE',
        'file': 'test_file.txt',
        'code': 'This is a test file content.'
    }

    def clipboard_side_effect():
        logging.debug("Clipboard side effect: Yielding initial content")
        yield initial_content
        logging.debug("Clipboard side effect: Yielding LLMOP content")
        yield clipboard_content
        logging.debug("Clipboard side effect: Raising KeyboardInterrupt")
        raise KeyboardInterrupt

    with patch('pyperclip.paste', side_effect=clipboard_side_effect()):
        logging.debug("Creating ClipboardMonitor instance")
        monitor = ClipboardMonitor(**mock_components)
        try:
            logging.debug("Starting monitoring")
            monitor.start_monitoring()
        except KeyboardInterrupt:
            logging.debug("KeyboardInterrupt caught")

    logging.debug("Asserting file_operator.execute was called")
    mock_components['file_operator'].execute.assert_called_once()
    args, _ = mock_components['file_operator'].execute.call_args
    assert args[0]['action'] == 'CREATE_FILE'
    assert args[0]['file'] == 'test_file.txt'
    logging.debug("Test completed successfully")

    # Print captured logs
    print("\nCaptured logs:")
    print(caplog.text)

def test_clipboard_to_file_modification(mock_components, tmp_path, caplog):
    caplog.set_level(logging.DEBUG)
    logging.debug("Starting test_clipboard_to_file_modification")

    initial_content = "Initial content"
    file_path = tmp_path / "existing_file.txt"
    with open(file_path, 'w') as f:
        f.write(initial_content)

    clipboard_content = """
    LLMOP:
      version: "1.0"
      action: REPLACE
      file: existing_file.txt
      language: text
      description: Modify existing file
      execution_key: "EXECUTE_LLM_INSTRUCTION"
      start_context: |-
        Initial content
      end_context: |-
        Initial content
      code: |-
        Modified content
    """
    mock_components['instruction_parser'].parse.return_value = {
        'action': 'REPLACE',
        'file': 'existing_file.txt',
        'start_context': 'Initial content',
        'end_context': 'Initial content',
        'code': 'Modified content'
    }

    def clipboard_side_effect():
        logging.debug("Clipboard side effect: Yielding initial content")
        yield "Initial clipboard content"
        logging.debug("Clipboard side effect: Yielding LLMOP content")
        yield clipboard_content
        logging.debug("Clipboard side effect: Raising KeyboardInterrupt")
        raise KeyboardInterrupt

    with patch('pyperclip.paste', side_effect=clipboard_side_effect()):
        logging.debug("Creating ClipboardMonitor instance")
        monitor = ClipboardMonitor(**mock_components)
        try:
            logging.debug("Starting monitoring")
            monitor.start_monitoring()
        except KeyboardInterrupt:
            logging.debug("KeyboardInterrupt caught")

    logging.debug("Asserting file_operator.execute was called")
    mock_components['file_operator'].execute.assert_called_once()
    args, _ = mock_components['file_operator'].execute.call_args
    assert args[0]['action'] == 'REPLACE'
    assert args[0]['file'] == 'existing_file.txt'
    logging.debug("Test completed successfully")

    # Print captured logs
    print("\nCaptured logs:")
    print(caplog.text)
