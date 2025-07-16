import matplotlib.pyplot as plt
import matplotlib.colors as col
import numpy as np
import random, math

SIZE = 10
DIMENSIONS = 2 

CLEAR = 0
OBJECT = 1
START = 2
GOAL = 3

colors = ["white","black","green","red"]
cmap = col.ListedColormap(colors)
grid = np.zeros((SIZE, SIZE), dtype=int)

def gaussian_islandz(count = 3):
    for _ in range(count):
        coord = [0,0]
        for dim in range(DIMENSIONS):
            coord[dim] = random.randint(0,SIZE-1)

        curr_x, curr_y = coord[0],coord[1]
        grid[curr_x,curr_y] = OBJECT

        gaussian_fill(curr_x, curr_y, 0.5)

def gaussian_fill(x,y, prob):
    cutoff = 0.3
    attenuation  = 0.3
    if prob <= cutoff: return
    for op in [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[-1,1]]:
        new_x, new_y = x+op[0], y+op[1]
        if (0 <= new_x < SIZE and 0 <= new_y < SIZE):
            grid[new_x,new_y] = OBJECT if random.random() <= (prob if (op[0] == 0 or op[1] == 0) else prob * math.sqrt(2)) else CLEAR      
            gaussian_fill(new_x, new_y, prob * attenuation)

def main():
    gaussian_islandz()
    plt.figure(figsize=(10,10))
    plt.imshow(grid, cmap, interpolation='none', origin='lower')
    plt.show()

if __name__ == '__main__':
    main()