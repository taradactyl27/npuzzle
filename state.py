class State:
    def __init__(self, initialS, depth):
        if initialS:
            self.goalState = [0,1,2,3,4,5,6,7,8]
            self.currentState = list(initialS)
            self.searchDepth = depth
            self.solved = self.currentState == self.goalState
            self.cost = self.heuristic()
            if not self.solved:
                self.zeroLoc = self.currentState.index(0)
                self.bounds = self.boundaries((self.zeroLoc))
                self.children = [self.setUp(),self.setDown(),self.setLeft(self.bounds),self.setRight(self.bounds)]
    def __key(self):
        return tuple(self.currentState)
    def __hash__(self):
        return hash(self.__key())
    def __eq__(self,other):
        return self.currentState == other.currentState
    def __ne__(self,other):
        return not (self.currentState == other.currentState)
    def __lt__(self, other):
        return self.cost < other.cost
    def __le__(self, other):
        return self.cost <= other.cost
    def __gt__(self, other):
        return self.cost > other.cost
    def __ge__(self, other):
        return self.cost >= other.cost

    def setUp(self):
        if(self.zeroLoc - 3 >= 0):
            #print("SLIDING UP")
            #TODO Better representation of state to increase efficiency
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc-3] = tempS[self.zeroLoc-3], tempS[self.zeroLoc]
            return tempS
        else:
            return None
    def setDown(self):
        if(self.zeroLoc + 3 <= 8):
            #print("SLIDING DOWN")
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc+3] = tempS[self.zeroLoc+3], tempS[self.zeroLoc]
            return tempS
        else:
            return None
    
    def setLeft(self,bounds):
        if(self.zeroLoc - 1 >= bounds[0]):
            #print("SLIDING LEFT")
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc-1] = tempS[self.zeroLoc-1], tempS[self.zeroLoc]
            return tempS
        else:
            return None

    def setRight(self,bounds):
        if(self.zeroLoc + 1 <= bounds[1]):
            #print("SLIDING RIGHT")
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc+1] = tempS[self.zeroLoc+1], tempS[self.zeroLoc]
            return tempS
        else:
            return None
    def heuristic(self):
        cost = 0
        for x in range(8):
            if (self.currentState[x] != x):
                cost += 1
        return cost
        
    def boundaries(self,zeroInd):
        if (zeroInd < 3):
            return [0,2]
        if (zeroInd < 6):
            return [3,5]
        if (zeroInd < 9):
            return [6,8]