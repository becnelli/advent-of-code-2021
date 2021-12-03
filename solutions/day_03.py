### --- Day 3: Binary Diagnostic --- ###

from helpers import *

with open('../input_files/day_03.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

######### PUZZLE 1 ###############
# initialize an array with 0 for the length of a single entry
bits=[0]*(len(lines[0]))

# add one to position if bit is '1' and subtract one if it is '0'
for line in lines:
    for pos in range(0,len(line)):
        b=int(line[pos])
        bits[pos] += (1 if b == 1 else -1)

gamma=''
epsilon=''

# construct string values for gamma and epsilon using bits 
for pos in range(0, len(bits)):
    gamma += ("0" if bits[pos] < 0 else "1")
    epsilon += ("1" if bits[pos] < 0 else "0")

gammaDec = convertBinaryToDecimal(gamma)
epsilonDec = convertBinaryToDecimal(epsilon)

print("Puzzle 1:", gammaDec * epsilonDec)

######### PUZZLE 2 ###############
oxRating = reduceListByBitFrequency(theList=lines, bitPos=0, useMostCommonBit=True)
co2Rating = reduceListByBitFrequency(theList=lines, bitPos=0, useMostCommonBit=False)

co2Dec = convertBinaryToDecimal(co2Rating[0])
oxDec = convertBinaryToDecimal(oxRating[0])

print("Puzzle 2:", co2Dec*oxDec)

### Answers ###
# Puzzle 1: 2743844
# Puzzle 2: 6677951
