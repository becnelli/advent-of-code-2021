### --- Day 4: --- ###

from helpers import *

with open('../input_files/day_04.txt', 'r') as f:
#with open('../input_files/day_04.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

drawn=lines[0].split(",")
lines.pop(0)

numBoards = int(len(lines) / 6)

# boards = an array of boards containing 2d arrays with row/col
boards=[]

for i in range(0, numBoards):
    newBoard=[]
    for r in range(1, 6):
        rowIndex=(i*6)+r
        newRow=[]
        values=lines[rowIndex].split()
        for c in range(0, 5):
            val=values[c]
            newRow.append(val)
        newBoard.append(newRow)
    boards.append(newBoard)

def populateNumber(n):
    for b1 in range(0,len(boards)):
        for r1 in range(0,5):
            for c1 in range(0,5):
                if boards[b1][r1][c1] == n:
                    boards[b1][r1][c1] = '-'

def printFancy():
    for f in range(0,len(boards)):
        print(f'{f}: {boards[f]}')

def sumUnmarked(b3):
    res=0
    for r3 in range(0, 5):
        for c3 in range(0, 5):
            if boards[b3][r3][c3] != '-':
                res += int(boards[b3][r3][c3])
    return res

def getWinningBoards():
    boardsToDrop=[]
    for b2 in range(0,len(boards)):
        foundWin=False
        for r2 in range(0, 5):
            totalFoundInRow = sum(1 for c2 in range(0, 5) if boards[b2][r2][c2] == '-')
            if totalFoundInRow == 5:
                foundWin=True
        for c2 in range(0, 5):
            totalFoundInCol = sum(1 for r2 in range(0, 5) if boards[b2][r2][c2] == '-')
            if totalFoundInCol == 5:
                foundWin=True
        if foundWin:
            boardsToDrop.append(b2)
    return boardsToDrop

foundFirstWin=False

for n in drawn:
    populateNumber(n)

    drops=getWinningBoards()

    if (not(foundFirstWin)) and len(drops) > 0:
        foundFirstWin=True
        total=sumUnmarked(drops[0])
        print("Puzzle 1:", total*int(n))
    
    if len(drops) == 1 and len(boards) == 1:
        total=sumUnmarked(0)
        print("Puzzle 2:", total*int(n))
        break

    for d in range(len(drops), 0, -1):
        boards.pop(drops[d-1])

### Answers ###
# Puzzle 1: 35711
# Puzzle 2: 5586 
