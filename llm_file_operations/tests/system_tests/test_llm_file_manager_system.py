import pytest
import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

# Import necessary modules
from src.clipboard_monitor import ClipboardMonitor
from src.instruction_parser import InstructionParser
from src.file_operations import FileOperator
from src.error_handler import ErrorHandler

# System test cases will be implemented here