######################
# Alex Taradachuk    #
# Prof. Raja         #
# CSCI-350           #
# Assignment 1       #
######################
import sys
import resource
import solver
import time
#Input the board argument by splitting it based on comma and mapping to integers
boardInput = sys.argv[2]
boardInput = boardInput.split(',')
boardInput = list(map(int,boardInput))
searchMethod = sys.argv[1] #Input the search method
start_time = time.time() #start stopwatch
if(searchMethod == "dfs"):
    solver.depth_first_search(boardInput)
if(searchMethod == "bfs"):
    solver.breadth_first_search(boardInput)
if(searchMethod == "ast"):
    solver.a_star_search(boardInput)
#Final statistic appending to output file
sys.stdout = open("output.txt","a")
print("running_time:" , str.format("{0:.8f}",(time.time() - start_time)))
print("max_ram_usage:",str.format("{0:.8f}",(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/100000)))
sys.stdout.close()
