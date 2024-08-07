# Context Selection Guidelines

## Handling Decorators

When selecting contexts for LLMOP commands, it's crucial to handle decorators correctly:

- Treat decorators as an integral part of the function definition.
- Never separate decorators from the functions they decorate when selecting contexts.
- Consider a function and its decorators as a single unit for context selection purposes.

### Good Example:

```yaml
start_context: |-
  @patch('some.module')
  def test_function():
end_context: |-
  assert result == expected_value
```

### Bad Example:

```yaml
start_context: |-
  @patch('some.module')
end_context: |-
  def test_function():
```

## Context Selection Checklist

When selecting contexts, always:

1. Verify that decorators are not separated from their functions.
2. Ensure that the entire function block, including decorators, is treated as a single unit.
3. Double-check that your start_context includes all relevant decorators if selecting a decorated function.
4. Confirm that your end_context doesn't cut off any part of the function body or its closing statements.

By following these guidelines, you'll maintain the integrity of code structures and avoid errors in LLMOP commands.