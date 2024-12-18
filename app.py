from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from faker import Faker
import random
import uuid
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

fake = Faker()

# Simulate 10 robots with random data
robots = []
for _ in range(10):
    robots.append({
        'robot_id': str(uuid.uuid4()),
        'status': random.choice([True, False]),
        'battery': random.randint(10, 100),
        'cpu_usage': random.randint(0, 100),
        'ram_usage': random.randint(0, 100),
        'location': (round(random.uniform(-90, 90), 6), round(random.uniform(-180, 180), 6)),
        'last_update': int(time.time())
    })

def update_robots_data():
    """ Periodically update robots data every 5 seconds. """
    while True:
        for robot in robots:
            robot['battery'] = random.randint(10, 100)
            robot['cpu_usage'] = random.randint(0, 100)
            robot['ram_usage'] = random.randint(0, 100)
            robot['location'] = (round(random.uniform(-90, 90), 6), round(random.uniform(-180, 180), 6))
            robot['status'] = random.choice([True, False])
            robot['last_update'] = int(time.time())
        socketio.emit('robot_data', {'robots': robots})
        time.sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/robots')
def get_robots():
    return jsonify({'robots': robots})

# WebSocket endpoint to push real-time updates
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('robot_data', {'robots': robots})

# Start a thread to update robots data every 5 seconds
thread = threading.Thread(target=update_robots_data)
thread.daemon = True
thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
