from flask import Flask, jsonify
import logging
import random
import sys
import time
import threading

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - payment-service - %(levelname)s - %(message)s', stream=sys.stdout)
logger = logging.getLogger()

@app.route('/health')
def health():
    return jsonify({"status": "UP"})

@app.route('/pay')
def pay():
    if random.random() > 0.2:
        logger.info("Payment processed successfully for amount $%d", random.randint(10, 500))
        return jsonify({"status": "success"})
    else:
        logger.warning("Payment declined due to insufficient funds")
        return jsonify({"status": "failed"}), 400

@app.route('/simulate-error')
def simulate_error():
    logger.error("Payment Gateway Timeout Exception: Unable to reach external gateway")
    return jsonify({"status": "error"}), 500

def background_traffic():
    while True:
        logger.info("Heartbeat: Payment service is active")
        time.sleep(7)

threading.Thread(target=background_traffic, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)
