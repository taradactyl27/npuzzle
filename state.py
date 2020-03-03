######################
# Alex Taradachuk    #
# Prof. Raja         #
# CSCI-350           #
# Assignment 1       #
######################
class State:
    def __init__(self, initialS, depth,parentN,moveMade, ast = False):
        if initialS:
            self.goalState = [0,1,2,3,4,5,6,7,8] #goal state to check is solved
            self.parent = parentN #parents node to be used for constructing path when goal is found
            self.currentState = list(initialS) #fast copy input list
            self.searchDepth = depth #keep track of depth
            self.path = (parentN,moveMade) #list comprised of move used to get to this node and parent node
            self.solved = self.currentState == self.goalState #simple solved equality
            if ast:
                self.cost = self.searchDepth + self.heuristic() #add manhattan distance heuristic is A-Star search is being performed
            if not self.solved: #determine children if state is not solved
                self.zeroLoc = self.currentState.index(0) #get zero location to be used in swapping numbers
                self.bounds = self.boundaries((self.zeroLoc)) #get boundaries for swapping horizontally
                self.children = [self.setUp(),self.setDown(),self.setLeft(self.bounds),self.setRight(self.bounds)] #set children to be int lists that will be generated into a state when needed
    ################ HASHING CAPABILITY ##########################################
    def __key(self):
        return tuple(self.currentState)
    def __hash__(self):
        return hash(self.__key())
    ################ EQUALITIES FOR PRIORITY QUEUE BASED ON COST #################
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
    ##############################################################################
    
    def setUp(self): #Return array of ints representing the state after an up move is made
        if(self.zeroLoc - 3 >= 0): 
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc-3] = tempS[self.zeroLoc-3], tempS[self.zeroLoc]
            return tempS
        else:
            return None
    def setDown(self): #Return array of ints representing the state after a down move is made
        if(self.zeroLoc + 3 <= 8):
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc+3] = tempS[self.zeroLoc+3], tempS[self.zeroLoc]
            return tempS
        else:
            return None
    
    def setLeft(self,bounds): #Return array of ints representing the state after a left move is made
        if(self.zeroLoc - 1 >= bounds[0]):
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc-1] = tempS[self.zeroLoc-1], tempS[self.zeroLoc]
            return tempS
        else:
            return None

    def setRight(self,bounds): #Return array of ints representing the state after a right move is made
        if(self.zeroLoc + 1 <= bounds[1]):
            tempS = list(self.currentState)
            tempS[self.zeroLoc],tempS[self.zeroLoc+1] = tempS[self.zeroLoc+1], tempS[self.zeroLoc]
            return tempS
        else:
            return None

    def heuristic(self): #heuristic function
        cost = 0
        for x in range(8):
            if (self.currentState[x] != x) and self.currentState[x]!=0: #compute manhattan distance if index does not equal to number found or if the number is 0
                cost += (abs(self.currentState[x]/3-x/3) + abs(self.currentState[x]%3-x%3)) #manhattan distance of 3x3 grid based on 1d vector positions
        return cost
        
    def boundaries(self,zeroInd): #boundaries for horizontal swaps
        if (zeroInd < 3):
            return [0,2]
        if (zeroInd < 6):
            return [3,5]
        if (zeroInd < 9):
            return [6,8]