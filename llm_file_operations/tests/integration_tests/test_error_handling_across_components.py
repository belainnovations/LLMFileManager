import pytest
from unittest.mock import patch, MagicMock
from src.clipboard_monitor import ClipboardMonitor
from src.instruction_parser import InstructionParser
from src.file_operations import FileOperator
from src.error_handler import ErrorHandler
import logging
import threading
import time
import ctypes

logger = logging.getLogger(__name__)

def terminate_thread(thread):
    if not thread.is_alive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("Invalid thread ID")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

@pytest.fixture
def mock_components():
    return {
        'instruction_parser': MagicMock(spec=InstructionParser),
        'file_operator': MagicMock(spec=FileOperator),
        'error_handler': MagicMock(spec=ErrorHandler),
        'config': {'clipboard_check_interval': 0.1}
    }

@pytest.fixture(autouse=True)
def cleanup():
    threads_before = set(threading.enumerate())
    yield
    threads_after = set(threading.enumerate())
    for thread in threads_after - threads_before:
        if thread.is_alive():
            logger.warning(f"Forcefully terminating thread: {thread.name}")
            terminate_thread(thread)
    logging.getLogger().handlers.clear()

def test_error_propagation(mock_components, caplog):
    caplog.set_level(logging.DEBUG)
    mock_components['instruction_parser'].parse.side_effect = ValueError("Invalid instruction format")

    stop_event = threading.Event()

    def monitored_start_monitoring():
        monitor = ClipboardMonitor(**mock_components)
        try:
            while not stop_event.is_set():
                try:
                    monitor.start_monitoring()
                except ValueError as e:
                    logger.error(f"Expected error: {str(e)}")
                stop_event.wait(0.1)
        except Exception as e:
            logger.error(f"Unexpected error in monitored_start_monitoring: {str(e)}")

    thread = threading.Thread(target=monitored_start_monitoring)
    thread.start()

    # Simulate clipboard change to trigger parsing
    with patch('pyperclip.paste', return_value="LLMOP: invalid content"):
        time.sleep(1)  # Allow time for the monitor to process the clipboard

    stop_event.set()
    thread.join(timeout=5)

    if thread.is_alive():
        terminate_thread(thread)

    print(f"Captured logs: {caplog.text}")
    assert "Expected error: Invalid instruction format" in caplog.text
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
