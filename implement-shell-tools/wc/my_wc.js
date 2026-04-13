const fs = require('fs');

const args = process.argv.slice(2);

let flagL = false;
let flagW = false;
let flagC = false;
let files = [];

for (let i = 0; i < args.length; i++) {
    if (args[i] === '-l') {
        flagL = true;
    } else if (args[i] === '-w') {
        flagW = true;
    } else if (args[i] === '-c') {
        flagC = true;
    } else {
        files.push(args[i]);
    }
}

// default: all flags on if none given
if (!flagL && !flagW && !flagC) {
    flagL = true;
    flagW = true;
    flagC = true;
}

// function to count words
function wordCount(str) {
    let parts = str.split(' ');
    let count = 0;
    for (let i = 0; i < parts.length; i++) {
        if (parts[i] !== '') {
            count++;
        }
    }
    return count;
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

files.forEach(file => {
    const content = fs.readFileSync(file, 'utf8');
    const rawBytes = fs.readFileSync(file).length;
    
    // count lines: split by newline
    const linesArray = content.split('\n');
    const lineCount = linesArray.length;
    
    // count words: need to split by spaces AND newlines
    let wordCountManual = 0;
    let inWord = false;
    for (let i = 0; i < content.length; i++) {
        let ch = content[i];
        if (ch === ' ' || ch === '\n' || ch === '\t') {
            inWord = false;
        } else {
            if (!inWord) {
                wordCountManual++;
                inWord = true;
            }
        }
    }
    
    totalLines += lineCount;
    totalWords += wordCountManual;
    totalBytes += rawBytes;
    
    let outputParts = [];
    if (flagL) outputParts.push(lineCount);
    if (flagW) outputParts.push(wordCountManual);
    if (flagC) outputParts.push(rawBytes);
    outputParts.push(file);
    console.log(outputParts.join(' '));
});

if (files.length > 1) {
    let totalParts = [];
    if (flagL) totalParts.push(totalLines);
    if (flagW) totalParts.push(totalWords);
    if (flagC) totalParts.push(totalBytes);
    totalParts.push('total');
    console.log(totalParts.join(' '));
}