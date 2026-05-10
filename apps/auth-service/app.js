const express = require('express');
const app = express();

app.get('/health', (req, res) => res.json({status: 'UP'}));
app.get('/login', (req, res) => {
    const success = Math.random() > 0.3;
    if (success) {
        console.log(JSON.stringify({level: "info", service: "auth-service", msg: "Login successful", user: "user_" + Math.floor(Math.random()*100)}));
        res.json({status: "success"});
    } else {
        console.log(JSON.stringify({level: "warn", service: "auth-service", msg: "Login failed - invalid credentials"}));
        res.status(401).json({status: "failed"});
    }
});
app.get('/simulate-error', (req, res) => {
    console.log(JSON.stringify({level: "error", service: "auth-service", msg: "Database connection lost!"}));
    res.status(500).json({status: "error"});
});

setInterval(() => {
    console.log(JSON.stringify({level: "info", service: "auth-service", msg: "Routine auth check..."}));
}, 5000);

app.listen(3001, () => console.log('Auth service running on 3001'));
