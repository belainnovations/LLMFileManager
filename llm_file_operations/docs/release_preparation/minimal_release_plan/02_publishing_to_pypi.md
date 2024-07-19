# Publishing LLM File Operations to PyPI

Follow these steps to publish the LLM File Operations package to PyPI:

## Step 1: Publish to TestPyPI

1. Ensure you have the latest versions of setuptools, wheel, and twine installed:
   ```
   pip install --upgrade setuptools wheel twine
   ```

2. Navigate to the root directory of the project (where `setup.py` is located).

3. Build the distribution files:
   ```
   python setup.py sdist bdist_wheel
   ```

4. Upload the package to TestPyPI:
   ```
   twine upload --repository testpypi dist/*
   ```

5. Test the installation from TestPyPI:
   ```
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ llm_file_operations
   ```

6. Test the functionality of the installed package.

## Step 2: Publish to PyPI

After successful testing on TestPyPI:

1. Upload the package to PyPI:
   ```
   twine upload dist/*
   ```

2. Enter your PyPI username and password when prompted.

After these steps, your package should be available on PyPI and can be installed using pip:
```
pip install llm_file_operations
```

Remember to update the version number in `setup.py` each time you publish a new release.
