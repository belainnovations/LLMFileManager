# 3D Bouncing Balls CPU Visualization

This project demonstrates a 3D visualization of bouncing balls, where the size of each ball is proportional to the current CPU usage of the local machine. The project consists of a Flask backend and a Three.js frontend.

## Features

- Real-time 3D visualization of bouncing balls
- Ball size reflects current CPU usage
- Constant ball generation (1 per second)
- Reduced gravity simulation (0.1 times Earth's gravity)

## Prerequisites

- Python 3.7+
- Modern web browser with WebGL support

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd examples/test05
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. You should see the 3D visualization of bouncing balls. New balls will be generated every second, with their size reflecting the current CPU usage.

## Project Structure

- `app.py`: Flask backend serving CPU usage data and the frontend
- `static/main.js`: JavaScript file handling the 3D scene and ball generation
- `templates/index.html`: HTML template for the frontend
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## Technologies Used

- Backend: Flask, psutil
- Frontend: Three.js, Cannon.js
- 3D Graphics: WebGL

## License

This project is open source and available under the [MIT License](LICENSE).