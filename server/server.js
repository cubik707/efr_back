const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const app = express();
const port = 5000;

app.use(cors());
app.use(bodyParser.json());

app.post('/calculate', (req, res) => {
     const jsonFilePath = 'D:/univer/efr-py/back/server/output.json';

    console.log('Attempting to read JSON file from:', jsonFilePath); // Вывод пути

    fs.readFile(jsonFilePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            return res.status(500).send('Error reading JSON file');
        }

        try {
            const jsonData = JSON.parse(data); // Parse JSON data
            res.json(jsonData); // Send parsed data as response
        } catch (parseError) {
            console.error('Error parsing JSON data:', parseError);
            res.status(500).send('Error parsing JSON data');
        }
    });
});

app.post('/save', (req, res) => {
    const jsonFilePath = 'D:/univer/efr-py/back/server/input.json';
    const dataToSave = req.body;

    console.log('Saving data to:', jsonFilePath);

    fs.writeFile(jsonFilePath, JSON.stringify(dataToSave, null, 2), 'utf8', (err) => {
        if (err) {
            console.error('Error writing to JSON file:', err);
            return res.status(500).send('Error writing to JSON file');
        }

        console.log('Data saved successfully');

        // Выполняем скрипт script.py
        exec('python script.py', (err, stdout, stderr) => {
            if (err) {
                console.error('Error executing script:', err);
                return res.status(500).send('Error executing script');
            }

            if (stderr) {
                console.error('Script stderr:', stderr);
                return res.status(500).send('Script error');
            }

            console.log('Script output:', stdout);
            res.status(200).send('Data saved and script executed successfully');
        });
    });
});


app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
