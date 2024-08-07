# LLM File Operations (LLMOP) Command Guide

## Introduction

This guide explains how to generate LLMOP commands for file and folder operations. LLMOP commands use YAML format to specify actions on files and folders.

## LLMOP Command Structure

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

## Action Types and Context Selection

### CREATE_FILE

- Creates a new file
- Requires only the `code` section
- No `start_context` or `end_context` needed

Example: Before (File doesn't exist)

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: CREATE_FILE
  file: example.py
  language: python
  description: Create a new Python file with a greeting function
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  code: |-
    def greet(name):
        return f"Hello, {name}!"

    if __name__ == "__main__":
        print(greet("World"))
```

After:

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

Explanation: This command creates a new file named 'example.py' with a greeting function.

Negative Example:

```yaml
LLMOP:
  version: "1.0"
  action: CREATE_FILE
  file: example/new_file.py
  language: python
  description: Attempt to create a file with missing code section
  execution_key: "EXECUTE_LLM_INSTRUCTION"
```

Explanation: This command will fail because it's missing the required `code` section for CREATE_FILE action.

### CREATE_FOLDER

- Creates a new folder
- Doesn't require `start_context`, `end_context`, or `code` sections

Example: Before (Folder doesn't exist)

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: CREATE_FOLDER
  file: new_folder
  description: Create a new folder
  execution_key: "EXECUTE_LLM_INSTRUCTION"
```

After: A new folder named 'new_folder' is created.

Explanation: This command creates a new empty folder.

### REPLACE

- Replaces a section of an existing file
- Requires both `start_context` and `end_context`
- Contexts must uniquely identify the section to be replaced

Example: Before:

```python
def old_function():
    print("This is the old function")

# Other code here
```

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: REPLACE
  file: example.py
  language: python
  description: Replace old function with a new one
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def old_function():
  end_context: |-
    # Other code here
  code: |-
    def new_function():
        print("This is the new function")
        return True

    # Other code here
```

After:

```python
def new_function():
    print("This is the new function")
    return True

# Other code here
```

Explanation: This command replaces the old_function with new_function, including everything including the comment. The comment only shows up in the updated code because it was included in the code context.

Negative Example:

```yaml
LLMOP:
  version: "1.0"
  action: REPLACE
  file: example.py
  language: python
  description: Replace function with non-unique context
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def function():
  end_context: |-
    return result
  code: |-
    def new_function():
        return "New result"
```

Explanation: This command may lead to unintended modifications if there are multiple functions with similar structures in the file. The contexts are not unique enough.

### INSERT

- Inserts code at a specific point in the file
- Requires only the `start_context`
- New code is inserted immediately before the `start_context`

Example:
Before:

```python
def existing_function():
    pass

# End of file
```

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example.py
  language: python
  description: Insert a new function before the existing one
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def existing_function():
  code: |-
    def new_function():
        print("This is a new function")

```

After:

```python
def new_function():
    print("This is a new function")

def existing_function():
    pass

# End of file
```

Explanation: This command inserts a new function immediately before the existing function.


Example:

Adding Imports at the Beginning of a File:

When adding new imports to a file that already contains import statements, it's crucial to use the INSERT action correctly to avoid duplication. Here's an example of how to properly add new imports:

Before:

```python
import pyperclip
import time
import logging
````

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example.py
  language: python
  description: Add new imports at the beginning of the file
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    import pyperclip
  code: |-
    import pygame
    import os
```

After:

```python
import pygame
import os
import pyperclip
import time
import logging
```

Explanation: This command correctly inserts new import statements at the beginning of the file, before the existing imports, without duplicating any import statements.


Example: Inserting in the middle of a file

Before:

```python
def existing_function1():
    pass
# comment before 2nd function
def existing_function2():
    pass

def existing_function3():
    pass

# End of file
```

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example.py
  language: python
  description: Insert a new function before the existing one
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    # comment before 2nd function
    def existing_function2():
  code: |-
    def new_function():
        print("This is a new function")

```

After:

```python
def existing_function1():
    pass

def new_function():
    print("This is a new function")

# comment before 2nd function
def existing_function2():
    pass

def existing_function3():
    pass

# End of file
```

Explanation: This example demonstrates that the INSERT operation adds the new function immediately before the line specified in the start_context. The start_context line itself is not modified or repeated in the inserted code. This ensures that the new content is inserted at the correct location without duplicating any existing code. It's crucial to understand that the start_context is used as a reference point for insertion, not as part of the inserted content.


Negative Example:

```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example.py
  language: python
  description: Attempt to insert at the end of file
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    # End of file
  code: |-
    def new_function():
        print("This won't be inserted at the end")
```

Explanation: This command won't insert the new function at the end of the file. INSERT action adds content before the start_context, so this will insert before the last line instead of after it.


Negative Example:

```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example.py
  language: python
  description: Add new imports incorrectly
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    import existing_module
  code: |-
    import new_module1
    import new_module2
    import existing_module
```

Explanation: This command incorrectly adds new imports by including an existing import statement in the code section. This approach would result in duplicate import statements, potentially causing confusion and unnecessarily cluttering the code. When adding new imports, it's crucial to consider the existing import statements and use a REPLACE action if necessary to ensure a clean, non-repetitive import section.
To make this example work, you can use REPLACE, or if you stick to INSERT, than just leave out the "import existing_module" line from the code section. 
So using INSERT, here is the correct command:
```yaml
LLMOP:
  version: "1.0"
  action: INSERT
  file: example.py
  language: python
  description: Add new imports incorrectly
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    import existing_module
  code: |-
    import new_module1
    import new_module2
```

### DELETE

- Removes a section of code from a file
- Requires both `start_context` and `end_context`
- Both contexts must uniquely identify the section to be deleted

Example: Before:

```python
def function_to_keep():
    pass

def function_to_delete():
    print("This function will be deleted")

def another_function():
    pass
```

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: DELETE
  file: example.py
  language: python
  description: Delete the function_to_delete
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    def function_to_delete():
  end_context: |-
    print("This function will be deleted")

```

After:

```python
def function_to_keep():
    pass

def another_function():
    pass
```

Explanation: This command deletes the function_to_delete and any content between it and the next function.

### DELETE_FILE

- Deletes a specific file
- Doesn't require `start_context`, `end_context`, or `code` sections

Example: Before: File 'to_delete.py' exists

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: DELETE_FILE
  file: to_delete.py
  description: Delete the specified file
  execution_key: "EXECUTE_LLM_INSTRUCTION"
```

After: File 'to_delete.py' is removed

Explanation: This command deletes the specified file.

### DELETE_FOLDER

- Deletes a folder and all its contents
- Doesn't require `start_context`, `end_context`, or `code` sections

Example: Before: Folder 'old_folder' exists

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: DELETE_FOLDER
  file: old_folder
  description: Delete the specified folder
  execution_key: "EXECUTE_LLM_INSTRUCTION"
```

After: Folder 'old_folder' and all its contents are removed

Explanation: This command deletes the specified folder and all its contents.

## Edge Cases and Special Scenarios

### Inserting at the End of a File

Use REPLACE action with the last unique part of the file as both start and end contexts.

Example: Before:

```python
def existing_function():
    pass

# End of file
```

LLMOP Command:

```yaml
LLMOP:
  version: "1.0"
  action: REPLACE
  file: example.py
  language: python
  description: Add a new function at the end of the file
  execution_key: "EXECUTE_LLM_INSTRUCTION"
  start_context: |-
    # End of file
  end_context: |-
    # End of file
  code: |-
    # End of file

    def new_function():
        print("This is a new function at the end")
```

After:

```python
def existing_function():
    pass

# End of file

def new_function():
    print("This is a new function at the end")
```

Explanation: This command adds a new function at the end of the file by replacing the last line and adding content after it.

### Replacing Entire File Content

Use REPLACE action with the entire file content as both start and end contexts.

### Inserting at the Beginning of a File

Use REPLACE action with the first unique part of the file as both start and end contexts.

### Handling Empty Files

For empty files, use CREATE_FILE action instead of REPLACE or INSERT.

### Dealing with Repetitive Content

Include enough context to uniquely identify the target location, even if it means using longer contexts.

## Choosing the Appropriate Action Type

When selecting an action type for file modifications, consider the following guidelines:

1. Use INSERT for adding new content:
   - Adding imports at the beginning of a file
   - Introducing new functions or classes
   - Appending content to the end of a file

2. Use narrow REPLACE for updating specific sections:
   - Modifying existing functions or methods
   - Updating configuration parameters
   - Changing small portions of code

3. Use full file REPLACE when:
   - Making comprehensive updates to a file
   - Ensuring complete file consistency is crucial
   - Dealing with small files where partial updates might be more complex

4. Prefer targeted operations (INSERT or narrow REPLACE) over full file replacements when possible:
   - Reduces risk of unintended modifications
   - Improves transparency and ease of review
   - Enhances performance for larger files

5. Always use the most precise context possible:
   - For INSERT, choose the exact insertion point
   - For REPLACE, use the shortest unique line region that includes the target section

By following these guidelines, you can achieve more accurate and efficient file modifications while minimizing the risk of errors or unintended changes.


## Context Selection Guidelines

### Handling Decorators

When selecting contexts for LLMOP commands, it's crucial to handle decorators correctly:

- Treat decorators as an integral part of the function definition.
- Never separate decorators from the functions they decorate when selecting contexts.
- Consider a function and its decorators as a single unit for context selection purposes.

#### Good Example:

```yaml
start_context: |-
  @patch('some.module')
  def test_function():
end_context: |-
  assert result == expected_value
```

#### Bad Example:

```yaml
start_context: |-
  @patch('some.module')
end_context: |-
  def test_function():
```

### Context Selection Checklist

When selecting contexts, always:

1. Verify that decorators are not separated from their functions.
2. Ensure that the entire function block, including decorators, is treated as a single unit.
3. Double-check that your start_context includes all relevant decorators if selecting a decorated function.
4. Confirm that your end_context doesn't cut off any part of the function body or its closing statements.

By following these guidelines, you'll maintain the integrity of code structures and avoid errors in LLMOP commands.

## Best Practices

1. Ensure context uniqueness within the file.
2. Use the shortest unique context possible.
3. Include function signatures, unique comments, or distinctive code patterns in contexts.
4. Verify the action type matches the intended operation.
5. Double-check file paths and extensions.
6. Review the code section for correctness and proper indentation.
7. Always include the correct execution_key.

## Common Pitfalls to Avoid

1. Non-unique contexts leading to unintended modifications.
2. Overly broad contexts affecting more code than intended.
3. Using INSERT when REPLACE is needed (e.g., for end-of-file additions).
4. Forgetting to include necessary sections (e.g., code for CREATE_FILE).
5. Incorrect indentation in the YAML structure or code section.

Remember, precise context selection is key to accurate and safe file modifications.

IMPORTANT:
Take this as instructions for file access.  Whenever you need to do file operations, adhere to this Command Guide.
Be sure to put each llmop command in a separate code box.
