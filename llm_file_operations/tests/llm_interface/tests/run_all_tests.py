import pytest
import os

if __name__ == "__main__":
    # Change to the root directory of the project
    os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    
    # Run all tests
    pytest.main(["-v", "--tb=short", "--cov=llm_file_operations", "--cov-report=term-missing"])