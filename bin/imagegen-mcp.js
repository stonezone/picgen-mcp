#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

// Get the path to the Python server
const serverPath = path.join(__dirname, '..', 'src', 'imagegen_mcp', 'server.py');

// Spawn the Python process
const python = spawn('python', [serverPath], {
  stdio: 'inherit',
  env: process.env
});

// Handle process exit
python.on('close', (code) => {
  process.exit(code);
});

// Handle errors
python.on('error', (err) => {
  console.error('Failed to start Python server:', err);
  console.error('\nMake sure Python 3.10+ is installed and in your PATH.');
  console.error('Install Python dependencies: pip install -e .');
  process.exit(1);
});
