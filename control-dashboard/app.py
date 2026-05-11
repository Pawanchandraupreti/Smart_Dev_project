# pyrefly: ignore [missing-import]
from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({"status": "success", "message": "Dashboard is running"})

@app.route('/api/start')
def start_stack():
    try:
        subprocess.Popen(['docker-compose', 'up', '-d'], cwd='..')
        return jsonify({"status": "started"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/stop')
def stop_stack():
    try:
        subprocess.Popen(['docker-compose', 'down'], cwd='..')
        return jsonify({"status": "stopped"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
