import smallnode

class Node:

    def __init__(self, parent, name, size):
        self.childNodes = []
        self.parentNode = parent
        self.size = size
        self.name = name
        self.sum = 0
        self.smallestNode = ""
        

    def GetParent(self):
        return self.parentNode

    def GetSize(self):
        if self.size > 0:
            return self.size

        size = 0
        for n in self.childNodes:
            size += n.GetSize()
        return size

    def AddChild(self, node):
        for c in self.childNodes:
            if c.name == node.name:
                return
        self.childNodes.append(node)
    
    def gotoDir(self, name):
        for c in self.childNodes:
            if c.name == name:
                return c

    def getRoot(self):
        if self.name != '/':
            return self.parentNode.getRoot()
        else:
            return self

    def PrintSizeFirst(self, seperator):
        if self.size == 0:
            ownSize = self.GetSize()
            if ownSize < 100000:
                print("{0}{1} {2}".format(seperator, self.name, ownSize))
                self.getRoot().sum += ownSize
            seperator += "---"
            for c in self.childNodes:
                c.PrintSizeFirst(seperator)


    def GetBestDir(self, smallest):
        if self.size == 0:
            selfSize = self.GetSize()
            if selfSize > 8690120:
                difference = abs(8690120 - selfSize)
                if difference <= smallest:
                    smallest = difference
                    self.getRoot().smallestNode = self
            for c in self.childNodes:
                c.GetBestDir(smallest)

    def getNodes(self):
        nodes = []
        for c in self.childNodes:
            if c.size == 0:
                nodes.append(smallnode.SmallNode(c.name, c.GetSize()))
                nodes += c.getNodes()
        return nodes
            