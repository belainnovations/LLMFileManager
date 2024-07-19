## Running LLM File Operations in Different Directories

After installing LLM File Operations via pip, you can run it from any directory on your system. The current working directory will be used as the root for all file operations.

Example usage:

```bash
# Navigate to your first project
cd /home/user/project1
llm_file_operations
# All file operations will be relative to /home/user/project1

# Switch to another project
cd /home/user/project2
llm_file_operations
# File operations will now be relative to /home/user/project2
```

This flexibility allows you to easily use LLM File Operations across different projects or directories without needing to specify the root path each time. Just navigate to the desired directory and run the command.
# LLM File Operations User Guide

This guide provides detailed instructions on how to use the LLM File Operations tool effectively.

## Getting Started

1. Ensure you have Python 3.7+ installed on your system.
2. Clone the repository and install dependencies:
   ```
   git clone https://github.com/yourusername/llm_file_operations.git
   cd llm_file_operations
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```
   python src/main.py
   ```

## Using LLM File Operations

LLM File Operations uses YAML-formatted instructions to perform file and folder operations. Here's how to use it:

1. Provide the content of llm_prompt_YAML.md to your LLM system:
   - Upload the file and instruct the LLM to "Take the context as instructions."
   - Or copy-paste the content of llm_prompt_YAML.md and give the same instruction.
2. Instruct the LLM to "Always put each LLMOP command in a separate code box." This helps in many use cases to easily copy the command for activation.
3. Request the LLM to generate LLMOP commands for your desired file operations.
4. Copy the generated LLMOP command (in its code box) to your clipboard.
5. The system will automatically detect and execute the instruction.

### LLMOP Instruction Format

```yaml
LLMOP:
  version: "1.0"
  action: [ACTION_TYPE]
  file: [FILE_PATH]
  language: [LANGUAGE]
  description: [DESCRIPTION]
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    [START_CONTEXT]
  end_context: |-
    [END_CONTEXT]
  code: |-
    [CODE]
```

### Available Actions

- CREATE_FILE: Create a new file
- CREATE_FOLDER: Create a new folder
- REPLACE: Replace content in an existing file
- INSERT: Insert content into an existing file
- DELETE: Remove content from an existing file
- DELETE_FILE: Delete an existing file
- DELETE_FOLDER: Delete an existing folder

### Examples

1. Creating a new file:
```yaml
LLMOP:
  version: "1.0"
  action: CREATE_FILE
  file: example/new_file.py
  language: python
  description: Create a new Python file with a simple function
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  code: |-
    def greet(name):
        return f"Hello, {name}!"
```

2. Replacing content in an existing file:
```yaml
LLMOP:
  version: "1.0"
  action: REPLACE
  file: example/existing_file.py
  language: python
  description: Replace the greet function
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def greet(name):
  end_context: |-
    return f"Hello, {name}!"
  code: |-
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
```

## Troubleshooting

If you encounter any issues:
1. Check the console output for error messages.
2. Ensure your YAML syntax is correct.
3. Verify that the file paths in your instructions are correct.

For more detailed information, refer to the API documentation.
