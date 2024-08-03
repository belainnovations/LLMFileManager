import pytest
from unittest.mock import Mock, patch, mock_open
import shutil
from file_operations import FileOperator

@pytest.fixture
def mock_context_matcher():
    return Mock()

@pytest.fixture
def mock_error_handler():
    return Mock()

@pytest.fixture
def mock_config():
    return {
        'project_root': '.',
        'file_operations': {
            'max_file_size': 10485760,
            'allowed_extensions': ['.txt', '.py', '.md']
        }
    }

@pytest.fixture
def file_operator(mock_context_matcher, mock_error_handler, mock_config):
    return FileOperator(mock_context_matcher, mock_error_handler, mock_config)

@patch('os.path.exists')
@patch('os.makedirs')
@patch('builtins.open', new_callable=mock_open)
def test_create_file(mock_file, mock_makedirs, mock_exists, file_operator):
    mock_exists.return_value = False
    file_operator.create_file('test/path/file.txt', 'content')
    mock_makedirs.assert_called_once_with('test/path', exist_ok=True)
    mock_file.assert_called_once_with('test/path/file.txt', 'w', newline='')
    
    @patch('builtins.open', new_callable=mock_open, read_data='original content')
    def test_modify_file(mock_file, file_operator, mock_context_matcher):
        mock_context_matcher.find_context_lines.return_value = (1, 1)
        instruction = {
            'start_context': 'original',
            'end_context': 'content',
            'code': 'modified content'
        }
        file_operator.modify_file('test.txt', 'REPLACE', instruction)
        mock_file.assert_any_call('test.txt', 'r', newline='')
        mock_file.assert_any_call('test.txt', 'w', newline='')
        mock_file().write.assert_called_with('modified content')
    mock_file().write.assert_called_once_with('content')

@patch('os.makedirs')
def test_create_folder(mock_makedirs, file_operator):
    file_operator.create_folder('test/folder')
    mock_makedirs.assert_called_once_with('test/folder', exist_ok=True)

@patch('os.path.exists')
@patch('shutil.rmtree')
def test_delete_folder(mock_rmtree, mock_exists, file_operator):
    mock_exists.return_value = True
    file_operator.delete_folder('test/folder')
    mock_rmtree.assert_called_once_with('test/folder')

@patch('os.path.exists')
@patch('os.remove')
def test_delete_file(mock_remove, mock_exists, file_operator):
    mock_exists.return_value = True
    file_operator.delete_file('test/file.txt')
    mock_remove.assert_called_once_with('test/file.txt')

@patch('builtins.open', new_callable=Mock)
def test_modify_file_replace(mock_open, file_operator, mock_context_matcher):
    mock_file_content = ['line1\n', 'line2\n', 'line3\n']
    mock_open.return_value.__enter__.return_value.readlines.return_value = mock_file_content
    mock_context_matcher.find_context_lines.return_value = (1, 2)

    instruction = {
        'start_context': 'line2',
        'end_context': 'line3',
        'code': 'new line2\nnew line3\n'
    }

    file_operator.modify_file('test.txt', 'REPLACE', instruction)

    mock_open.assert_any_call('test.txt', 'r', newline='')
    mock_open.assert_any_call('test.txt', 'w', newline='')
    mock_open.return_value.__enter__.return_value.writelines.assert_called_once_with(
        ['line1\n', 'new line2\n', 'new line3\n']
    )

@patch('builtins.open', new_callable=Mock)
def test_modify_file_insert(mock_open, file_operator, mock_context_matcher):
    mock_file_content = ['line1\n', 'line2\n', 'line3\n']
    mock_open.return_value.__enter__.return_value.readlines.return_value = mock_file_content
    mock_context_matcher.find_context_lines.return_value = (1, None)

    instruction = {
        'start_context': 'line2',
        'code': 'new line\n'
    }

    file_operator.modify_file('test.txt', 'INSERT', instruction)

    mock_open.assert_any_call('test.txt', 'r', newline='')
    mock_open.assert_any_call('test.txt', 'w', newline='')
    mock_open.return_value.__enter__.return_value.writelines.assert_called_once_with(
        ['line1\n', 'new line\n', 'line2\n', 'line3\n']
    )

@patch('os.path.exists')
@patch('os.path.getsize')
def test_execute_file_size_limit(mock_getsize, mock_exists, file_operator, mock_error_handler):
    mock_exists.return_value = True
    mock_getsize.return_value = 20000000  # Larger than max_file_size

    instruction = {
        'action': 'REPLACE',
        'file': 'large_file.txt'
    }

    file_operator.execute(instruction)
    mock_error_handler.handle_error.assert_called_once_with("File size exceeds maximum allowed size: large_file.txt")

def test_execute_invalid_file_extension(file_operator, mock_error_handler):
    instruction = {
        'action': 'CREATE_FILE',
        'file': 'invalid.exe'
    }

    file_operator.execute(instruction)
    mock_error_handler.handle_error.assert_called_once_with("File extension not allowed: exe")

@patch('os.path.exists')
def test_delete_nonexistent_file(mock_exists, file_operator, mock_error_handler):
    mock_exists.return_value = False
    file_operator.delete_file('nonexistent.txt')
    mock_error_handler.handle_error.assert_called_once_with("File not found: nonexistent.txt")

@patch('os.makedirs')
def test_create_folder_permission_error(mock_makedirs, file_operator, mock_error_handler):
    mock_makedirs.side_effect = PermissionError("Permission denied")
    file_operator.create_folder('restricted/folder')
    mock_error_handler.handle_error.assert_called_once_with("Error creating folder: Permission denied")

def test_execute_unknown_action(file_operator, mock_error_handler):
    instruction = {
        'action': 'UNKNOWN_ACTION',
        'file': 'test.txt'
    }

    file_operator.execute(instruction)
    mock_error_handler.handle_error.assert_called_once_with("Unknown action: UNKNOWN_ACTION")
@patch('builtins.open', new_callable=Mock)
def test_modify_file_delete(mock_open, file_operator, mock_context_matcher):
    mock_file_content = ['line1\n', 'line2\n', 'line3\n', 'line4\n']
    mock_open.return_value.__enter__.return_value.readlines.return_value = mock_file_content
    mock_context_matcher.find_context_lines.return_value = (1, 2)

    instruction = {
        'start_context': 'line2',
        'end_context': 'line3'
    }

    file_operator.modify_file('test.txt', 'DELETE', instruction)

    mock_open.assert_any_call('test.txt', 'r', newline='')
    mock_open.assert_any_call('test.txt', 'w', newline='')
    mock_open.return_value.__enter__.return_value.writelines.assert_called_once_with(
        ['line1\n', 'line4\n']
    )
@patch('os.path.exists')
@patch('shutil.rmtree')
def test_delete_folder(mock_rmtree, mock_exists, file_operator):
    mock_exists.return_value = True
    file_operator.delete_folder('test/folder')
    mock_rmtree.assert_called_once_with('test/folder')
# Test cases will be added here
