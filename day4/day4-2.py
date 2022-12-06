import os

with open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r') as f:
    input_lines = f.read().splitlines()

count = 0

for line in input_lines:
    splittedLine = line.split(',')
    firstElf = splittedLine[0]
    secondElf = splittedLine[1]

    firstElfMin = int(firstElf.split('-')[0])
    firstElfMax = int(firstElf.split('-')[1])

    secondElfMin =int(secondElf.split('-')[0])
    secondElfMax =int(secondElf.split('-')[1])

    if (firstElfMin >= secondElfMin and firstElfMax <= secondElfMax) or (secondElfMin >= firstElfMin and secondElfMax <= firstElfMax):
        count += 1
        continue

    if (firstElfMin <= secondElfMin and firstElfMax <= secondElfMax and firstElfMax >= secondElfMin) or (secondElfMin <= firstElfMin and secondElfMax <= firstElfMax and secondElfMax >= firstElfMin):
        count += 1

print(count)