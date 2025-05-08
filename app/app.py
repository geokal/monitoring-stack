from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world from Flask in Docker!"

@app.route('/load-test', methods=['GET'])
def load_test():
    """
    Simulates a workload by performing a time delay and returning random data.
    """
    # Simulate workload
    time.sleep(2)  # Simulates a delay (e.g., heavy computation or I/O)
    random_numbers = [random.randint(1, 100) for _ in range(10)]  # Generate random data

    return jsonify({
        "message": "Load test completed",
        "data": random_numbers
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
