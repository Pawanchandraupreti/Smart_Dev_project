const express = require('express');
const app = express();

app.get('/health', (req, res) => res.json({status: 'UP'}));
app.get('/order', (req, res) => {
    console.log(`[INFO] [order-service] Order placed successfully.`);
    res.json({status: "success"});
});
app.get('/simulate-error', (req, res) => {
    console.error(`[ERROR] [order-service] Inventory sync failed!`);
    res.status(500).json({status: "error"});
});

setInterval(() => {
    console.log(`[INFO] [order-service] Listening for new orders...`);
}, 6000);

app.listen(3003, () => console.log('Order service running on 3003'));
