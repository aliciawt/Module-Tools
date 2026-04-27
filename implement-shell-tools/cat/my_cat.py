import sys

args = sys.argv[1:]

numberNonBlank = False
numberLines = False
files = []

for arg in args:
    if arg == '-n':
        numberLines = True
    elif arg == '-b':
        numberNonBlank = True
    else:
        files.append(arg)

lineNumber = 1

for file in files:
    f = open(file, 'r')
    content = f.read()
    f.close()
    
    lines = content.split('\n')
    
    for line in lines:
        if numberNonBlank:
            if line != '':
                print(str(lineNumber) + '\t' + line)
                lineNumber = lineNumber + 1
            else:
                print(line)
        elif numberLines:
            print(str(lineNumber) + '\t' + line)
            lineNumber = lineNumber + 1
        else:
            print(line)