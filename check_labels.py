import urllib.request
import urllib.parse
import json

url = 'http://localhost:3100/loki/api/v1/label/container/values'

try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        print("Available container labels in Loki:", data.get('data', []))
except Exception as e:
    print('Error:', e)
