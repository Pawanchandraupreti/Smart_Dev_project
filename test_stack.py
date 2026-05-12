import urllib.request
import time
import json

urls_to_test = [
    'http://localhost:5500/api/status',
    'http://localhost:3001/health',
    'http://localhost:3001/simulate-error',
    'http://localhost:3001/simulate-error',
    'http://localhost:3001/simulate-error',
    'http://localhost:3001/simulate-error',
    'http://localhost:3001/simulate-error',
    'http://localhost:3002/simulate-error',
    'http://localhost:3003/simulate-error',
    'http://localhost:3004/simulate-error'
]

print("--- Testing API Endpoints ---")
for url in urls_to_test:
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            print(f'SUCCESS: {url} -> {data}')
    except urllib.error.HTTPError as e:
        data = e.read().decode('utf-8')
        print(f'HTTP ERROR {e.code}: {url} -> {data}')
    except Exception as e:
        print(f'FAILED: {url} -> {e}')
    time.sleep(0.5)

print("\\n--- Waiting for Alertmanager to process rules... ---")
time.sleep(5)

print("\\n--- Querying Alertmanager Status ---")
try:
    req = urllib.request.Request('http://localhost:9093/api/v2/alerts')
    with urllib.request.urlopen(req) as response:
        alerts = json.loads(response.read().decode('utf-8'))
        print(f"Total Active Alerts: {len(alerts)}")
        for alert in alerts:
            print(f"- ALERT: {alert['labels'].get('alertname')} -> {alert['annotations'].get('summary')}")
except Exception as e:
    print(f"Failed to reach Alertmanager: {e}")
