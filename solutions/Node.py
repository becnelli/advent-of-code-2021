import sys

class node:
    def __init__(self, value, name):
        self.value = value
        self.neighbors = []
        self.start = False
        self.end = False
        self.returnRoute = None
        self.returnCost = sys.maxsize
        self.visited = False
        self.name= name

    def __repr__(self):
        result = self.name + ': '
        if self.start:
            result += 'Start '
        elif self.end:
            result += 'End '

        result += str(self.value)
        return str(self.value)
        
    def getValue(self):
        return self.value

    def setStart(self):
        self.start = True
        self.returnCost = 0
        self.returnRoute = None
        return

    def setEnd(self):
        self.end = True
        return
        
    def isStart(self):
        return self.start
        
    def getReturnCost(self):
        return self.returnCost
        
    def getReturnNode(self):
        return self.returnRoute

    def addNeighbor(self, n, setBack=False):
        if not n in self.neighbors:
            self.neighbors.append(n)
        if setBack:
            n.addNeighbor(self)
        return

    def reviewReturnCost(self, n, cost):
        if cost < self.returnCost:
            if self.returnCost != sys.maxsize:
                print(f'{self.name}: return from {n} ({cost}) is better than {self.returnRoute} ({self.returnCost}).')
            self.returnRoute = n
            self.returnCost = cost
        return
    
    def setVisited(self, isVisited):
        self.visited = isVisited
        return
    
    def isVisited(self):
        return self.visited
        
    def getOrderedNeighborsByValue(self, includeVisited=False):
        if includeVisited:
            self.neighbors.sort(key=lambda x: x.value)
            return self.neighbors
        
        results=[n for n in self.neighbors if not n.visited]
        
        results.sort(key=lambda x: x.value)
        
        return results
        
    def getOrderedNeighborsByReturnCost(self, includeVisited=False):
        if includeVisited:
            self.neighbors.sort(key=lambda x: x.returnCost)
            return self.neighbors
        
        results=[n for n in self.neighbors if not n.visited]
        
        results.sort(key=lambda x: x.returnCost)
    
        return results
        
    def printReturnChain(self):
        if self.returnRoute == None:
            print('No return route')
        else:
            retNode = self.returnRoute
            result=str(self.value) + ' -> '
            
            while retNode != None:
                result+=str(retNode.value) + ' -> '
                retNode = retNode.returnRoute
            result += 'start'
            
            print(result)