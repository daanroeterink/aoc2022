import os

with open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r') as f:
    input_lines = f.read().splitlines()

firstLine = input_lines[0]

length = len(firstLine)

counter = 0

for x in range(length-14):

    words = {}
    for s in range(x,x+14):
        if firstLine[s] not in words:
            words[firstLine[s]] = True
            counter +=1 
        elif firstLine[s] in words:
            break
    
    length = len(words)
    if length >= 14:
        print(x+14)
        break