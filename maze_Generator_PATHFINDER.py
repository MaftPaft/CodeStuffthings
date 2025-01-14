from maze_generator import MakeMaze


branch=[] # not very important but tracks the dead ends as well by recording the path
solution=[] # path to the goal
g=MakeMaze(13,13)
g.generate(2) # generates maze; 2 is the goal target in the maze
def pathfinder(path=[[1,1]]):
    unvisited=[i for i in g.getneighbours(path[-1][0],path[-1][1],1) if g.grid[i[1]][i[0]]==0 or g.grid[i[1]][i[0]]==2]
    
    if not unvisited:
        branch.append(path)
        return
    if 2 in [g.grid[i[1]][i[0]] for i in unvisited]:
        unvisited.clear()
        solution.append(path)
        return
    for n in unvisited:
        g.grid[path[-1][1]][path[-1][0]]=5
        pathfinder(path+[n])
        g.grid[path[-1][1]][path[-1][0]]=0
pathfinder()
for s in solution[-1]:
    g.grid[s[1]][s[0]]=4 # Draws a path to the solution using 4s

# # # # OUTPUT
for m in g.grid:
    print(m)
# RESULT:
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [1, 4, 4, 4, 4, 4, 1, 0, 0, 4, 4, 4, 1]
# [1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 4, 1]
# [1, 0, 0, 0, 1, 4, 4, 4, 1, 4, 1, 4, 1]
# [1, 1, 1, 0, 1, 1, 1, 4, 1, 4, 1, 4, 1]
# [1, 4, 4, 4, 4, 4, 1, 4, 4, 4, 1, 4, 1]
# [1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1, 4, 1]
# [1, 4, 1, 2, 4, 4, 1, 4, 4, 4, 1, 4, 1]
# [1, 4, 1, 1, 1, 1, 1, 4, 1, 4, 1, 4, 1]
# [1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 1, 4, 1]
# [1, 0, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 1]
# [1, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
