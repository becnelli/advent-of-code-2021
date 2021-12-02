### --- Day 2: Dive! --- ###

with open('../input_files/day_02.txt', 'r') as f:
    lines = f.readlines()

d1=0
d2=0
f=0
a=0

for line in lines:
    direction,value=line.split()
    v=int(value)
    if direction == "down":
        d1=d1+v
        a =a+v
    elif direction == "up":
        d1=d1-v
        a =a-v
    elif direction == "forward":
        f =f+v
        d2=d2+v*a

print("Puzzle 1: ", d1*f)
print("Puzzle 2: ", d2*f)

### Answers ###
# Puzzle 1: 1727835
# Puzzle 2: 1544000595 
