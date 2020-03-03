######################
# Alex Taradachuk    #
# Prof. Raja         #
# CSCI-350           #
# Assignment 1       #
######################
import math
import collections
import state
import sys
from queue import PriorityQueue

def breadth_first_search(stateInitial): 
    frontier = collections.deque() #use deque as the frontier
    explored = set() #set for all explored states
    initstate = state.State(stateInitial,0,None,None)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    moves = ["Up","Down","Left","Right"] #moves to be referenced later when exploring children
    while(frontier):
        currentS = frontier.popleft() #pop left of deque to make it FIFO
        if(currentS.solved): #solution check
            path_to_goal = [] #initiate path array
            while currentS.path[0]: #trace back parent nodes until null is reached adding each move at each point
                path_to_goal.insert(0,currentS.path[1])
                currentS.path = currentS.path[0].path
            ###############STATISTIC OUTPUT######################
            sys.stdout = open('output.txt',"w")
            print("path_to_goal:",path_to_goal)
            print("cost_of_path:",currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            sys.stdout.close()
            #####################################################
            return
        nodesExpanded += 1 #increment nodes expanded
        for i in range(4): #loop through 4 numbers representing each possible direction
            nextChild = currentS.children[i]
            if(nextChild): #if next state exists, generate it and add to frontier and explored lists
                nextState = state.State(nextChild,currentS.searchDepth+1,currentS,moves[i])
                max_search_depth = max(max_search_depth,nextState.searchDepth)
                if(not(nextState in explored)): #might cause inefficiency since state is generated before it is checked for membership in frontier but didn't affect performance in test cases
                    frontier.append(nextState)
                    explored.add(nextState)
                
def depth_first_search(stateInitial):
    frontier = collections.deque() #use deque as a frontier 
    explored = set() #set for all explored states
    initstate = state.State(stateInitial,0,None,None)
    frontier.append(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    moves = ["Up","Down","Left","Right"] #moves to be referenced later when exploring children
    while(frontier):
        currentS = frontier.pop() #pop from right side to make it FILO
        max_search_depth = max(max_search_depth,currentS.searchDepth)
        if(currentS.solved):
            path_to_goal = []
            while currentS.path[0]:
                path_to_goal.insert(0,currentS.path[1])
                currentS.path = currentS.path[0].path
            ###############STATISTIC OUTPUT######################
            sys.stdout = open('output.txt',"w")
            print("path_to_goal:",path_to_goal)
            print("cost_of_path:",currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            sys.stdout.close()
            #####################################################
            return
        nodesExpanded += 1 #increment nodes expanded
        for i in range(4): #loop through 4 numbers representing each possible direction
            nextChild = currentS.children[3-i] #index (3-i) to go through list in reverse so stack retrives in UDLR order
            if(nextChild): #if next state exists, generate it and add to frontier and explored lists
                nextState = state.State(nextChild,currentS.searchDepth+1,currentS,moves[3-i])
                if(not(nextState in explored)):
                    frontier.append(nextState)
                    explored.add(nextState)
        

def a_star_search(stateInitial):
    frontier = PriorityQueue() #use priority queue as frontier for a-star
    explored = set() #use set for explored states
    initstate = state.State(stateInitial,0,None,None,True)
    frontier.put(initstate)
    explored.add(initstate)
    nodesExpanded = 0
    max_search_depth = 0
    moves = ["Up","Down","Left","Right"] #moves to be referenced later when exploring children
    while(frontier):
        currentS = frontier.get() #get from priority queue
        max_search_depth = max(max_search_depth,currentS.searchDepth)
        if(currentS.solved):
            path_to_goal = []
            while currentS.path[0]:
                path_to_goal.insert(0,currentS.path[1])
                currentS.path = currentS.path[0].path
            ###############STATISTIC OUTPUT######################
            sys.stdout = open('output.txt',"w")
            print("path_to_goal:",path_to_goal)
            print("cost_of_path:",currentS.searchDepth)
            print("nodes_expanded:",nodesExpanded)
            print("search_depth:",currentS.searchDepth)
            print("max_search_depth:",max_search_depth)
            sys.stdout.close()
            #####################################################
            return
        nodesExpanded += 1 #increment nodes expanded
        for i in range(4): #loop through 4 numbers representing each possible direction
            nextChild = currentS.children[i]
            if(nextChild): #same process as all other searches
                nextState = state.State(nextChild,currentS.searchDepth+1,currentS,moves[i],True)
                if(not(nextState in explored)):
                    frontier.put(nextState)
                    explored.add(nextState)