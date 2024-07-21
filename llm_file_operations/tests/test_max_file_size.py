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

def test_max_file_size():
    config = load_config()
    error_handler = ErrorHandler()
    context_matcher = ContextMatcher()
    file_operator = FileOperator(context_matcher, error_handler, config)

    max_file_size = config.get('file_operations', {}).get('max_file_size', 10485760)
    print(f"Configured max file size: {max_file_size} bytes")

    # Create a temporary file larger than the max_file_size
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'0' * (max_file_size + 1))
        temp_file_path = temp_file.name

    # Attempt to modify the file (which should fail due to size)
    instruction = {
        'action': 'REPLACE',
        'file': temp_file_path,
        'start_context': '',
        'end_context': '',
        'code': 'This should not be written'
    }

    result = file_operator.execute(instruction)
    print(f"Result of file operation: {result}")

    # Clean up
    os.unlink(temp_file_path)

if __name__ == "__main__":
    test_max_file_size()
