const fs = require('fs');
const args = process.argv.slice(2);

let numberNonBlank = false;
let numberLines = false;
let files = [];

// Separate flags from filenames
for (let arg of args) {
    if (arg === '-n') {
        numberLines = true;
    } else if (arg === '-b') {
        numberNonBlank = true;
    } else {
        files.push(arg);
    }
}

let lineNumber = 1;  // start counting from 1

for (let file of files) {
    const content = fs.readFileSync(file, 'utf8');
    const lines = content.split('\n');

    for (let line of lines) {
        if (numberNonBlank) {
            if (line.trim() !== '') {
                console.log(lineNumber + '\t' + line);
                lineNumber++;
            } else {
                console.log(line);   // blank line, no number
            }
        } else if (numberLines) {
            console.log(lineNumber + '\t' + line);
            lineNumber++;
        } else {
            console.log(line);
        }
    }
}