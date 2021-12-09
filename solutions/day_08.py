### --- Day 8: --- ###

with open('../input_files/day_08.txt', 'r') as f:
    lines = f.readlines()

def solution1(lines):
    total=0
    for line in lines:
        part2 = line.split('|')[1].split()
        for num in part2:
            if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
                total+=1

    print("Puzzle 1:", total)

solution1(lines)


# ---- Part 2 ---------

def reverseReverse(data):
    return dict((''.join(sorted(set(v))),k) for k,v in data.items())

def groupBySize(data):
    results = {}
    
    for d in data:
        if not len(d) in results:
            results[len(d)] = []

        results[len(d)].append(d)

    return results


def decodeNums(data):
    bySize = groupBySize(data)
    results = {}

    # we automatically know 1, 4, 7, 8 by size
    results[1]=bySize[2][0]
    bySize.pop(2)

    results[4]=bySize[4][0]
    bySize.pop(4)

    results[7]=bySize[3][0]
    bySize.pop(3)

    results[8]=bySize[7][0]
    bySize.pop(7)

    # solve for 0, 2, 3, 5, 6, 9

    # 0, 6, 9 all have 6 digits
    ## 6 is the only one without both 1 numbers in it
    for n in bySize[6]:
        containsAll=True
        for one in results[1]:
            if not one in n:
                containsAll=False
        if not containsAll:
            results[6]=n
            bySize[6].remove(n)
            break

    for l in results[1]:
        if not l in results[6]:
            letterInPosC=l

    ## 9 must contain 4
    for n in bySize[6]:
        containsAll=True
        for letter in results[4]:
            if not letter in n:
                containsAll=False
        if containsAll:
            results[9]=n
            bySize[6].remove(n)
            break

    for l in results[1]:
        if not l in results[9]:
            letterInPosC=l

    ## 0 is the last at size 6
    results[0]=bySize[6][0]
    bySize.pop(6)
    
    # 2, 3, 5 all have 5 digits
    ## 5 is the only one without letter in pos c
    for n in bySize[5]:
        if not letterInPosC in n:
            results[5]=n
            bySize[5].remove(n)
            break

    ## 3 contains all of one
    for n in bySize[5]:
        containsAll=True
        for one in results[1]:
            if not one in n:
                containsAll=False
        if containsAll:
            results[3]=n
            bySize[5].remove(n)
            break

    ## 2 remains
    results[2]=bySize[5][0]
    bySize.pop(5)


    return reverseReverse(results)

def solution2(lines):
    result = 0
    for line in lines:
        parts=line.split('|')
        numMap=decodeNums(parts[0].split())
        
        num=""
        for val in parts[1].split():
            val=''.join(sorted(set(val)))
            digit=str(numMap[val])
            num+=str(numMap[val])

        result+=int(num)

    print("Puzzle 2:", result)


solution2(lines)
