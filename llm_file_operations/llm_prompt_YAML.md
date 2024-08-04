# LLM File Operation Instructions

LLM commands are used to perform file and folder operations in your project. Use the following YAML format for all LLM instructions:

```yaml
LLMOP:
  version: "1.0"
  action: [CREATE_FILE|CREATE_FOLDER|REPLACE|INSERT|DELETE|DELETE_FILE|DELETE_FOLDER]
  file: [relative_path_from_project_root]
  language: [file_extension_or_language_name]
  description: [brief description of the change]
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    [exact start context, including indentation]
  end_context: |-
    [exact end context, including indentation]
  code: |-
    [exact code to be inserted or used for replacement, including indentation]
```

## Important Guidelines:

1. Ensure proper YAML indentation and format.
2. The `execution_key` must be exactly "EXECUTE_LLM_INSTRUCTION" for safety.
3. For `start_context` and `end_context`, provide contexts that uniquely identify the target location in the file. Pay close attention to line numbers and ensure that the contexts accurately represent the beginning and end of the section you intend to modify.
4. For REPLACE and DELETE actions, the first line of the start_context is the first line to be replaced, and the last line of the end_context is the last line to be replaced. These first and last lines will be overwritten.
5. The context must match exactly with the content in the file, including indentation and whitespace.
6. If a single line is not unique, include additional lines to ensure uniqueness.
7. Use `|-` for multi-line strings (start_context, end_context, and code) to preserve newlines but trim the final newline.
8. Maintain consistent indentation within the multi-line strings.
9. When using REPLACE or DELETE actions, ensure that the start_context and end_context precisely bound the intended section of code, including the correct line numbers.

## Best Practices for Context Selection:

- Always double-check the line numbers of your start_context and end_context.
- Use IDE features or text editor line numbers to ensure accuracy.
- When in doubt, include one line before and after your intended section to provide clear boundaries.
- For functions or methods, use the function definition as the start_context and the last line of the function body as the end_context.
## Context Uniqueness

Ensuring context uniqueness is crucial for accurate file modifications. Both start_context and end_context must be unique within the file. Here are examples of correct and incorrect context selections:

Correct (unique):
```yaml
start_context: |-
  def unique_function_name():
    """Unique docstring for this function"""
end_context: |-
  return result  # Unique comment for this function
```

Incorrect (not unique):
```yaml
start_context: |-
  def process_data():
end_context: |-
  return result
```

Always verify that your chosen contexts appear only once in the target file.
## Handling Complex Scenarios

When dealing with more intricate code structures, consider these strategies:

1. Nested Functions or Classes:
   - Include the outer function/class name in your context.
   Example:
   ```yaml
   start_context: |-
     class OuterClass:
       def inner_method(self):
         """Unique docstring for inner_method"""
   end_context: |-
     # End of inner_method
   ```

2. Multiple Similar Functions:
   - Use unique attributes like function arguments or docstrings.
   Example:
   ```yaml
   start_context: |-
     def process_data(input_type="csv"):
       """Process data from CSV files"""
   end_context: |-
     return processed_data  # End of CSV processing
   ```

3. Large Code Blocks:
   - Use the beginning and end of the block, including unique identifiers.
   Example:
   ```yaml
   start_context: |-
     # Start of data transformation block
     def transform_data():
   end_context: |-
     # End of data transformation block
     return transformed_data
   ```

These strategies help maintain precision in complex code structures.
## Understanding start_context and end_context

The start_context and end_context are crucial for precise file modifications. Here's how they work:

1. Inclusive Boundaries:
   - The start_context represents the first line to be affected.
   - The end_context represents the last line to be affected.
   - Both start and end lines are included in the modification or deletion.

2. Action-specific Usage:
   - For REPLACE and DELETE: Both start_context and end_context are required.
   - For INSERT: Only start_context is needed. The new code is inserted before this line.

3. Matching Behavior:
   - The system searches for exact matches, including whitespace and indentation.
   - The first occurrence of the start_context is used if multiple matches exist.

4. Context Selection Tips:
   - For functions: Use the function definition as start_context and the last line (often a return statement) as end_context.
   - For class methods: Include the method definition in start_context and the last line of the method in end_context.
   - For specific code blocks: Use unique comments or docstrings to mark the start and end.

Example of proper context usage:

```yaml
LLMOP:
  version: "1.0"
  action: REPLACE
  file: src/example.py
  language: python
  description: Update a specific function
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def process_data(input_data):
        """Process the input data"""
  end_context: |-
    return processed_data
  code: |-
    def process_data(input_data):
        """Process the input data using an improved algorithm"""
        # New implementation
        processed_data = advanced_processing(input_data)
        return processed_data
```

In this example, the entire function from its definition to the return statement will be replaced.


## Example: Precise Context Selection for INSERT

Consider the following file content:

```python
import pytest
from main import main

# Add your unit tests for the main function here
```

To insert new imports and tests after the existing imports but before the comment, use this LLMOP command:

```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example_file.py
  language: python
  description: Add new imports and tests
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    
    # Add your unit tests for the main function here
  code: |-
    import yaml
    from unittest.mock import patch, mock_open

    def test_new_functionality():
        # Test code here
        pass
```

After execution, the file will look like this:

```python
import pytest
from main import main
import yaml
from unittest.mock import patch, mock_open

def test_new_functionality():
    # Test code here
    pass

# Add your unit tests for the main function here
```

This example demonstrates how to precisely select the insertion point to maintain the desired file structure.
Remember, precise context selection is key to accurate and safe file modifications.
## Detailed Context Selection Guidelines:

When selecting contexts for your LLMOP commands, consider the following:

1. Uniqueness: Ensure both start_context and end_context are unique within the file.
   - Use distinctive function names, comments, or code patterns.
   - Include enough lines to guarantee uniqueness.

2. Precision: Be as precise as possible to target the exact location.
   - For functions, use the function definition (including anything else that belongs to the function, for example decorators) as start_context and the last line as end_context.
   - For class methods, include the class name and method definition.

3. Line Numbers: Pay attention to line numbers, especially for REPLACE and DELETE actions.
   - The first line of start_context is the first line to be affected.
   - The last line of end_context is the last line to be affected.

4. Nested Structures: For nested functions or classes, provide sufficient context.
   - Include parent class or function names, if needed, to avoid ambiguity.

5. Comments and Docstrings: Utilize unique comments or docstrings as part of your context.
   - These can provide clear markers for start and end points.

6. Whitespace and Indentation: Preserve exact whitespace and indentation in your contexts.
   - The matcher is sensitive to these details.

By following these detailed guidelines, you can create more accurate and reliable LLMOP commands.
## Context Selection Guidelines:

- Choose the shortest possible context that uniquely identifies the target location.
- Prefer using function or class definitions, unique comments, or other distinctive lines as context.
- Ensure the chosen context appears only once in the entire file.
- Include surrounding lines only if necessary to achieve uniqueness.
- For REPLACE and DELETE operations, make sure both start and end contexts are unique and correctly bound the target section.

## Action-Specific Instructions:

### CREATE_FILE
- Used to create a new file.
- Automatically creates all non-existent folders in the file path.
- Requires only the `code` section.
- Omit `start_context` and `end_context`.

### CREATE_FOLDER
- Used to create a new folder.
- Does not require `start_context`, `end_context`, or `code` sections.

### REPLACE
- Used to replace a section of an existing file.
- Requires both `start_context` and `end_context`.
- Both contexts must uniquely identify the section to be replaced.

### INSERT
- Used to insert code at a specific point in the file.
- Requires only the `start_context`.
- The new code will be inserted immediately before the `start_context`.

### DELETE
- Used to remove a section of code from a file.
- Requires both `start_context` and `end_context`.
- Both contexts must uniquely identify the section to be deleted.

### DELETE_FILE
- Used to delete a specific file.
- Does not require `start_context`, `end_context`, or `code` sections.

### DELETE_FOLDER
- Used to delete a folder and all its contents.
- Does not require `start_context`, `end_context`, or `code` sections.

## Examples:

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
        """
        A simple greeting function.

        Args:
        name (str): The name of the person to greet.

        Returns:
        str: A greeting message.
        """
        return f"Hello, {name}! Welcome to our project."

    if __name__ == "__main__":
        print(greet("User"))
```

2. Replacing a section in an existing file (using minimal unique contexts):

```yaml
LLMOP:
  version: "1.0"
  action: REPLACE
  file: example/existing_file.py
  language: python
  description: Replace the greet function with an enhanced version
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def greet(name):
  end_context: |-
    if __name__ == "__main__":
  code: |-
    def greet(name, time_of_day=""):
        """
        An enhanced greeting function.

        Args:
        name (str): The name of the person to greet.
        time_of_day (str, optional): The time of day (e.g., "morning", "afternoon", "evening").

        Returns:
        str: A personalized greeting message.
        """
        if time_of_day:
            return f"Good {time_of_day}, {name}! Welcome to our project."
        else:
            return f"Hello, {name}! Welcome to our project at any time of day."

    def get_time_of_day():
        """
        Determine the time of day based on the current hour.

        Returns:
        str: A string representing the time of day ("morning", "afternoon", or "evening").
        """
        import datetime
        current_hour = datetime.datetime.now().hour
        if 5 <= current_hour < 12:
            return "morning"
        elif 12 <= current_hour < 18:
            return "afternoon"
        else:
            return "evening"
```

3. Inserting code (using a single unique line as context):

```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example/existing_file.py
  language: python
  description: Insert a new function before the greet function
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def greet(self, name):
  code: |-
    def validate_name(name):
        """
        Validate the given name.

        Args:
        name (str): The name to validate.

        Returns:
        bool: True if the name is valid, False otherwise.
        """
        return bool(name and name.strip())

```

Remember: The contexts must match exactly with the content in the file, including indentation and whitespace. Choose the shortest unique context possible to ensure accurate and safe file modifications.

## Verifying LLMOP Commands

Before executing an LLMOP command, verify its correctness:

1. Context Uniqueness: Ensure start_context and end_context are unique within the target file.
2. Context Boundaries: Verify that contexts include sufficient surrounding code for accurate targeting.
3. Action Appropriateness: Confirm the action matches your intended operation.
4. File Paths and Extensions: Double-check the accuracy of file paths and extensions.
5. Code Content: Review the code section for correctness and proper indentation.
6. Execution Key: Verify the execution_key is exactly "EXECUTE_LLM_INSTRUCTION".

Taking these verification steps will significantly reduce the risk of unintended file modifications.
## Troubleshooting Common Issues

When encountering problems with LLMOP commands, consider these common issues and solutions:

1. "Context not found":
   - Verify the exact content and indentation of your contexts.
   - Check for hidden characters or trailing whitespace.

2. "Multiple matches found":
   - Expand your context to include more unique surrounding code.
   - Use line numbers or additional unique identifiers in your context.

3. "File extension not allowed":
   - Check the config file for the list of allowed extensions.
   - For special files like .gitignore, ensure they're properly handled.

4. Unexpected modifications:
   - Double-check the line numbers in your contexts.
   - Ensure the end_context doesn't include lines you want to preserve.

5. YAML parsing errors:
   - Verify proper indentation in your LLMOP command.
   - Use a YAML validator to check your command structure.

By addressing these common issues, you can improve the reliability of your LLMOP commands.
# LLM Prompt Guidelines Update: Handling Multi-line Strings in Python Code

When generating LLMOP commands that include Python code with multi-line strings, follow these guidelines:

1. Use string concatenation for multi-line strings within Python code blocks:

    ```python
    mock_generate.return_value = (
        "LLMOP:\n"
        "  version: '1.0'\n"
        "  action: CREATE_FILE\n"
        "  file: test.txt\n"
        "  content: 'Hello, World!'\n"
        "  execution_key: 'EXECUTE_LLM_INSTRUCTION'"
    )
    ```

2. Avoid using triple-quoted strings ("""...""") for YAML content within Python code, as it can cause YAML parsing errors.

3. Ensure proper indentation of the concatenated strings to maintain readability.

4. When representing YAML content within Python strings, use explicit newline characters (\n) to separate lines.

5. For complex YAML structures, consider using a YAML library to generate the string programmatically.


By following these guidelines, we can prevent YAML parsing errors and ensure that the LLMOP commands are correctly formatted and executed.
