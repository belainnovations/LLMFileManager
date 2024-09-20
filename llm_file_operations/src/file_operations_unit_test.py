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
    
@patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
def test_modify_file_replace(mock_file, file_operator, mock_context_matcher):
    mock_context_matcher.find_context_lines.return_value = (1, 2)
    instruction = {
        'start_context': 'line2',
        'end_context': 'line3',
        'code': 'new line2\nnew line3\n'
    }
    file_operator.modify_file('test.txt', 'REPLACE', instruction)
    mock_file.assert_any_call('test.txt', 'r', newline='')
    mock_file.assert_any_call('test.txt', 'w', newline='', encoding='utf-8')
    mock_file().writelines.assert_called_once_with(['line1\n', 'new line2\n', 'new line3\n'])

@patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\n')
def test_modify_file_insert(mock_file, file_operator, mock_context_matcher):
    mock_context_matcher.find_context_lines.return_value = (1, None)
    instruction = {
        'start_context': 'line2',
        'code': 'new line\n'
    }
    file_operator.modify_file('test.txt', 'INSERT', instruction)
    mock_file.assert_any_call('test.txt', 'r', newline='')
    mock_file.assert_any_call('test.txt', 'w', newline='', encoding='utf-8')
    mock_file().writelines.assert_called_once_with(['line1\n', 'new line\n', 'line2\n', 'line3\n'])

@patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\nline4\n')
def test_modify_file_delete(mock_file, file_operator, mock_context_matcher):
    mock_context_matcher.find_context_lines.return_value = (1, 2)
    instruction = {
        'start_context': 'line2',
        'end_context': 'line3'
    }
    file_operator.modify_file('test.txt', 'DELETE', instruction)
    mock_file.assert_any_call('test.txt', 'r', newline='')
    mock_file.assert_any_call('test.txt', 'w', newline='', encoding='utf-8')
    mock_file().writelines.assert_called_once_with(['line1\n', 'line4\n'])
@patch('os.path.exists')
@patch('shutil.rmtree')
def test_delete_folder(mock_rmtree, mock_exists, file_operator):
    mock_exists.return_value = True
    file_operator.delete_folder('test/folder')
    mock_rmtree.assert_called_once_with('test/folder')
# Test cases will be added here
