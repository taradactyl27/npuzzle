import math
import collections
import state
import sys
from queue import PriorityQueue

def breadth_first_search(stateInitial):
    frontier = collections.deque()
    explored = set()
    initstate = state.State(stateInitial,0,None,None)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    moves = ["Up","Down","Left","Right"]
    while(frontier):
        currentS = frontier.popleft()
        if(currentS.solved):
            path_to_goal = []
            while currentS.path[0]:
                path_to_goal.insert(0,currentS.path[1])
                currentS.path = currentS.path[0].path
            sys.stdout = open('output.txt',"w")
            print("path_to_goal:",path_to_goal)
            print("cost_of_path:",currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            sys.stdout.close()
            return
        nodesExpanded += 1
        for i in range(4):
            nextChild = currentS.children[i]
            if(nextChild):
                nextState = state.State(nextChild,currentS.searchDepth+1,currentS,moves[i])
                max_search_depth = max(max_search_depth,nextState.searchDepth)
                if(not(nextState in explored)):
                    frontier.append(nextState)
                    explored.add(nextState)
                
def depth_first_search(stateInitial):
    frontier = collections.deque()
    explored = set()
    initstate = state.State(stateInitial,0,None,None)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    moves = ["Up","Down","Left","Right"]
    while(frontier):
        currentS = frontier.pop()
        max_search_depth = max(max_search_depth,currentS.searchDepth)
        if(currentS.solved):
            path_to_goal = []
            while currentS.path[0]:
                path_to_goal.insert(0,currentS.path[1])
                currentS.path = currentS.path[0].path
            sys.stdout = open('output.txt',"w")
            print("path_to_goal:",path_to_goal)
            print("cost_of_path:",currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            sys.stdout.close()
            return
        nodesExpanded += 1
        for i in range(4):
            nextChild = currentS.children[3-i]
            if(nextChild):
                nextState = state.State(nextChild,currentS.searchDepth+1,currentS,moves[3-i])
                if(not(nextState in explored)):
                    frontier.append(nextState)
                    explored.add(nextState)
        

def a_star_search(stateInitial):
    frontier = PriorityQueue()
    explored = set()
    initstate = state.State(stateInitial,0,None,None,True)
    frontier.put(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    moves = ["Up","Down","Left","Right"]
    while(frontier):
        currentS = frontier.get()
        max_search_depth = max(max_search_depth,currentS.searchDepth)
        if(currentS.solved):
            path_to_goal = []
            while currentS.path[0]:
                path_to_goal.insert(0,currentS.path[1])
                currentS.path = currentS.path[0].path
            sys.stdout = open('output.txt',"w")
            print("path_to_goal:",path_to_goal)
            print("cost_of_path:",currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            sys.stdout.close()
            return
        nodesExpanded += 1
        for i in range(4):
            nextChild = currentS.children[i]
            if(nextChild):
                nextState = state.State(nextChild,currentS.searchDepth+1,currentS,moves[i],True)
                if(not(nextState in explored)):
                    frontier.put(nextState)
                    explored.add(nextState)