import sys

args = sys.argv[1:]

flagL = False
flagW = False
flagC = False
files = []

for arg in args:
    if arg == '-l':
        flagL = True
    elif arg == '-w':
        flagW = True
    elif arg == '-c':
        flagC = True
    else:
        files.append(arg)

# default to all flags if none specified
if not flagL and not flagW and not flagC:
    flagL = True
    flagW = True
    flagC = True

def wordCount(str):
    parts = str.split(' ')
    count = 0
    for i in range(len(parts)):
        if parts[i] != '':
            count = count + 1
    return count

totalLines = 0
totalWords = 0
totalBytes = 0

for file in files:
    f = open(file, 'r')
    content = f.read()
    f.close()
    
    f2 = open(file, 'rb')
    rawBytes = len(f2.read())
    f2.close()
    
    linesArray = content.split('\n')
    lineCount = len(linesArray)
    
    # count words by checking each character
    wordCountManual = 0
    inWord = False
    for ch in content:
        if ch == ' ' or ch == '\n' or ch == '\t':
            inWord = False
        else:
            if not inWord:
                wordCountManual = wordCountManual + 1
                inWord = True
    
    totalLines = totalLines + lineCount
    totalWords = totalWords + wordCountManual
    totalBytes = totalBytes + rawBytes
    
    outputParts = []
    if flagL:
        outputParts.append(str(lineCount))
    if flagW:
        outputParts.append(str(wordCountManual))
    if flagC:
        outputParts.append(str(rawBytes))
    outputParts.append(file)
    print(' '.join(outputParts))

# show total line if multiple files
if len(files) > 1:
    totalParts = []
    if flagL:
        totalParts.append(str(totalLines))
    if flagW:
        totalParts.append(str(totalWords))
    if flagC:
        totalParts.append(str(totalBytes))
    totalParts.append('total')
    print(' '.join(totalParts))