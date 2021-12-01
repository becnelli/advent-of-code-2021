### --- Day 1: Sonar Sweep --- ###
# Puzzle 1: Compare the current depth with the previous depth.  
#           If it is greater the depth increased.  
#           Count how many times the depth increased.
# Puzzle 2: Compare the most recent 3 depths with the previous 3 depths.
#           If it is greater the depth increased.  
#           Count how many times the depth increased.

with open('../input_files/day_01.txt', 'r') as f:
    depths = [int(i) for i in f.readlines()]

puzzle1Count = sum(1 for i in range(1, len(depths)) if depths[i] > depths[i-1])
puzzle2Count = sum(1 for i in range(3, len(depths)) if depths[i] > depths[i-3])

print("Puzzle 1: ", puzzle1Count)
print("Puzzle 2: ", puzzle2Count)

### Notes ###
# - You must cast the strings as integers, because in python a string 
#   value with three characters (e.g. "100") is considered less than 
#   one with two characters (e.g. "99").
# - Puzzle 2 wants you to compare the sum of the past three values 
#   instead of the most recent. Since two of those values are the 
#   same on both sides of the equation, we can simply compare "i" and "i-3".
#   (e.g. Consider the following array: [A, B, C, D, E, F].  In the first
#   comparison "A + B + C" is compared to "B + C + D". You can remove "B + C"
#   from both sides of the equation and simply compare A and D.)

### Answers ###
# Puzzle 1:  1266
# Puzzle 2:  1217
