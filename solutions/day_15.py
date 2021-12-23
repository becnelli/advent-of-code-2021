import sys
from Node import node

with open('./../input_files/day_15.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines() ]

queueNodes=[]
gridNodes=[]    

growSize=5
origHeight=len(lines)
origLength=len(lines[0])

for y in range(0, len(lines)*growSize):
    gridNodes.append([])

    for x in range(0, len(lines[y % origHeight])*growSize):

        cost = int(lines[y % origHeight][x % origLength])

        # adjust cost
        if y >= origHeight:
            cost = cost + int(y/origHeight)
        if x >= origLength:
            cost = cost + int(x/origLength)

        if cost > 9:
            cost -= 9

        n=node(cost, f'{cost}')

        gridNodes[y].append(n)
        
        if x > 0:
            gridNodes[y][x-1].addNeighbor(n, True)
        
        if y > 0:
            gridNodes[y-1][x].addNeighbor(n, True)
    
startNode=gridNodes[0][0]
startNode.setStart()

endNode = gridNodes[len(gridNodes) - 1][len(gridNodes[0])-1]
endNode.setEnd()

queueNodes.append(startNode)

def visitNode(node):
    node.setVisited(True)
    neighbors=node.getOrderedNeighborsByValue()
    
    for neighbor in neighbors:
        costToEnter = node.getReturnCost() + neighbor.getValue()
        neighbor.reviewReturnCost(node, costToEnter)
        
        # add to queueNodes
        if not neighbor.isVisited() and not neighbor in queueNodes:
            queueNodes.append(neighbor)

    queueNodes.sort(key=lambda x: x.getReturnCost())

    return
    
while not len(queueNodes) == 0:
    nextNode = queueNodes.pop(0)
    if not nextNode.isVisited():
        visitNode(nextNode)

print(endNode.getReturnCost())
endNode.printReturnChain()