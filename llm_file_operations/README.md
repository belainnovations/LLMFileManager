# LLM File Operations

LLM File Operations is a powerful tool for performing file and folder operations in your project using YAML-based instructions.

## Installation

You can install LLM File Operations using pip:

```bash
pip install llm_file_operations
```

Alternatively, you can clone the repository:

```bash
git clone https://github.com/belainnovations/LLMFileManager
cd llm_file_operations
pip install -r requirements.txt
```

## Quick Start Guide

1. Install LLM File Operations as described above.

2. Run the main script:
   ```bash
   llm_file_operations
   ```
   Or if you cloned the repository:
   ```bash
   python src/main.py
   ```

3. Use a chat application to generate LLMOP commands and copy them to your clipboard.

4. The system will automatically detect and execute the instruction.

## Usage with Chat Applications

To use LLM File Operations with chat applications like ChatGPT, Claude, or Cody:

1. Start the LLM File Operations application on your local machine.

2. In your chat application, provide the content of `llm_prompt_YAML.md` to the AI. You can do this by:
   - Uploading the file and instructing the AI to "Take the context as instructions."
   - Copy-pasting the content of `llm_prompt_YAML.md` and giving the same instruction.

3. Instruct the AI to "Always put each LLMOP command in a separate code box."

4. Request the AI to generate LLMOP commands for your desired file operations.

5. Copy the generated LLMOP command (in its code box) to your clipboard.

6. The LLM File Operations application will automatically detect and execute the instruction.

## Basic Usage Examples

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

2. Modifying an existing file:

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


## Configuration

The `config.yaml` file in the `config` directory allows you to customize various settings. When specifying paths in the configuration, use double backslashes for Windows paths:

```yaml
# Root directory for file operations (relative to the project root)
# Use "." for the current directory
project_root: "llm_file_operations\\docs"
```

This ensures proper path handling across different operating systems.

## Running from Different Directories

After installing LLM File Operations via pip, you can run it from any directory:

```bash
cd /path/to/your/project
llm_file_operations
```

The current working directory will be used as the root for all file operations.

For more detailed information and advanced usage, please refer to the documentation in the `docs` folder.

## Support

If you encounter any issues or have questions, please open an issue on our GitHub Issues page.

## Contributing

Contributions are welcome! Please read our contributing guidelines for details on how to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
