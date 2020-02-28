import math
import collections
import state
from queue import PriorityQueue

def breadth_first_search(stateInitial):
    #TODO Improve data structures
    frontier = collections.deque()
    explored = set()
    initstate = state.State(stateInitial,0)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    while(frontier):
        currentS = frontier.popleft()
        #print("State:",currentS.currentState)
        #print("Frontier:",frontier)
        if(currentS.solved):
            print("Goal Found!")
            print("cost_of_path:",currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            return
        nodesExpanded += 1
        for nextChild in currentS.children:
            if(nextChild):
                nextState = state.State(nextChild,currentS.searchDepth+1)
                max_search_depth = max(max_search_depth,nextState.searchDepth)
                if(not(nextState in explored)):
                    frontier.append(nextState)
                    explored.add(nextState)
                
def depth_first_search(stateInitial):
    frontier = collections.deque()
    explored = set()
    initstate = state.State(stateInitial,0)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    while(frontier):
        currentS = frontier.pop()
        #print("State:",currentS.currentState)
        #print("Frontier:",frontier)
        if(currentS.solved):
            print("Goal Found!")
            print("cost_of_path:", currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            return
        max_search_depth = max(max_search_depth,currentS.searchDepth)
        nodesExpanded += 1
        for nextChild in reversed(currentS.children):
            if(nextChild):
                nextState = state.State(nextChild,currentS.searchDepth+1)
                if(not(nextState in explored)):
                    frontier.append(nextState)
                    explored.add(nextState)
        

def a_star_search(stateInitial):
    frontier = PriorityQueue()
    explored = set()
    initstate = state.State(stateInitial,0)
    frontier.put(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    while(frontier):
        currentS = frontier.get()
        #print("State:",currentS.currentState)
        #print("Frontier:",frontier)
        max_search_depth = max(max_search_depth,currentS.searchDepth)
        if(currentS.solved):
            print("Goal Found!")
            print("cost_of_path:", currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            return
        nodesExpanded += 1
        for nextChild in reversed(currentS.children):
            if(nextChild):
                nextState = state.State(nextChild,currentS.searchDepth+1)
                if(not(nextState in explored)):
                    frontier.put(nextState)
                    explored.add(nextState)