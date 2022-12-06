input = open('input.txt', 'r')
input_lines = input.readlines()

elves = {}
counter = 1
calories = 0
max_calories = 0

for line in input_lines:
    if line != '' and line != '\n':
        calories += int(line)
    else:
        elves[counter] = calories
        if max_calories < calories:
            max_calories = calories
        calories = 0
        counter+=1

print(max_calories)
 
orderedElves = list(dict(sorted(elves.items(), key = lambda item: item[1], reverse=True)).items())[:3]

print(orderedElves)

top3 = 0
for oelf in orderedElves:
    top3 += oelf[1]

print(top3)
