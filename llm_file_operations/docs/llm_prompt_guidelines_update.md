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