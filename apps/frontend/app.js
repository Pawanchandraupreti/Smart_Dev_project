const express = require('express');
const path = require('path');
const axios = require('axios');
const app = express();

app.get('/health', (req, res) => res.json({status: 'UP'}));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const services = {
    auth: 'http://auth-service:3001',
    payment: 'http://payment-service:3002',
    order: 'http://order-service:3003',
    notification: 'http://notification-service:3004'
};

app.get('/api/:service/:action', async (req, res) => {
    const { service, action } = req.params;
    const url = `${services[service]}/${action}`;
    try {
        const response = await axios.get(url);
        res.json(response.data);
    } catch (error) {
        if (error.response) {
            res.status(error.response.status).json(error.response.data);
        } else {
            res.status(500).json({ error: 'Service unreachable' });
        }
    }
});

app.listen(3000, () => {
    console.log('[INFO] [frontend] Server started on port 3000');
});
