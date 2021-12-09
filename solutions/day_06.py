### --- Day 4: --- ###

with open('../input_files/day_06.txt', 'r') as f:
    lines = f.readlines()
    
fish=[int(f) for f in lines[0].split(',')]

def bruteForce(fishArray, days):
    for i in range(days):
        for f in range(len(fishArray)):
            if fishArray[f] == 0:
                fishArray.extend([8])
                fishArray[f]=6
            else:
                fishArray[f] -= 1
    return len(fishArray)
    
def optimize(fishArray, days):
    x = {}

    for a in range(0,9):
        x[a]=0
        
    for f in fishArray:
        x[f] += 1
    
    for d in range(days):
        mommaFish=x[0] # move fully gestated fish to 9 since they had babies

        for i in range(1, 9):
            x[i-1]=x[i]
            
        x[8] = mommaFish # mommaFish create one baby fish
        x[6] += mommaFish # add 9 to six because the fish that had babies also start their cycle again        
    
    t=0
    for i in range(9):
        t+=x[i]
                
    return t
    
days = 80
#numFish=bruteForce(fish, days)
numFish=optimize(fish, days)

print(f'After {days} days we have {numFish} fish!')

days = 256
#numFish=bruteForce(fish, days)
numFish=optimize(fish, days)

print(f'After {days} days we have {numFish} fish!')

