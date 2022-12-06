import os

input = open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r')
input_lines = input.readlines()

searchIndex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def getSharedChar(firstLine, secondLine, ThirdLine):
    for c in firstLine:
        if c in secondLine and c in ThirdLine:
            return c


for x in range(len(input_lines)):
    input_lines[x] = input_lines[x].replace('\n','')

    
totalScore = 0

for x in range(0, len(input_lines)-2, 3):
    line = input_lines[x]
    secline = input_lines[x+1]
    thirdline = input_lines[x+2]

    chosen = getSharedChar(line, secline, thirdline)

    score = searchIndex.index(chosen)+1
 
    totalScore += score

print(totalScore)



