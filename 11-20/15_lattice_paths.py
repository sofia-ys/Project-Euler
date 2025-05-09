import numpy as np

def moveRight(pos, grid):
    if 0 <= pos[1] < (len(grid[0]) - 1):
        pos[1] = pos[1] + 1
    return pos

def moveDown(pos, grid):
    if 0 <= pos[0] < (len(grid) - 1):
        pos[0] = pos[0] + 1
    return pos

pos = [0,0]
gridSize = 2
grid = np.ones((gridSize, gridSize))
routes = 0

'''unfinished'''