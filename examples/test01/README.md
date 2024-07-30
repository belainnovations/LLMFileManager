# Shape Inheritance Example

This project demonstrates object-oriented programming concepts, particularly inheritance, using geometric shapes as an example.

## Project Structure

- `shape.py`: Contains the base `Shape` class.
- `circle.py`: Defines the `Circle` class, inheriting from `Shape`.
- `rectangle.py`: Defines the `Rectangle` class, inheriting from `Shape`.
- `shape_example.py`: Demonstrates the usage of the shape classes.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/shape-inheritance-example.git
   cd shape-inheritance-example
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the example script:

```
python shape_example.py
```

## Running Tests

To run the unit tests:

```
python -m unittest discover tests
```

## Documentation

To build the documentation:

1. Navigate to the `docs` directory:
   ```
   cd docs
   ```

2. Build the HTML documentation:
   ```
   make html
   ```

3. Open `docs/_build/html/index.html` in your web browser to view the documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.