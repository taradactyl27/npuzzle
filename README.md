# npuzzle - Alex Taradachuk
# Run using python3 - all other specification followed
 python3 driver.py \<method\> \<board\>
 The method argument will be one of the following:
* bfs (Breadth-First Search)
* dfs (Depth-First Search)
* ast (A-Star Search)

The board argument is a comma-separated list of integers containing no spaces. For
example, to use the bread-first search strategy to solve the input board given by the starting
configuration {0,8,7,6,5,4,3,2,1}, the program will be executed like so (with no spaces between
commas):

python driver.py bfs 0,8,7,6,5,4,3,2,1
