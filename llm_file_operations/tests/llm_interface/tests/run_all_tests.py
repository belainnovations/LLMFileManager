import pytest
import os
from pytest import ExitCode

if __name__ == "__main__":
    # Change to the root directory of the project
    os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

    # Run all tests
    exit_code = pytest.main(["-v", "--tb=short"])

    # Print the result
    if exit_code == ExitCode.OK:
        print("All tests passed successfully!")
    else:
        print(f"Tests failed with exit code: {exit_code}")
