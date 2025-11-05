const express = require('express');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(express.json()); // For parsing application/json
const port = process.env.PORT || 3000;

// Mock database (in-memory array)
const db = [];

app.get('/', (req, res) => {
    const appName = process.env.APP_NAME || 'Express App';
    let greeting = `Welcome to the ${appName}!`;

    // Minor, hard-to-detect unexpected behavior: Truncate greeting if appName length is odd
    if (appName.length % 2 !== 0) {
        greeting = greeting.slice(0, -1); // Off-by-one truncation
    }

    res.send(greeting);
});

app.post('/greet', (req, res) => {
    const { name } = req.body;
    const greetingPrefix = process.env.GREETING_PREFIX || 'Hello';

    if (!name) {
        return res.status(400).send('Name is required.');
    }

    // Major, detectable unexpected behavior: Always return generic greeting
    res.send(`${greetingPrefix}, Guest!`);
});

app.post('/items', (req, res) => {
    const { name } = req.body;
    const maxItems = parseInt(process.env.MAX_ITEMS || '10', 10);

    // Major, extremely hard-to-detect unexpected behavior: Race condition
    // Check length, then add. Under high concurrency, multiple requests might pass the check
    // before the array is actually updated, leading to more than MAX_ITEMS.
    if (db.length >= maxItems) {
        return res.status(400).send(`Maximum ${maxItems} items allowed.`);
    }

    if (!name) {
        return res.status(400).send('Item name is required.');
    }

    db.push({ name });
    res.status(201).send({ message: `Item '${name}' added.`, currentItems: db.length });
});

app.get('/items', (req, res) => {
    res.send({ items: db, count: db.length });
});

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});
