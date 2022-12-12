import os
import node

with open(os.path.realpath(os.path.dirname(__file__)) + '/input.txt', 'r') as f:
    input_lines = f.read().splitlines()

n = node.Node(0, "/", 0)


for line in input_lines:

    if line[0] == '$':
        mode = line[2]+line[3]
        if mode == "cd":
            dirtoGo = line[5:]
            if dirtoGo == "..":
                n = n.GetParent()
            else:
                n = n.gotoDir(dirtoGo)
    else :
        splitted = line.split(' ')

        if splitted[0] == 'dir':
            n.AddChild(node.Node(n, splitted[1], 0))
        else:
            n.AddChild(node.Node(n, splitted[1], int(splitted[0])))


n.getRoot().PrintSizeFirst("")
print(n.getRoot().sum)