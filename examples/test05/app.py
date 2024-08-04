from flask import Flask, render_template, jsonify
import psutil
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cpu_usage')
def cpu_usage():
    return jsonify({'cpu_usage': psutil.cpu_percent()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
