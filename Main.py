totalNodes = 10;
thresholdDistance = 3;

nodePointers = [];

class Node:
    pos = 0;
    x = 0;
    y = 0;
    info = "";
    neighbours = [];
    data = [];

    def CalculateDistance(self, x1, y1):
        return ((self.x - x1) ^ 2 + (self.y - y1) ^ 2) ^ 0.5


    def UpdateNeighbours(self):
        for i in range(totalNodes):
            n = nodePointers[i]
            if self.CalculateDistance(n.x, n.y) <= thresholdDistance:
                neighbours[i] = n.pos
                data[i] = n.ReturnInfo
                n.UpdateNeighbours()


    def PrintNeighbours(self):
        for i in neighbours:
            if neighbours[i] > 0:
                print(neighbours[i]);


    def UpdatePosition(self, x1, y1):
        x = x1
        y = y1
        self.UpdateNeighbours()

    def UpdateData(self, node, info):
        data[node - 1] = info


    def ReturnInfo(self):
        return info
    
    def GetData(self, node):
        info = ""
        if neighbours[node - 1] > 0:
            return data[node - 1]
        else:
            for n in neighbours:
                if n > 0:
                  info = nodePointers[node - 1].SendData(node)
                  if (info != ""):
                      break
        return info


n = int(input("Enter number of nodes in the network"));
for i in range(n):
    node = Node()
    node.pos = i
    node.neighbours = [0] * n
    nodePointers.append(node)
    node.x = int(input("Enter x co-ordinate for node " + str(i + 1)))
    node.y = int(input("Enter y co-ordinate for node " + str(i + 1)))

for j in range(n):
    nodePointers[j].UpdateNeighbours();
    nodePointers[j].PrintNeighbours();

