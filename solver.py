import math
import collections

def breadth_first_search(state):
    #TODO Improve data structures
    frontier = collections.deque()
    explored = collections.deque()
    frontier.append(state)
    nodesExpanded = -1
    search_depth = 0
    max_search_depth = 0
    #TODO Keep trac
    while(frontier):
        currentS = frontier.popleft()
        #print("State:",currentS)
        #print("Frontier:",frontier)
        if(currentS == [0,1,2,3,4,5,6,7,8]):
            print("Goal Found!")
            print("Nodes Expanded: ",nodesExpanded)
            return
        nodesExpanded += 1
        #TODO UNNECESSARILY ------ Keep track of 0 index for improved efficiency over the long run
        indexOfEmpty = currentS.index(0)
        #print(indexOfEmpty)
        bounds = boundaries(indexOfEmpty)
        #print(bounds)
        if(indexOfEmpty - 3 >= 0):
            #print("SLIDING UP")
            #TODO Better representation of state to increase efficiency
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty-3] = tempS[indexOfEmpty-3], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        if(indexOfEmpty + 3 <= 8):
            #print("SLIDING DOWN")
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty+3] = tempS[indexOfEmpty+3], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        if(indexOfEmpty - 1 >= bounds[0]):
            #print("SLIDING LEFT")
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty-1] = tempS[indexOfEmpty-1], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        if(indexOfEmpty + 1 <= bounds[1]):
            #print("SLIDING RIGHT")
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty+1] = tempS[indexOfEmpty+1], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        
def boundaries(pos):
    if (pos < 3):
        return [0,2]
    if (pos < 6):
        return [3,5]
    if (pos < 9):
        return [6,8]

def depth_first_search(state):
    frontier = collections.deque()
    explored = collections.deque()
    frontier.append(state)
    nodesExpanded = -1
    search_depth = 0
    max_search_depth = 0
    while(frontier):
        currentS = frontier.pop()
        #print("State:",currentS)
        #print("Frontier:",frontier)
        if(currentS == [0,1,2,3,4,5,6,7,8]):
            print("Goal Found!")
            print("Nodes Expanded: ",nodesExpanded)
            return
        nodesExpanded += 1
        indexOfEmpty = currentS.index(0)
        #print(indexOfEmpty)
        bounds = boundaries(indexOfEmpty)
        #print(bounds)
        if(indexOfEmpty + 1 <= bounds[1]):
            #print("SLIDING RIGHT")
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty+1] = tempS[indexOfEmpty+1], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        if(indexOfEmpty - 1 >= bounds[0]):
            #print("SLIDING LEFT")
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty-1] = tempS[indexOfEmpty-1], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        if(indexOfEmpty + 3 <= 8):
            #print("SLIDING DOWN")
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty+3] = tempS[indexOfEmpty+3], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        if(indexOfEmpty - 3 >= 0):
            #print("SLIDING UP")
            tempS = list(currentS)
            tempS[indexOfEmpty],tempS[indexOfEmpty-3] = tempS[indexOfEmpty-3], tempS[indexOfEmpty]
            #print(tempS)
            if not(tempS in explored):
                frontier.append(tempS)
                #print(frontier)
                explored.append(tempS)
        
        

#def a_star_search():
