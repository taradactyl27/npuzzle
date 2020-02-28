import sys
import resource
import solver

def main():
    boardInput = sys.argv[2]
    boardInput = boardInput.split(',')
    boardInput = list(map(int,boardInput))
    print(solver.depth_first_search(boardInput))
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

main()