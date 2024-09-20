import pytest
from pytest import ExitCode
import os
import sys
from datetime import datetime
from io import StringIO

def get_version():
    version_file = os.path.join("tests", "version.txt")
    with open(version_file, "r") as f:
        return f.read().strip()

def generate_test_report(exit_codes, outputs):
    version = get_version()
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_prefix = now.strftime("%Y%m%d_%H%M")
    report_dir = os.path.join("tests", "test_reports", date)
    os.makedirs(report_dir, exist_ok=True)

    report_filename = f"{time_prefix}_test_report_v{version}.md"
    report_path = os.path.join(report_dir, report_filename)

    with open(report_path, "w") as report_file:
        report_file.write(f"# Test Report v{version}\n\n")
        report_file.write(f"Date: {date}\n\n")
        for i, (exit_code, output) in enumerate(zip(exit_codes, outputs), 1):
            report_file.write(f"## Test Run {i}\n\n")
            report_file.write("### Test Results\n\n")
            report_file.write(output.replace('\\', '/'))  # Replace backslashes with forward slashes
            report_file.write(f"\nExit Code: {exit_code}\n\n")
            report_file.write("="*80 + "\n\n")

# Change to the root directory of the project
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(project_root)

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(project_root, 'src'))

all_outputs = []
all_exit_codes = []

# Run tests multiple times
for _ in range(3):
    output_buffer = StringIO()
    sys.stdout = output_buffer

    # Include src, integration_tests, and system_tests directories
    exit_code = pytest.main(["-v", "--tb=short", "src", "tests/integration_tests", "tests/system_tests", "--ignore=tests/llm_interface"])

    sys.stdout = sys.__stdout__
    output = output_buffer.getvalue()

    all_outputs.append(output)
    all_exit_codes.append(exit_code)

    # Print the result of each run
    print(output)
    if exit_code == ExitCode.OK:
        print(f"Test run {_+1} passed successfully!")
    else:
        print(f"Test run {_+1} failed with exit code: {exit_code}")

# Generate test report with all results
generate_test_report(all_exit_codes, all_outputs)

# Print overall result
if all(code == ExitCode.OK for code in all_exit_codes):
    print("All test runs for the main project passed successfully!")
else:
    print("Some test runs failed. Check the test report for details.")

    # Run all tests in the src directory, integration_tests, and system_tests, excluding the llm_interface subproject
    exit_code = pytest.main(["-v", "--tb=short", "src", "tests/integration_tests", "tests/system_tests", "--ignore=tests/llm_interface"])

    # Print the result
    if exit_code == ExitCode.OK:
        print("All tests for the main project passed successfully!")
    else:
        print(f"Tests failed with exit code: {exit_code}")
