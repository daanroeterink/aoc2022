import os

input = open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r')
input_lines = input.readlines()

searchIndex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def getSharedChar(firstPart, secondPart):
    for c in firstPart:
        if c in secondPart:
            return c

totalScore = 0

for line in input_lines:
    line = line.replace('\n', '')
    halve = int(len(line)/2)
    firstPart = line[0:halve]
    lastPart = line[halve:]
    chosen = getSharedChar(firstPart, lastPart)
    print(chosen)

    score = searchIndex.index(chosen)+1
 
    totalScore += score

print(totalScore)



