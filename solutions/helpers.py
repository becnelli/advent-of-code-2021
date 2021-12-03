# Module: helpers.py

# split an array of binary strings into two arrays based on the value in bitPos.  The first array will be items with '0' in the position and the second is items with '1'.
def splitListByBit(theList, bitPos):
    resultList=[[],[]]
    for item in theList:
        if int(item[bitPos]) == 0:
            resultList[0].append(item)
        else:
            resultList[1].append(item)
    return resultList

# convert binary string to decimal number
def convertBinaryToDecimal(binaryNum):
    result = 0
    for pos in range(0, len(binaryNum)):
        power = len(binaryNum)-pos-1
        if binaryNum[pos] == "1":
            result = result + (2 ** power)
    return result

# reduce list of binary numbers based on the frequency of ones or zeros in each position of the list
def reduceListByBitFrequency(theList, bitPos, useMostCommonBit):
    if len(theList) <= 1 or len(theList[0]) < bitPos:
        return theList

    splitList = splitListByBit(theList, bitPos)
    moreZerosThanOnes = len(splitList[0]) > len(splitList[1])
    splitPos = 0 if useMostCommonBit ^ (not(moreZerosThanOnes)) else 1

    return reduceListByBitFrequency(splitList[splitPos], bitPos + 1, useMostCommonBit)
