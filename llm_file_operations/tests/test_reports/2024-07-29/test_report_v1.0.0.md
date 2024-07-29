# Test Report v1.0.0

Date: 2024-07-29

## Test Run 1

### Test Results

=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.11.4, pytest-8.2.2, pluggy-1.5.0 -- C:\ProgramData\anaconda3\envs\AG_Ex1\python.exe
cachedir: .pytest_cache
rootdir: c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations
plugins: anyio-4.2.0
collecting ... collected 7 items

src/clipboard_monitor_unit_test.py::test_clipboard_monitor_initialization PASSED                                                                                     [ 14%]
src/clipboard_monitor_unit_test.py::test_detect_format[LLMOP:\n  version: '1.0'-yaml] PASSED                                                                         [ 28%]
src/clipboard_monitor_unit_test.py::test_detect_format[###LLMOP_START###\nSome content-custom] PASSED                                                                [ 42%]
src/clipboard_monitor_unit_test.py::test_detect_format[Invalid content-None] PASSED                                                                                  [ 57%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_new_content PASSED                                                                                         [ 71%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling FAILED                                                                                      [ 85%]
src/clipboard_monitor_unit_test.py::test_clipboard_check_interval PASSED                                                                                             [100%]

================================================================================ FAILURES =================================================================================
__________________________________________________________________ test_start_monitoring_error_handling ___________________________________________________________________
src\clipboard_monitor_unit_test.py:64: in test_start_monitoring_error_handling
    mock_dependencies['error_handler'].error.assert_called_once_with(
C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py:950: in assert_called_once_with
    raise AssertionError(msg)
E   AssertionError: Expected 'error' to be called once. Called 0 times.
-------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
An error occurred. Check the log for details.
---------------------------------------------------------------------------- Captured log call ----------------------------------------------------------------------------
ERROR    clipboard_monitor:clipboard_monitor.py:44 An error occurred: Test error
Traceback (most recent call last):
  File "c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations\src\clipboard_monitor.py", line 21, in start_monitoring
    clipboard_content = pyperclip.paste()
                        ^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1124, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1128, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1187, in _execute_mock_call
    raise result
Exception: Test error
========================================================================= short test summary info =========================================================================
FAILED src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling - AssertionError: Expected 'error' to be called once. Called 0 times.
======================================================================= 1 failed, 6 passed in 1.74s =======================================================================

Exit Code: 1

================================================================================

## Test Run 2

### Test Results

=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.11.4, pytest-8.2.2, pluggy-1.5.0 -- C:\ProgramData\anaconda3\envs\AG_Ex1\python.exe
cachedir: .pytest_cache
rootdir: c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations
plugins: anyio-4.2.0
collecting ... collected 7 items

src/clipboard_monitor_unit_test.py::test_clipboard_monitor_initialization PASSED                                                                                     [ 14%]
src/clipboard_monitor_unit_test.py::test_detect_format[LLMOP:\n  version: '1.0'-yaml] PASSED                                                                         [ 28%]
src/clipboard_monitor_unit_test.py::test_detect_format[###LLMOP_START###\nSome content-custom] PASSED                                                                [ 42%]
src/clipboard_monitor_unit_test.py::test_detect_format[Invalid content-None] PASSED                                                                                  [ 57%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_new_content PASSED                                                                                         [ 71%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling FAILED                                                                                      [ 85%]
src/clipboard_monitor_unit_test.py::test_clipboard_check_interval PASSED                                                                                             [100%]

================================================================================ FAILURES =================================================================================
__________________________________________________________________ test_start_monitoring_error_handling ___________________________________________________________________
src\clipboard_monitor_unit_test.py:64: in test_start_monitoring_error_handling
    mock_dependencies['error_handler'].error.assert_called_once_with(
C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py:950: in assert_called_once_with
    raise AssertionError(msg)
E   AssertionError: Expected 'error' to be called once. Called 0 times.
-------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
An error occurred. Check the log for details.
---------------------------------------------------------------------------- Captured log call ----------------------------------------------------------------------------
ERROR    clipboard_monitor:clipboard_monitor.py:44 An error occurred: Test error
Traceback (most recent call last):
  File "c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations\src\clipboard_monitor.py", line 21, in start_monitoring
    clipboard_content = pyperclip.paste()
                        ^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1124, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1128, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1187, in _execute_mock_call
    raise result
Exception: Test error
========================================================================= short test summary info =========================================================================
FAILED src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling - AssertionError: Expected 'error' to be called once. Called 0 times.
======================================================================= 1 failed, 6 passed in 1.31s =======================================================================

Exit Code: 1

================================================================================

## Test Run 3

### Test Results

=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.11.4, pytest-8.2.2, pluggy-1.5.0 -- C:\ProgramData\anaconda3\envs\AG_Ex1\python.exe
cachedir: .pytest_cache
rootdir: c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations
plugins: anyio-4.2.0
collecting ... collected 7 items

src/clipboard_monitor_unit_test.py::test_clipboard_monitor_initialization PASSED                                                                                     [ 14%]
src/clipboard_monitor_unit_test.py::test_detect_format[LLMOP:\n  version: '1.0'-yaml] PASSED                                                                         [ 28%]
src/clipboard_monitor_unit_test.py::test_detect_format[###LLMOP_START###\nSome content-custom] PASSED                                                                [ 42%]
src/clipboard_monitor_unit_test.py::test_detect_format[Invalid content-None] PASSED                                                                                  [ 57%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_new_content PASSED                                                                                         [ 71%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling FAILED                                                                                      [ 85%]
src/clipboard_monitor_unit_test.py::test_clipboard_check_interval PASSED                                                                                             [100%]

================================================================================ FAILURES =================================================================================
__________________________________________________________________ test_start_monitoring_error_handling ___________________________________________________________________
src\clipboard_monitor_unit_test.py:64: in test_start_monitoring_error_handling
    mock_dependencies['error_handler'].error.assert_called_once_with(
C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py:950: in assert_called_once_with
    raise AssertionError(msg)
E   AssertionError: Expected 'error' to be called once. Called 0 times.
-------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
An error occurred. Check the log for details.
---------------------------------------------------------------------------- Captured log call ----------------------------------------------------------------------------
ERROR    clipboard_monitor:clipboard_monitor.py:44 An error occurred: Test error
Traceback (most recent call last):
  File "c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations\src\clipboard_monitor.py", line 21, in start_monitoring
    clipboard_content = pyperclip.paste()
                        ^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1124, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1128, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1187, in _execute_mock_call
    raise result
Exception: Test error
========================================================================= short test summary info =========================================================================
FAILED src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling - AssertionError: Expected 'error' to be called once. Called 0 times.
======================================================================= 1 failed, 6 passed in 1.28s =======================================================================

Exit Code: 1

================================================================================

## Test Run 4

### Test Results

=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.11.4, pytest-8.2.2, pluggy-1.5.0 -- C:\ProgramData\anaconda3\envs\AG_Ex1\python.exe
cachedir: .pytest_cache
rootdir: c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations
plugins: anyio-4.2.0
collecting ... collected 7 items

src/clipboard_monitor_unit_test.py::test_clipboard_monitor_initialization PASSED                                                                                     [ 14%]
src/clipboard_monitor_unit_test.py::test_detect_format[LLMOP:\n  version: '1.0'-yaml] PASSED                                                                         [ 28%]
src/clipboard_monitor_unit_test.py::test_detect_format[###LLMOP_START###\nSome content-custom] PASSED                                                                [ 42%]
src/clipboard_monitor_unit_test.py::test_detect_format[Invalid content-None] PASSED                                                                                  [ 57%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_new_content PASSED                                                                                         [ 71%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling FAILED                                                                                      [ 85%]
src/clipboard_monitor_unit_test.py::test_clipboard_check_interval PASSED                                                                                             [100%]

================================================================================ FAILURES =================================================================================
__________________________________________________________________ test_start_monitoring_error_handling ___________________________________________________________________
src\clipboard_monitor_unit_test.py:64: in test_start_monitoring_error_handling
    mock_dependencies['error_handler'].error.assert_called_once_with(
C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py:950: in assert_called_once_with
    raise AssertionError(msg)
E   AssertionError: Expected 'error' to be called once. Called 0 times.
-------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
An error occurred. Check the log for details.
---------------------------------------------------------------------------- Captured log call ----------------------------------------------------------------------------
ERROR    clipboard_monitor:clipboard_monitor.py:44 An error occurred: Test error
Traceback (most recent call last):
  File "c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations\src\clipboard_monitor.py", line 21, in start_monitoring
    clipboard_content = pyperclip.paste()
                        ^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1124, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1128, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1187, in _execute_mock_call
    raise result
Exception: Test error
========================================================================= short test summary info =========================================================================
FAILED src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling - AssertionError: Expected 'error' to be called once. Called 0 times.
======================================================================= 1 failed, 6 passed in 1.23s =======================================================================

Exit Code: 1

================================================================================

## Test Run 5

### Test Results

=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.11.4, pytest-8.2.2, pluggy-1.5.0 -- C:\ProgramData\anaconda3\envs\AG_Ex1\python.exe
cachedir: .pytest_cache
rootdir: c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations
plugins: anyio-4.2.0
collecting ... collected 7 items

src/clipboard_monitor_unit_test.py::test_clipboard_monitor_initialization PASSED                                                                                     [ 14%]
src/clipboard_monitor_unit_test.py::test_detect_format[LLMOP:\n  version: '1.0'-yaml] PASSED                                                                         [ 28%]
src/clipboard_monitor_unit_test.py::test_detect_format[###LLMOP_START###\nSome content-custom] PASSED                                                                [ 42%]
src/clipboard_monitor_unit_test.py::test_detect_format[Invalid content-None] PASSED                                                                                  [ 57%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_new_content PASSED                                                                                         [ 71%]
src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling FAILED                                                                                      [ 85%]
src/clipboard_monitor_unit_test.py::test_clipboard_check_interval PASSED                                                                                             [100%]

================================================================================ FAILURES =================================================================================
__________________________________________________________________ test_start_monitoring_error_handling ___________________________________________________________________
src\clipboard_monitor_unit_test.py:64: in test_start_monitoring_error_handling
    mock_dependencies['error_handler'].error.assert_called_once_with(
C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py:950: in assert_called_once_with
    raise AssertionError(msg)
E   AssertionError: Expected 'error' to be called once. Called 0 times.
-------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------
An error occurred. Check the log for details.
---------------------------------------------------------------------------- Captured log call ----------------------------------------------------------------------------
ERROR    clipboard_monitor:clipboard_monitor.py:44 An error occurred: Test error
Traceback (most recent call last):
  File "c:\Agy\Programming\BelAInnovations\Projects\LLMFileManager\llm_file_operations\src\clipboard_monitor.py", line 21, in start_monitoring
    clipboard_content = pyperclip.paste()
                        ^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1124, in __call__
    return self._mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1128, in _mock_call
    return self._execute_mock_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\ProgramData\anaconda3\envs\AG_Ex1\Lib\unittest\mock.py", line 1187, in _execute_mock_call
    raise result
Exception: Test error
========================================================================= short test summary info =========================================================================
FAILED src/clipboard_monitor_unit_test.py::test_start_monitoring_error_handling - AssertionError: Expected 'error' to be called once. Called 0 times.
======================================================================= 1 failed, 6 passed in 1.40s =======================================================================

Exit Code: 1

================================================================================

