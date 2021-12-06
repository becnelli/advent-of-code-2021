### --- Day 4: --- ###

from helpers import *

with open('../input_files/day_05.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

ventSpots_p1 = {}
ventSpots_p2 = {}

def addCordToVentDict(theDict, xPos, yPos):
    if (not(xPos in theDict)):
        theDict[xPos] = {}
    
    if (not(yPos in theDict[xPos])):
        theDict[xPos][yPos] = 0
        
    theDict[xPos][yPos] += 1    


def addCordsToVentDict(x1, y1, x2, y2):
    if x1 == x2:
        minY = y1 if y1 < y2 else y2
        maxY = y2 if y2 > y1 else y1    
        for y in range(minY, maxY + 1):
            addCordToVentDict(ventSpots_p1,x1, y)
            addCordToVentDict(ventSpots_p2,x1, y)
    elif y1 == y2:
        minX = x1 if x1 < x2 else x2
        maxX = x2 if x2 > x1 else x1
        for x in range(minX, maxX + 1):
            addCordToVentDict(ventSpots_p1,x, y1)
            addCordToVentDict(ventSpots_p2,x, y1)
    else:
        diff = abs(x1 - x2)
        xStep = 1 if x1 < x2 else -1
        yStep = 1 if y1 < y2 else -1
                
        for inc in range(0, diff+1):
            addCordToVentDict(ventSpots_p2,x1+(inc*xStep), y1 + (inc*yStep))
    
# print a map of the vents - helper function when testing with sample data
def printVentSpots():
    for y in range(0, 10):
        row=''
        for x in range(0, 10):
            if x in theDict and y in theDict[x]:
                row += str(theDict[x][y])
            else:
                row += '.'
        print(row)

for line in lines:
    cords = line.split(" -> ")
    
    start=[int(x) for x in cords[0].split(",")]
    end=[int(x) for x in cords[1].split(",")]
        
    addCordsToVentDict(start[0], start[1], end[0], end[1])

print('Puzzle 1:', sum(1 for xKey in ventSpots_p1 for yKey in ventSpots_p1[xKey] if ventSpots_p1[xKey][yKey] > 1))
print('Puzzle 2:', sum(1 for xKey in ventSpots_p2 for yKey in ventSpots_p2[xKey] if ventSpots_p2[xKey][yKey] > 1))
    

### Answers ###
# Puzzle 1: 35711
# Puzzle 2: 5586 
