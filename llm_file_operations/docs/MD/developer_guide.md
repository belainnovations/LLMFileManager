# LLM File Operations Developer's Guide

This document provides detailed information about the internal structure and components of the LLM File Operations system.

## Core Classes

### InstructionParser

Responsible for parsing YAML instructions and validating their structure.

#### Methods:
- `parse(content: str) -> dict`: Parses the YAML content and returns a dictionary of instructions.
- `validate_yaml_structure(parsed_yaml: dict) -> bool`: Validates the structure of the parsed YAML.

### FileOperator

Handles file and folder operations based on the parsed instructions.

#### Methods:
- `execute(instruction: dict) -> str`: Executes the given instruction and returns a result message.
- `create_file(file_path: str, content: str) -> str`: Creates a new file with the given content.
- `create_folder(folder_path: str) -> str`: Creates a new folder.
- `delete_file(file_path: str) -> str`: Deletes the specified file.
- `delete_folder(folder_path: str) -> str`: Deletes the specified folder and its contents.
- `modify_file(file_path: str, action: str, instruction: dict) -> str`: Modifies an existing file (REPLACE, INSERT, DELETE).

### ClipboardMonitor

Monitors the clipboard for new LLMOP instructions.

#### Methods:
- `start_monitoring() -> None`: Starts the clipboard monitoring process.
- `detect_format(content: str) -> str`: Detects the format of the clipboard content.

### ContextMatcher

Matches context within files for precise modifications.

#### Methods:
- `find_context_lines(lines: List[str], start_context: str, end_context: str) -> Tuple[int, int]`: Finds the start and end lines matching the given contexts.

### ErrorHandler

Handles and logs errors that occur during operations.

#### Methods:
- `handle_error(message: str) -> str`: Logs the error and returns an error message.

## Configuration

The `config/config.yaml` file contains settings that can be adjusted to customize the behavior of LLM File Operations. Refer to the comments in this file for details on each setting.

## Extending LLM File Operations

To add new actions or modify existing ones:

1. Update the `FileOperator` class in `file_operations.py`.
2. Modify the `validate_yaml_structure` method in `instruction_parser.py` if necessary.
3. Update the user guide and this developer's guide to reflect the changes.

For more information on contributing, please refer to the CONTRIBUTING.md file in the project root.