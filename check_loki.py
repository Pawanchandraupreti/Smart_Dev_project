import urllib.request
import urllib.parse
import json

query = urllib.parse.quote('{container="auth-service"}')
url = f'http://localhost:3100/loki/api/v1/query?query={query}'

try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        results = data.get('data', {}).get('result', [])
        if not results:
            print("No data found for auth-service.")
        else:
            print(f"Found {len(results)} label streams.")
            for stream in results:
                print(f"Labels: {stream['stream']}")
                print(f"Lines: {len(stream['values'])}")
                if len(stream['values']) > 0:
                    print(f"Sample line: {stream['values'][0][1]}")
except Exception as e:
    print('Error querying Loki for auth-service:', e)
