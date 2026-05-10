from flask import Flask, jsonify
import logging
import sys
import time
import threading

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: notification-service: %(message)s', stream=sys.stdout)
logger = logging.getLogger()

@app.route('/health')
def health():
    return jsonify({"status": "UP"})

@app.route('/send')
def send():
    logger.info("Email sent successfully")
    return jsonify({"status": "success"})

@app.route('/simulate-error')
def simulate_error():
    logger.error("SMTP Connection Refused: Could not deliver email")
    return jsonify({"status": "error"}), 500

def background_traffic():
    while True:
        logger.info("Checking notification queue...")
        time.sleep(8)

threading.Thread(target=background_traffic, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3004)
