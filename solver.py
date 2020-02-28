import math
import collections
import state

def breadth_first_search(stateInitial):
    #TODO Improve data structures
    frontier = collections.deque()
    explored = set()
    initstate = state.State(stateInitial)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    search_depth = 0
    max_search_depth = 0
    #TODO Keep trac
    while(frontier):
        currentS = frontier.popleft()
        #print("State:",currentS.currentState)
        #print("Frontier:",frontier)
        if(currentS.solved):
            print("Goal Found!")
            print("Nodes Expanded: ",nodesExpanded)
            return
        nodesExpanded += 1
        for nextChild in currentS.children:
            if(nextChild):
                nextState = state.State(nextChild)
                if(not(nextState in explored)):
                    frontier.append(nextState)
                    explored.add(nextState)
                
def depth_first_search(stateInitial):
    frontier = collections.deque()
    explored = set()
    initstate = state.State(stateInitial)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    search_depth = 0
    max_search_depth = 0
    while(frontier):
        currentS = frontier.pop()
        #print("State:",currentS.currentState)
        #print("Frontier:",frontier)
        if(currentS.solved):
            print("Goal Found!")
            print("Nodes Expanded: ",nodesExpanded)
            return
        nodesExpanded += 1
        for nextChild in reversed(currentS.children):
            if(nextChild):
                nextState = state.State(nextChild)
                if(not(nextState in explored)):
                    frontier.append(nextState)
                    explored.add(nextState)
        
        

#def a_star_search():
