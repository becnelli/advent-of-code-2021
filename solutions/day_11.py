### --- Day 11: --- ###


def buildArray(lines):
    results=[]
    for line in lines:
        results.append([int(x) for x in line.strip()])
    return results

def advance(octoArray):
    for r in range(0, len(octoArray)):
        for c in range(0, len(octoArray[r])):
            octoArray[r][c]+=1

def flashEm(octoArray):
    flashCount = 0
    newFlash=False
    for r in range(0, len(octoArray)):
        for c in range(0, len(octoArray[r])):
            if octoArray[r][c] > 9:
                newFlash=True
                flashCount+=1

                octoArray[r][c] *= -1

                #advance neighbors
                if r > 0 and octoArray[r-1][c] >= 0:
                    octoArray[r-1][c] += 1
                if r < 9 and octoArray[r+1][c] >= 0:
                    octoArray[r+1][c] += 1
                if c > 0 and octoArray[r][c-1] >= 0:
                    octoArray[r][c-1] += 1
                if c < 9 and octoArray[r][c+1] >= 0:
                    octoArray[r][c+1] += 1

                #advance diag
                if r > 0 and c > 0 and octoArray[r-1][c-1] >= 0:
                    octoArray[r-1][c-1] += 1
                if r > 0 and c < 9 and octoArray[r-1][c+1] >= 0:
                    octoArray[r-1][c+1] += 1
                if r < 9 and c > 0 and octoArray[r+1][c-1] >= 0:
                     octoArray[r+1][c-1] += 1
                if r < 9 and c < 9 and octoArray[r+1][c+1] >= 0:
                     octoArray[r+1][c+1] += 1

    if(newFlash):
        flashCount += flashEm(octoArray)

    return flashCount

def reset(octoArray):
    numReset=0
    for r in range(0, len(octoArray)):
        for c in range(0, len(octoArray[r])):
            if octoArray[r][c] < 0:
                octoArray[r][c] = 0
                numReset+=1
    return numReset

def printNice(day, octoArray):
    print()
    print("DAY:", day)
    for r in octoArray:
        row=''
        for c in r:
            row+=str(c)
        print(row)


with open('../input_files/day_11.txt', 'r') as f:
    lines = f.readlines()

octo=buildArray(lines)

stepLen=100
totalFlash=0
for step in range(0, stepLen):
    advance(octo)
    totalFlash+= flashEm(octo)
    reset(octo)
    printNice(step+1, octo)

print("Puzzle 1:", totalFlash)

octo=buildArray(lines)
numReset=0
stepDay=0
while numReset != 100:
    stepDay+=1
    advance(octo)
    totalFlash+= flashEm(octo)
    numReset=reset(octo)
    printNice(stepDay, octo)

print("Puzzle 2:", stepDay)
