import os
import sys

args = sys.argv[1:]

showHidden = False
targetDir = '.'

i = 0
while i < len(args):
    if args[i] == '-a':
        showHidden = True
    elif args[i] == '-1':
        # one per line is default so nothing to do
        pass
    else:
        targetDir = args[i]
    i = i + 1

entries = os.listdir(targetDir)

if not showHidden:
    newEntries = []
    for entry in entries:
        if not entry.startswith('.'):
            newEntries.append(entry)
    entries = newEntries

entries.sort()

for entry in entries:
    print(entry)