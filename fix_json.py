import json
import os

files = ['dashboards/system-overview.json', 'dashboards/service-insights.json']

for filename in files:
    with open(filename, 'r') as f:
        data = json.load(f)
    
    for panel in data.get('panels', []):
        for target in panel.get('targets', []):
            expr = target.get('expr', '')
            if expr:
                expr = expr.replace('container="/auth-service"', 'container="auth-service"')
                expr = expr.replace('container="/payment-service"', 'container="payment-service"')
                expr = expr.replace('container=~"/.*-service"', 'container=~"^.*-service$"')
                target['expr'] = expr
                
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

