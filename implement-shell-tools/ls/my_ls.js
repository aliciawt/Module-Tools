const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);

let showHidden = false;
let targetDir = '.';

// Parse arguments
for (let i = 0; i < args.length; i++) {
    if (args[i] === '-a') {
        showHidden = true;
    } else if (args[i] === '-1') {
        // -1 just means one per line, which we always do – nothing to store
    } else {
        // Assume it's the directory path
        targetDir = args[i];
    }
}

// Read directory contents
let entries = fs.readdirSync(targetDir);

// Filter hidden files unless -a is used
if (!showHidden) {
    entries = entries.filter(entry => !entry.startsWith('.'));
}

// Sort alphabetically
entries.sort();

// Print one per line
entries.forEach(entry => console.log(entry));