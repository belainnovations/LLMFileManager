import os
import sys
import tempfile

# Add the src directory to the Python path
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_dir)

from main import load_config
from file_operations import FileOperator
from error_handler import ErrorHandler
from context_matcher import ContextMatcher

def test_allowed_extensions():
    config = load_config()
    error_handler = ErrorHandler()
    context_matcher = ContextMatcher()
    file_operator = FileOperator(context_matcher, error_handler, config)

    allowed_extensions = config.get('file_operations', {}).get('allowed_extensions', [])
    print(f"Configured allowed extensions: {allowed_extensions}")

    # Test with allowed extension
    allowed_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
    allowed_file_path = allowed_file.name
    allowed_file.close()

    # Test with disallowed extension
    disallowed_file = tempfile.NamedTemporaryFile(suffix='.exe', delete=False)
    disallowed_file_path = disallowed_file.name
    disallowed_file.close()

    # Attempt to modify the allowed file
    allowed_instruction = {
        'action': 'REPLACE',
        'file': allowed_file_path,
        'start_context': '',
        'end_context': '',
        'code': 'This should be written'
    }

    # Attempt to modify the disallowed file
    disallowed_instruction = {
        'action': 'REPLACE',
        'file': disallowed_file_path,
        'start_context': '',
        'end_context': '',
        'code': 'This should not be written'
    }

    allowed_result = file_operator.execute(allowed_instruction)
    print(f"Result of allowed file operation: {allowed_result}")

    disallowed_result = file_operator.execute(disallowed_instruction)
    print(f"Result of disallowed file operation: {disallowed_result}")

    # Clean up
    os.unlink(allowed_file_path)
    os.unlink(disallowed_file_path)

if __name__ == "__main__":
    test_allowed_extensions()