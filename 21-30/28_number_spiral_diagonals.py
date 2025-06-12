import numpy as np
size = 5
maxnum = size*size
spiral = np.zeros((size, size))
# i, j = int(size/2), int(size/2)
i, j = 0, -1
cum = np.sum(np.cumsum(np.ones((size, size))))

# spiral[i, j] = 1
counter = 1
# while np.sum(spiral) < cum:
#     spiral[i, j] = maxnum
#     spiral[i, ]