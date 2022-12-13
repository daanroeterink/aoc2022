import os

with open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r') as f:
    input_lines = f.read().splitlines()

height = len(input_lines)
width = len(input_lines[0])


leftHighest = []
rightHighest = []
TopHighest = []
BottomHighest = []

visible = []

for x in range(width):
    TopHighest.append(int(input_lines[0][x]))
    BottomHighest.append(int(input_lines[height-1][x]))
    leftHighest.append(int(input_lines[x][0]))
    rightHighest.append(int(input_lines[x][width-1]))
    

for y in range(height):
    visible.append([])
    for x in range(width):
        if x == 0 or y == 0 or x == width-1 or y == height - 1:
            visible[y].append(True)
        else:
            visible[y].append(False)
        #visible[y].append(int(input_lines[y][x]))

counter = (width*2)+(height*2)-4

for y in range(height):
    for x in range(width):
        treeHeigth = int(input_lines[x][y])
        currentTopHeight = TopHighest[x]
        currentLeftHeight = leftHighest[y]

        if treeHeigth > currentLeftHeight and not visible[x][y]:
            counter +=1
            leftHighest[x] = treeHeigth
            visible[x][y] = True

        if treeHeigth > currentTopHeight and not visible[x][y]:
            counter += 1
            TopHighest[y] = treeHeigth
            visible[x][y] = True

        

for y in range(height-2,0,-1):
    for x in range(width-2,0,-1):
        treeHeigth = int(input_lines[x][y])
        currentBottomHeight = BottomHighest[x]
        currentRightHeight = rightHighest[y]

        if treeHeigth > currentRightHeight and not visible[x][y]:
            counter +=1
            rightHighest[x] = treeHeigth
            visible[x][y] = True

        if treeHeigth > currentBottomHeight and not visible[x][y]:
            counter += 1
            BottomHighest[y] = treeHeigth
            visible[x][y] = True
        

for y in range(height):
    grid = ""
    for x in range(width):
        if visible[x][y]:
            grid += "."
        else:
            grid += ","
        #grid += "{0}".format(visible[x][y])
    print(grid)


        
print(counter)
