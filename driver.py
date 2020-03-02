import sys
import resource
import solver
import time

boardInput = sys.argv[2]
boardInput = boardInput.split(',')
boardInput = list(map(int,boardInput))
searchMethod = sys.argv[1]
start_time = time.time()
if(searchMethod == "dfs"):
    solver.depth_first_search(boardInput)
if(searchMethod == "bfs"):
    solver.breadth_first_search(boardInput)
if(searchMethod == "ast"):
    solver.a_star_search(boardInput)
sys.stdout = open("output.txt","a")
print("running_time:" ,time.time() - start_time)
print("max_ram_usage:",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000)
sys.stdout.close()
