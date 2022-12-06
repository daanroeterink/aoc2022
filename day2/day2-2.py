import os

input = open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r')
input_lines = input.readlines()



# A X = Rock
# B Y= Paper
# C Z= Scissor

totalScore = 0

for line in input_lines:
    line = line.replace('\n', '')
    splitted_line = line.split(' ')
    opponent = splitted_line[0]
    end = splitted_line[1]

    score = 0
    Yours = ''

    if end == 'X':
        if opponent == 'A':
            yours = 'Z'
        if opponent == 'B':
            yours = 'X'
        if opponent == 'C':
            yours = 'Y'
    if end == 'Y':
        if opponent == 'A':
            yours = 'X'
        if opponent == 'B':
            yours = 'Y'
        if opponent == 'C':
            yours = 'Z'
    if end == 'Z':
        if opponent == 'A':
            yours = 'Y'
        if opponent == 'B':
            yours = 'Z'
        if opponent == 'C':
            yours = 'X'


    if (opponent == 'A' and yours == 'Y') or (opponent == 'B' and yours == 'Z') or (opponent == 'C' and yours== 'X'):
        score += 6

    if (opponent == 'A' and yours == 'X') or (opponent == 'B' and yours == 'Y') or (opponent == 'C' and yours== 'Z'):
        score += 3

    if yours == 'X':
        score += 1
    if yours == 'Y':
        score += 2
    if yours == 'Z':
        score += 3

    totalScore += score

print(totalScore)


