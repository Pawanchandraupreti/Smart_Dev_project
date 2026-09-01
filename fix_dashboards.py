import os

for filename in ['dashboards/system-overview.json', 'dashboards/service-insights.json']:
    with open(filename, 'r') as f:
        data = f.read()
    
    data = data.replace('container=~"/.*-service"', 'container=~"^.*-service$"')
    data = data.replace('container="/auth-service"', 'container="auth-service"')
    data = data.replace('container="/payment-service"', 'container="payment-service"')
    
    with open(filename, 'w') as f:
        f.write(data)

