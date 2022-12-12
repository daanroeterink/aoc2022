import os

with open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r') as f:
    input_lines = f.read().splitlines()

firstLine = input_lines[0]

length = len(firstLine)

counter = 0

for x in range(length-3):
    counter+=1
    firstL = firstLine[x]
    secL = firstLine[x+1]
    thirdL = firstLine[x+2]
    fourthL = firstLine[x+3]
    
    if firstL != secL and firstL != thirdL and firstL != fourthL and secL != thirdL and secL != fourthL and thirdL != fourthL:
        print(counter+3)
        break
